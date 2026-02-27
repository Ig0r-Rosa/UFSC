// Inludes
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// Variaveis globais
const int numThreads = 2;
pthread_mutex_t mutexGlobal;
pthread_t threads[numThreads];

int ehPrimo = 1;

typedef struct
{
    int ID;
    int De;
    int Ate;
    int X;

} ArgThreads;


// Função de execução dos threads
void* operacaoThreads(void* argThread)
{
    ArgThreads* arg = (ArgThreads*) argThread;
    int i = (int)arg->De;
    int idoutra = (int)arg->ID;
    int X = (int)arg->X;
    int ate = (int)arg->Ate;

    while (i <= ate) {
        pthread_mutex_lock(&mutexGlobal);

        // Verifica se o número é divisível por i
        if (arg->X % i == 0) {
            ehPrimo = 0;
            pthread_cancel(threads[idoutra]);
            pthread_mutex_unlock(&mutexGlobal);  // Destrava o mutex
            break;
        }

        pthread_mutex_unlock(&mutexGlobal);  // Destrava o mutex fora da seção crítica
        i++;
    }

    arg = NULL;
    return NULL;
}

