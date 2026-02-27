/*
Nome:Igor de matos da rosa
Matrícula:20103930
*/
#include <stdio.h>

int main(){
    const int linha = 3, coluna = 3;
    int i, j;
    int a[linha][coluna];
    int b[linha][coluna];
    int c[linha][coluna];

    
    for(i = 0; i < linha; i++)
        {
            for(j=0; j < coluna; j++){
                printf("\nDigite o valor a[%i][%i] : ", i, j);
                scanf("%i", &a[i][j]);
            }
        }
    printf("\n\n");

    for(i = 0; i < linha; i++)
        {
            for(j=0; j < coluna; j++){
                printf("\nDigite o valor b[%i][%i] : ", i, j);
                scanf("%i", &b[i][j]);
            }
        }
    printf("\n\n");

    printf("Matriz(c):\n");
    for(i = 0; i < linha; i++)
        {
            for(j=0; j < coluna; j++){
                if(a[i][j] >= b[i][j]){
                    c[i][j] = a[i][j];
                }
                else if(b[i][j] > a[i][j]){
                    c[i][j] = b[i][j];
                }
                printf("   %i   ", c[i][j]);


            }
        printf("\n");
        }
        
    return 0;
}