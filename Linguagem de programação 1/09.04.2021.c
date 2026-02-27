/*
Nome: Igor de Matos da Rosa
Matrícula: 20103930
questão realizada: 2, lista 4.
*/

#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int Impar(int v[]);
int Sump(int v[]);
int i; // utilizei o i como variavel global para deixar o código menor
int main(){
    setlocale(LC_ALL,"Portuguese");
    int v[10];
    int impar = 0, positivos = 0;

    for(i=0; i < 10; i++){
        printf("\nDigite o número de v[%i] : ", i);
        scanf("%i", &v[i]);
        impar = Impar(v) + impar;
        positivos = Sump(v) + positivos;
    }

    printf("\nNo vetor V, estitem (%i) números impares\n", impar);
    printf("\nA soma dos números positivos de V é : %i \n", positivos);
    return 0;
}

int Impar(int v[]){
    int k = 0, par;
    par = v[i] % 2;
    if(par != 0){
        k++;
        }
    return k;
}

int Sump(int v[]){
    int k = 0;
    if(v[i] >= 0){
        k = v[i];
    }
    return k;
}