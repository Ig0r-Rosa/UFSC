#include "scheduler.h"
#include "config.h"
#include "types.h"

extern readyQueueT rQueue;

void Scheduler()
{
    #if DEFAULT_SCHEDULER == RR_SCHEDULER
        //
    #elif DEFAULT_SCHEDULER == PRIORITY_SCHEDULER
        //
    #endif
};

void RrScheduler()
{
    rQueue.taskRunning = (rQueue.taskRunning + 1) % rQueue.readyQueueSize;
};

void PriorityScheduler()
{
    
};