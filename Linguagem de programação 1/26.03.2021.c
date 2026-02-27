/*
Nome: Igor de Matos da Rosa
Matrícula:20103930
 Escreva uma função int fatorial (int N) que calcula N! (fatorial de N), sendo
que o valor inteiro (positivo) N é fornecido pelo usuário.
*/

#include <stdio.h>
//#include <math.h>
#include <locale.h>

int funcao(int num);


int main(){
    setlocale(LC_ALL,"Portuguese");

    int N;
    int res;

    printf("Digíte o número de N!: ");
    scanf("%i", &N);
    
    res = funcao(N);
    
    if(res > 0){
        printf("O número %i! = %i", N, res);
    }
    else if(res == 0){
        printf("O número %i! = 1", N);
    }
    else{
        printf("Este número é inválido");
    }

    return 0;
}

int funcao(int num)
{
    int n;
    int m;

    for(n=0;n < num; n++){
        if(n == 0){
            m = num;
        }
        else{
            m = m * n;
        }
    }
    
    return m;
}