/*
Nome:Igor de matos da rosa
Matrícula:20103930
*/
#include <stdio.h>

int main(){
    const int linha = 3, coluna = 3;
    int i, j, parA, parA1, parB, parB1;
    int a[linha][coluna];
    int b[linha][coluna];
    parA = 0;
    parB = 0;
    parA1 = 0;
    parB1 = 0;

    for(i = 0; i < linha; i++)
        {
            for(j=0; j < coluna; j++){
                printf("\nDigite o valor a[%i][%i] : ", i, j);
                scanf("%i", &a[i][j]);
                parA = a[i][j] % 2;
                if(parA == 0){
                    parA1++;
                }
            }
        }
    printf("\n\n");

    for(i = 0; i < linha; i++)
        {
            for(j=0; j < coluna; j++){
                printf("\nDigite o valor b[%i][%i] : ", i, j);
                scanf("%i", &b[i][j]);
                parB = b[i][j] % 2;
                if(parB == 0){
                    parB1++;
                }
            }
        }
    printf("\n\n");

    if(parA1 > parB1){
        printf("\nA matriz(a) possui %i pares e a matriz(b) possui %i pares\nlogo (a) possui mais pares que (b)\n", parA1, parB1);
    }
    else if(parB1 > parA1){
        printf("\nA matriz(a) possui %i pares e a matriz(b) possui %i pares\nlogo (b) possui mais pares que (a)\n", parA1, parB1);
    }
    else{
        printf("\nA matriz(a) possui %i pares e a matriz(b) possui %i pares\nAs duas matrizes possuem a mesma quantidade de pares\n", parA1, parB1);
    }
    return 0;
}