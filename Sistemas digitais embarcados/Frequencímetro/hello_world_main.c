#include <stdio.h>
#include "sdkconfig.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "esp_timer.h"

volatile int pulsos = 0;

// Função de interrupção
void IRAM_ATTR INTERRUPCAO(void *arg) {
    pulsos++;
}

void app_main(void)
{
    gpio_num_t gpio_num = GPIO_NUM_15;

    /* Set the GPIO as a input */
        gpio_install_isr_service(1);

    gpio_set_direction(gpio_num, GPIO_MODE_INPUT);
    /* Set the GPIO pull */
    gpio_set_pull_mode(gpio_num, GPIO_PULLUP_ONLY);

    gpio_set_intr_type(gpio_num, GPIO_INTR_NEGEDGE);
    gpio_isr_handler_add(gpio_num, INTERRUPCAO, (void*) gpio_num);

    int64_t start_time = esp_timer_get_time();  // Tempo inicial em microsegundos
    int pulsos_old = 0;
    while (1)
    {
        if ((esp_timer_get_time() - start_time) >= 1000000) 
        {
            int delta_pulsos = pulsos - pulsos_old;  // Calcula a diferença de pulsos
            pulsos_old = pulsos;  // Atualiza o valor anterior

            float frequencia = delta_pulsos;  // A diferença de pulsos por segundo é a frequência em Hz

            printf("Frequência: %.2f Hz\n", frequencia);

            start_time = esp_timer_get_time();
        }

        vTaskDelay(1);  // Pequeno atraso para não sobrecarregar o loop
    }
}
