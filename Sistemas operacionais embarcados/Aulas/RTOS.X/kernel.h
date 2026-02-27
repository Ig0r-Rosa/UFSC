#ifndef KERNELH
#define	KERNELH

#include "types.h"
void CreateTask(int8 id, int8 priority, fPtr task);
void Delay(int8 time);
void Yield();

TASK Idle();

void OsInit();
void OsStart();

#define SAVECONTEXT(state)

#define RESTORECONTEXT()

#endif

