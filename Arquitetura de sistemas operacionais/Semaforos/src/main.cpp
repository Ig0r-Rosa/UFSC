#include <iostream>
#include <unistd.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <semaphore.h>
#include <cstdlib> 
#include <ctime> 
#include <sys/wait.h>

// Variaveis globais

// Função main
int main()
{    
    int numProcessos = 1;
    srand(time(NULL));
    std::cout << "Escolha o número de threads: ";
    std::cin >> numProcessos;
    std::cout << std::endl;

    if(numProcessos < 1)
    {
        std::cout << "O número não pode ser menor que 1 escolha novamente!" << std::endl;        
        return main();
    }   

    int *id = static_cast<int *>(mmap(NULL, sizeof(int), PROT_READ 
    | PROT_WRITE, MAP_SHARED | MAP_ANONYMOUS, -1, 0));
    
    *id = 0;

    sem_t *sem = sem_open("/semaforo_exclusao_mutua", O_CREAT, 01, 1);

    // Criação de threads
    for (int i = 0; i < numProcessos; ++i) 
    {
        pid_t pid = fork();

        if(pid < 0){return 1;}
        else if(pid == 0)
        {
            // Execução do processo filho
            srand(time(NULL) ^ getpid());
            int tempo = rand() % 10 + 1;
            sleep(tempo);
            sem_wait(sem);
            (*id)++;
            std::cout << "Processo " << *id << " criado (PID: " 
            << getpid() << ") após " << tempo << " segundos." << std::endl;
            sem_post(sem);
            exit(0); // Para o processo filho
        }
    }

    // Processo pai espera os processos filhos
    for (int i = 0; i < numProcessos; ++i) {
        wait(NULL);
    }

    // limpa memoria
    sem_close(sem);
    sem_unlink("/semaforo_exclusao_mutua");
    munmap(id, sizeof(int));

    return 0;
}