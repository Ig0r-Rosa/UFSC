#include "user_app.h"
#include "queue.h"
#include "semphr.h"

SemaphoreHandle_t s;
QueueHandle_t fila;
uint16_t tempo_injecao;
volatile uint8_t freio_acionado = 0;
volatile uint8_t tarefa_estabilidade_ativa = 0;

void config_user_app()
{
    TRISGbits.TRISG0    = 0; // Acelerador 50%+
    TRISGbits.TRISG1    = 0; // Freio ativo
    TRISGbits.TRISG2    = 0; // Controle de estabilidade
    TRISGbits.TRISG3    = 0; // DEBUG
    
    s = xSemaphoreCreateBinary();    
    fila = xQueueCreate(5, sizeof(char));
    
    // Configura conversor AD
    config_adc();
    config_pwm();
    config_interrupcao();
    
    xTaskCreate(tarefa_estabilidade, "Estabilidade", 128, NULL, 4, NULL);
    xTaskCreate(tarefa_acelerador, "Acelerador", 128, NULL, 3, NULL);
    xTaskCreate(tarefa_controle_central, "Central", 128, NULL, 2, NULL);
    xTaskCreate(tarefa_injecao_eletronica, "Injecao", 128, NULL, 1, NULL);
}

void config_adc()
{
    // Configuração do conversor AD
    AD1CON3bits.ADRC    = 1;            // Clock interno
    AD1CON3bits.SAMC    = 0b11111;      // Tad = 31
    AD1CON3bits.ADCS    = 0b00111111;   //  64 * TCY
    AD1CHSbits.CH0SA    = 0b0000;
    AD1CON2bits.VCFG    = 0b011;
    AD1CON1bits.SAMP    = 0;  
    AD1CON1bits.ADON    = 1;            // Liga conversor AD
}

void config_pwm()
{
    // Configura RD2 como saída do PWM (OC1)
    TRISDbits.TRISD2 = 0;

    // Configura Timer2
    T2CONbits.TON = 0;         // Desliga Timer2
    T2CONbits.TCKPS = 0b01;    // Prescaler 1:8
    PR2 = 499;               
    TMR2 = 0;
    T2CONbits.TON = 1;         // Liga Timer2

    OC1CONbits.OCM = 0b000;    // Desliga temporariamente
    OC1R = PR2;             
    OC1RS = PR2;              
    OC1CONbits.OCTSEL = 0;     
    OC1CONbits.OCM = 0b110;    // Modo PWM
}

void config_interrupcao()
{
    // Configura pino como entrada para interrupção externa 1 (INT1 = RE7)
    TRISEbits.TRISE7 = 1;
    INTCON2bits.INT1EP = 0;      
    IFS1bits.INT1IF = 0;         // Limpa a flag de interrupção
    IEC1bits.INT1IE = 1;         // Habilita interrupção INT1
    __builtin_enable_interrupts();
}

void __attribute__((interrupt, no_auto_psv)) _INT1Interrupt(void)
{
    IFS1bits.INT1IF = 0;
    
    if (PORTEbits.RE8 == 1)
    {
        if(tarefa_estabilidade_ativa == 0)
        {
            tarefa_estabilidade_ativa = 1;
            freio_acionado = 1;
        }
    }
}

uint16_t le_adc()
{
    AD1CON1bits.SAMP   = 1;
    vTaskDelay(5);
    AD1CON1bits.SAMP   = 0;
    
    while (!AD1CON1bits.DONE);
    
    return ADC1BUF0;
}

void tarefa_acelerador(void *pvParameters)
{
    uint16_t posicao_pedal;
    uint8_t valor_enviar;

    #define NUM_LEITURAS 3
    uint16_t leituras[NUM_LEITURAS] = {0};
    uint8_t indice = 0;
    uint32_t soma = 0;

    while (1)
    {
        soma -= leituras[indice];
        leituras[indice] = le_adc();
        soma += leituras[indice];
        indice = (indice + 1) % NUM_LEITURAS;

        posicao_pedal = soma / NUM_LEITURAS;

        if (posicao_pedal > 512)
        {
            LATGbits.LATG0 = 1;
        }
        else
        {
            LATGbits.LATG0 = 0;
        }

        valor_enviar = (uint8_t)(posicao_pedal >> 2);
        xQueueSend(fila, &valor_enviar, portMAX_DELAY);

        vTaskDelay(pdMS_TO_TICKS(25));
    }
}

void tarefa_controle_central(void *pvParameters)
{
    uint8_t posicao_pedal;

    while (1)
    {
        if (xQueueReceive(fila, &posicao_pedal, portMAX_DELAY) == pdTRUE)
        {
            tempo_injecao = posicao_pedal * 4;
        }

        vTaskDelay(pdMS_TO_TICKS(10));
    }
}

void pwm_set_duty(uint8_t channel, uint16_t duty) 
{
    if (channel == 1) 
    {
        uint16_t max_duty = PR2;
        if (duty > max_duty) 
        {
            duty = max_duty;
        }
        
        OC1RS = duty;
    }
}

void tarefa_injecao_eletronica(void *pvParameters)
{
    while (1)
    {
        uint16_t tempo;

        if (freio_acionado == 1)
        {
            tempo = 0;
        }
        else
        {
            tempo = tempo_injecao;
        }

        if (tempo > 255)
        {
            pwm_set_duty(1, 255);
        }
        else
        {
            pwm_set_duty(1, tempo);
        }

        vTaskDelay(pdMS_TO_TICKS(5));
    }
}

void tarefa_estabilidade(void *pvParameters)
{
    while(1)
    {
        vTaskDelay(pdMS_TO_TICKS(10));
        if(PORTEbits.RE8 == 1 && tarefa_estabilidade_ativa == 1)
        {
            __builtin_disable_interrupts();
            
            LATGbits.LATG1 = 1;
            LATGbits.LATG2 = ~LATGbits.LATG2;
            
            __builtin_enable_interrupts();
        }
        else
        {
            LATGbits.LATG1 = 0;
            LATGbits.LATG2 = 0;
            tarefa_estabilidade_ativa = 0;
            freio_acionado = 0;
        }
    }
}