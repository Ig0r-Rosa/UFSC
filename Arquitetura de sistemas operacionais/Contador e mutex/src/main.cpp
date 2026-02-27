#include "funcThread.hpp"

int main() {
  int threadsAtuais =  0;
  pthread_t threads[numThreads];
  int threadsID[numThreads]{};

  for(int i = 0; i < numThreads; i++)
  {
    threadsID[i] = i;
    pthread_create(&threads[i], NULL, operacaoThreads, (void*) &threadsID[i]);
  }

  // Espera as threads acabarem a operação
  for(int i = 0; i < numThreads; i++)
  {
    pthread_join(threads[i], NULL);
  }

  std::cout << "Valor da contagem final: " << contadorGlobal << std::endl;

  return 0;
}
