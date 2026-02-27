#include <xc.h>

#define STACK_SIZE 128
#define READY_QUEUE_SIZE 3

// TIPOS DE DADOS
typedef void (*f_ptr)(void);

typedef enum {READY = 0, RUNNING = 1, WAITING = 2} state_t;

typedef struct tcb {
    unsigned char id;
    unsigned char priority;
    state_t state;
    uint16_t *sp;
    f_ptr task_f;
    uint16_t stack[STACK_SIZE];
} tcb_t;

void timer_config();

// FILA DE TAREFAS
tcb_t tasks[READY_QUEUE_SIZE];
unsigned int task_running = 0;
unsigned int nr_of_tasks = 0;

// CHAMADA DE SISTEMAS
void create_task(unsigned char id, unsigned char priority, f_ptr task);
void __attribute__((interrupt)) _T1Interrupt(void);
unsigned int round_robin();

// TAREFAS DE USUÁRIO
void tarefa_1();
void tarefa_2();
void tarefa_3();

void config_hw()
{
    TRISCbits.TRISC14 = 0;
    TRISEbits.TRISE0 = 0;
    TRISEbits.TRISE1 = 0;
}

int main(){
    
    timer_config();
    config_hw();

    create_task(1, 3, tarefa_1);
    create_task(2, 2, tarefa_2);
    create_task(3, 1, tarefa_3);

    __builtin_enable_interrupts();

    while(1);

    return 0;
};

// CHAMADA DE SISTEMAS
void create_task(unsigned char id, unsigned char priority, f_ptr task){
    tasks[nr_of_tasks].id = id;
    tasks[nr_of_tasks].priority = priority;
    tasks[nr_of_tasks].state = READY;
    tasks[nr_of_tasks].task_f = task;
    tasks[nr_of_tasks].sp = &tasks[nr_of_tasks].stack[STACK_SIZE-1];
    
    *tasks[nr_of_tasks].sp-- = (uint16_t)task;
    
    *tasks[nr_of_tasks].sp-- = 0;
    
    *tasks[nr_of_tasks].sp-- = CORCON;
    *tasks[nr_of_tasks].sp-- = SR;
    *tasks[nr_of_tasks].sp-- = RCOUNT;
    *tasks[nr_of_tasks].sp-- = PSVPAG;
    *tasks[nr_of_tasks].sp-- = TBLPAG; 
    
    for(int i = 0; i < 16; i++)
    {
        *tasks[nr_of_tasks].sp-- = 0x0000;
    }
    
    nr_of_tasks++;
}

void __attribute__((interrupt)) _T1Interrupt(void)
{
    IFS0bits.T1IF = 0;
    PR1 = 100;

    // SALVA CONTEXTO
    if(tasks[task_running].state == RUNNING)
    {
    asm("PUSH CORCON");
    asm("PUSH SR");
    asm("PUSH RCOUNT");
    asm("PUSH PSVPAG");
    asm("PUSH TBLPAG");
    asm("PUSH W1");
    asm("PUSH.D W2");
    asm("PUSH.D W4");
    asm("PUSH.D W6");
    asm("PUSH.D W8");
    asm("PUSH.D W10");
    asm("PUSH.D W12");
    asm("PUSH W14");
    asm("MOV %0, W0" :: "r"(tasks[task_running].sp));
    asm("MOV W15, [W0]");
    
    tasks[task_running].state = READY;
    }
        
    // SELECIONA A PRÓXIMA TAREFA A ENTRAR EM EXECUÇÃO
    task_running = round_robin();

    // RESTAURA CONTEXTO
    asm("MOV %0, W0" :: "r"(tasks[task_running].sp));
    asm("MOV [W0], W15");
    asm("POP W14");
    asm("POP.D W12");
    asm("POP.D W10");
    asm("POP.D W8");
    asm("POP.D W6");
    asm("POP.D W4");
    asm("POP.D W2");
    asm("POP W1");
    asm("POP TBLPAG");
    asm("POP PSVPAG");
    asm("POP RCOUNT");
    asm("POP SR");
    asm("POP CORCON");
}

unsigned int round_robin(){
    return(task_running + 1) % READY_QUEUE_SIZE;
}

void tarefa_1(){
    while(1)
    {
        LATCbits.LATC14 = ~PORTCbits.RC14;
    }
}

void tarefa_2(){
    while(1)
    {
        LATEbits.LATE0 = ~PORTEbits.RE0;
    }
}

void tarefa_3(){
    while(1)
    {
        LATEbits.LATE1 = ~PORTEbits.RE1;
    }
}

// CONFIGURAÇÃO
void timer_config(){
    IEC0bits.T1IE = 1; // HABILITA A INTERRUPÇÃO DO TIMER 1
    IPC0bits.T1IP = 0b100; // NÍVEL DE TIMER 4 
    IFS0bits.T1IF = 0; // LIMPA A FLAG DE INTERRUPÇÃO
    SRbits.IPL = 0b100; // NÍVEL DE PRIORIDADE 4 PARA CPU
    T1CONbits.TCS = 0; // REFERENCIA DO CLOCK MUDANÇA DE INSTRUÇÃO
    T1CONbits.TCKPS = 0b10; // PRESCALER 1:64
    T1CONbits.TON = 1; // LIGA O TIMER 1
    PR1 = 100;
}