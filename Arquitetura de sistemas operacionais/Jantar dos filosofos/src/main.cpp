#include <iostream>
#include <thread>
#include <mutex>
#include <semaphore.h>
#include <chrono>
#include <cstdlib>
#include <ctime>

#define NF 5        
#define PENSANDO 0   
#define FOME 1     
#define COMENDO 2  

// Variáveis globais
std::mutex mutex;
sem_t semaforos[NF];
int estado[NF];
char estados_char[NF] = {'P', 'P', 'P', 'P', 'P'};
std::thread filosofos[NF];

// Imprime os estados dos filosofos
void imprime()
{
    std::cout << estados_char << std::endl;
}

// Esquerda é (i + NF-1) % NF
int verEsq(int i)
{
    return (i + NF-1) % NF;
}
// Direita é (i + 1) % NF
int verDir(int i)
{
    return (i + 1) % NF;
}

// Testa se pode comer
void testaFilosofo(int i) 
{
    if (estado[i] == FOME && estado[verEsq(i)] != COMENDO && estado[verDir(i)] != COMENDO) 
    {
        // Se os vizinhos não estão comendo, o filósofo pode comer
        estado[i] = COMENDO;
        estados_char[i] = 'C';
        sem_post(&semaforos[i]);
    }
}

void Filosofo(int i)
{
    while (true) {
        // Tempo aleatório pensando
        std::this_thread::sleep_for(std::chrono::milliseconds(1000 + rand() % 1000));

        // Fica com fome
        std::unique_lock<std::mutex> lock(mutex);
        estado[i] = FOME;
        estados_char[i] = 'F';
        imprime();
        testaFilosofo(i);
        lock.unlock();

        sem_wait(&semaforos[i]);

        // Tempo aleatório comendo
        std::this_thread::sleep_for(std::chrono::milliseconds(1000 + rand() % 1000));

        // Depois de comer, volta a pensar
        lock.lock();
        estado[i] = PENSANDO;
        estados_char[i] = 'P';
        imprime();
        // Verifica se o filósofo à esquerda e da direita podem comer
        testaFilosofo(verEsq(i));
        testaFilosofo(verDir(i));
        lock.unlock();
    }
}

int main()
{
    srand(time(NULL));

    for (int i = 0; i < NF; i++) 
    {
        estado[i] = PENSANDO;
        sem_init(&semaforos[i], 0, 0);
    }

    for (int i = 0; i < NF; i++) 
    {
        filosofos[i] = std::thread(Filosofo, i);
    }

    for (int i = 0; i < NF; i++) 
    {
        filosofos[i].join();
    }
    
    return 0;
}