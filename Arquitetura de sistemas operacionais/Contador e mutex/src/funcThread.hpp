// Inludes
#include <iostream>
#include <pthread.h>
#include <mutex>


// Variaveis globais
int numThreads = 128;
int execPorThread = 1000;
int contadorGlobal = 0;
std::mutex mutexGlobal;

// Função de execução dos threads
void* operacaoThreads(void* ID)
{
    for(int i = 0; i < execPorThread; i++)
    {
        std::lock_guard<std::mutex> LGuard(mutexGlobal);
        contadorGlobal++;
    }
    
    std::lock_guard<std::mutex> LGuard(mutexGlobal);
    std::cout << "Thread[" << *static_cast<int*>(ID) << "] finalizou sua contagem -> valor da contagem: " << contadorGlobal << std::endl;
    return NULL;
}

