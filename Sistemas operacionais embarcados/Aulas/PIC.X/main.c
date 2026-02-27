// Primeiro exemplo PIC24

#include <xc.h>

#define FCY 10000000UL

#include <libpic30.h>

typedef void (*f_ptr)(void);

void config_ports();
void task_1();
void task_2();
void ler_botao();
void config_int0();

// tratador de interrupção
void __attribute__((interrupt())) _INT0Interrupt(void);


// Fila de tarefas
f_ptr fila[2];
int next = 0;

int main()
{
    config_ports();
    config_int0();
    
    // Instalar as tarefas
    fila[0] = task_1;
    fila[1] = task_2;
    
    while (1) 
    {
        
    }
   
    return 0;
}

void config_ports()
{
    TRISCbits.TRISC14 = 0; // Saï¿½da de dados
    TRISCbits.TRISC15 = 0; // Saï¿½da de dados
    TRISEbits.TRISE0  = 0;
}

void task_1()
{
    //while(1)
    //{
        LATCbits.LATC14 = ~PORTCbits.RC14;
    //    __delay_ms(50);
    //}
}

void task_2()
{
    //LATCbits.LATC15 = ~PORTCbits.RC15;
    LATEbits.LATE0 = ~PORTEbits.RE0;
    //__delay_ms(50);
}

void ler_botao()
{
    if (PORTFbits.RF0 == 1) 
    {
        fila[next]();
        next = (next + 1) % 2;
    }
}

void config_int0()
{
    // prioridade de cpu
    SRbits.IPL = 0b100; // prioridade 4
    INTCON2bits.INT0EP = 0; // borda de subida (sinal positivo)
    IFS0bits.INT0IF = 0;
    IEC0bits.INT0IE = 1;
    IPC0bits.INT0IP = 0b100;
    __builtin_enable_interrupts();
}

void __attribute__((interrupt())) _INT0Interrupt(void)
{
    fila[next]();
    next = (next + 1) % 2;
    IFS0bits.INT0IF = 0;
}
