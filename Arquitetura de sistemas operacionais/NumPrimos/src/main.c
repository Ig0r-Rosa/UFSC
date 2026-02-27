#include "funcThread.h"

int main() {

  long x;
  scanf("%ld",&x);

  int meio = x / 2;

  ArgThreads argthread[numThreads];
  argthread[0].ID = 1;
  argthread[0].De = 2;
  argthread[0].Ate = meio;
  argthread[0].X = x;
  pthread_create(&threads[0], NULL, operacaoThreads, (void*) &argthread[0]);

  argthread[1].ID = 0;
  argthread[1].De = meio + 1;
  argthread[1].Ate = x -1;
  argthread[1].X = x;
  pthread_create(&threads[1], NULL, operacaoThreads, (void*) &argthread[1]);
  

  // Espera as threads acabarem a operação
  for(int i = 0; i < numThreads; i++)
  {
    pthread_join(threads[i], NULL);
  }

  if(ehPrimo == 1)
  {
    printf("O numero %ld eh primo", x);
  }
  else
  {
    printf("O numero %ld nao eh primo", x);
  }

  return 0;
}
