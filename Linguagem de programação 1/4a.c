/*
Nome:Igor de matos da rosa
Matrícula:20103930
*/

#include <stdio.h>

int main(){
    const int vetor = 15;
    int i, par, soma;
    int v[vetor];
    soma = 0;
    
    for(i = 0; i < vetor; i++)
        {
            printf("\nDigite o valor [%i] : ", i);
            scanf("%i", &v[i]);  
        }
        printf("\n\n");
    for(i = 0; i < vetor; i++)
        {
            par = v[i] % 2;
            if(par == 0){
                soma = soma + v[i];
            }
            printf("   %i   \n", v[i]); 
        }
        printf("\n\n");
    printf("Soma de todos os pares = %i\n", soma);

    return 0;
}