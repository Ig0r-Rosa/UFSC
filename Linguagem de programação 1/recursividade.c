/*
*/

#include <stdio.h>
#include <locale.h>
#include "recursividade.h"


int main(){
    setlocale(LC_ALL,"Portuguese");
    int i;
    int N = 10;
    int v[N];

    for(i = 0; i < N; i++){
        v[i]= factorial(i);
    }
    for(i = 0; i < 10; i++){
        printf("\n %i! = %i ", i, v[i]);
    }

    return 0;
}