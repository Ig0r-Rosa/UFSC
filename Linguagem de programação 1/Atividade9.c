/*
Nome:Igor de Matos da Rosa 
Matrícula:20103930
Questão realizada: 13
*/

#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

void imprimirA(int *v, int m, int n);
void imprimirB(int *v, int m, int n);
int main(){
    setlocale(LC_ALL,"Portuguese");
    int i, j, n, m;
    int *mptrA;

    printf("\n Quantidade de linhas : ");
    scanf("%i", &n);

    printf("\n Quantidade de colunas : ");
    scanf("%i", &m);

    mptrA = (int*) malloc(n*m*sizeof(int));

    printf("\nEntrada de dados: \n");
    for(i=0; i< n;i++){
        for(j= 0; j< m; j++){
            printf("matriz [%i][%i] = ",i, j);
            scanf("%i", (mptrA + i*m +j));
        }
    }
    
    imprimirA(mptrA, m, n);
    imprimirB(mptrA, m, n);

    return 0;
}

void imprimirA(int *v, int m, int n){
    int i, j;
    printf("\nMatriz A: \n");
    for(i=0; i< n;i++){
        for(j= 0; j< m; j++){
            printf("  %i  ", *(v + i*m +j));
        }
        printf("\n");
    }
}

void imprimirB(int *v, int m, int n){
    int i, j;
    printf("\nMatriz B: \n");
    for(j=0; j< m;j++){
        for(i= 0; i< n; i++){
            printf("  %i  ", *(v + i*m +j));
        }
        printf("\n");
    }
}