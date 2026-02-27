// Primeiro exemplo PIC24

#include <xc.h>

#define FCY 10000000UL

#include <libpic30.h>

typedef void (*f_ptr)(void);

void config_ports();
void task_1();
void task_2();
void ler_botao();

// Fila de tarefas
f_ptr fila[2];
int next = 0;

int main()
{
    config_ports();
    
    // Instalar as tarefas
    fila[0] = task_1;
    fila[1] = task_2;
    
    while (1) {
        ler_botao();
    }
    
    POSCMOD_NONE;

    return 0;
}

void config_ports()
{
    TRISCbits.TRISC14 = 0; // Sa�da de dados
    TRISCbits.TRISC15 = 0; // Sa�da de dados
    TRISEbits.TRISE0  = 0;
}

void task_1()
{
    LATCbits.LATC14 = ~PORTCbits.RC14;
    __delay_ms(50);
}

void task_2()
{
    //LATCbits.LATC15 = ~PORTCbits.RC15;
    LATEbits.LATE0 = ~PORTEbits.RE0;
    __delay_ms(50);
}

void ler_botao()
{
    if (PORTFbits.RF0 == 1) {
        fila[next]();
        next = (next + 1) % 2;
    }
}
