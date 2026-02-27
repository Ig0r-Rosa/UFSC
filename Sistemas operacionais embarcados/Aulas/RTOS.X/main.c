#include "kernel.h"
#include "userApp.h"

int main()
{
    OsInit();
    
    CreateTask(1,3, Tarefa1);
 
    OsStart();

    while(1){};
    return 0;
}
