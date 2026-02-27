/*
Nome:Igor de matos da rosa
Matrícula:20103930
*/
#include <stdio.h>

int main(){
    const int vetor = 15;
    int i, k;
    int v[vetor];

    
    for(i = 0; i < vetor; i++)
        {
            printf("\nDigite o valor [%i] : ", i);
            scanf("%i", &v[i]);  
        }
    printf("\nEscolha o valor(k): ");
    scanf("%i", &k);
    printf("\n\n");
    for(i = 0; i < vetor; i++)
        {
            if(v[i] == k){
                v[i] = v[i] * 10;
            }
        }
    for(i = 0; i < vetor; i++)
        {
            printf("   %i   \n", v[i]); 
        }
    printf("\n\n");
    return 0;
}