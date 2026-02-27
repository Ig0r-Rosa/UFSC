#include "user_app.h"
#include "FreeRTOS.h"
#include "task.h"

int main(void)
{
    config_user_app();

    vTaskStartScheduler();

    while (1);
}