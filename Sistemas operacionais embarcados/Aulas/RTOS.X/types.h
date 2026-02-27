#ifndef TYPESH
#define	TYPESH

#include <xc.h>
#include <stddef.h>
#include <stdint.h>
#include "config.h"

typedef void TASK;
typedef void (*fPtr)(void);
typedef unsigned char byte;
typedef uint8_t int8;

typedef enum {READY =0, RUNNING, WAITING} stateT;

typedef struct tcb
{
    int8 taskId;
    int8 taskPriority;
    stateT taskState;
    fPtr taskF;
    byte WREG;
    byte STATUSREG;
    byte BSRREG;
    byte FSRREG;
    byte taskStack[MAXSTACKSIZE];
    int8 taskSp;
    int8 timeSleeping;
} tcbT;

typedef struct readyQueue 
{
    tcbT readyQueue[MAXUSERTASKS + 1];
    int8 taskRunning;
    int8 readyQueueSize;
} readyQueueT;

#define RRSCHEDULER 1
#define PRIORITYSCHEDULER 2

#endif

