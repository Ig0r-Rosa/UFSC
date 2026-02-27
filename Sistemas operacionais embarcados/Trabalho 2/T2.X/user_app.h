#ifndef USER_APP_H
#define USER_APP_H
#include "FreeRTOS.h"
#include "task.h"
#include "xc.h"
#include "FreeRTOSConfig.h"
#include "queue.h"
#include "semphr.h"

#define FCY 40000000UL          // 40MHz
#define NUM_LEITURAS 3          // Para média móvel

// Estruturas de comunicação
extern QueueHandle_t acelerador_queue;
extern SemaphoreHandle_t injecao_mutex;

// Variáveis globais
extern uint16_t tempo_injecao;
extern volatile uint8_t freio_acionado;
extern volatile uint8_t tarefa_estabilidade_ativa;

// Protótipos
void config_user_app(void);
void config_adc(void);
void config_pwm(void);
void config_interrupcao(void);

void tarefa_acelerador(void *pvParameters);
void tarefa_controle_central(void *pvParameters);
void tarefa_injecao_eletronica(void *pvParameters);
void tarefa_estabilidade(void *pvParameters);
void __attribute__((interrupt, no_auto_psv)) _INT1Interrupt(void); 

uint16_t le_adc(void);
void pwm_set_duty(uint8_t channel, uint16_t duty);

#endif