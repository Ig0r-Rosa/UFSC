#include "kernel.h"
#include "scheduler.h"
#include "userApp.h"

readyQueueT rQueue;

void CreateTask(int8 id, int8 priority, fPtr task)
{
    tcbT newTask;

    newTask.taskId = id;
    newTask.taskPriority = priority;
    newTask.taskF = task;

    newTask.taskSp = 0;
    newTask.timeSleeping = 0;
    newTask.taskState = READY;

    newTask.BSRREG = 0x000;
    newTask.WREG = 0x000;
    newTask.STATUSREG = 0x000;
    newTask.FSRREG = 0x000;

    rQueue.readyQueue[rQueue.readyQueueSize++] = newTask;
};

void Delay(int8 time)
{
    SAVECONTEXT(waiting);
    rQueue.readyQueue[rQueue.taskRunning].timeSleeping = time;
    Scheduler();
    RESTORECONTEXT();
};

void Yield()
{
    SAVECONTEXT(READY);
    Scheduler();
    RESTORECONTEXT();
};

TASK Idle()
{
    while(1)
    {
        Nop();
    }
};

void OsInit()
{
    rQueue.readyQueueSize = 0;
    rQueue.taskRunning = 0;
};

void OsStart()
{
    UserConfig();
    
};

