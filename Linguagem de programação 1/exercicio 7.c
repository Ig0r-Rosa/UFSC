/*
Nome:Igor de Matos da Rosa
Matrícula:20103930

Atividade realizada: 7-Achar a soma dos números inteiros impares no intervalo de 0 a 100

*/

#include <stdio.h>

int main(){

    int r;//resto da divisao por 2, para indentificar se o numero é par ou impar
    int ni;//numero a ser processado e alterado
    int rf;//resultado final

    ni = 0;
    rf = 0;

    while(ni < 100){//caso o numero seja menor que 100 ele irá executar o comando
        ++ni;//adiciona antes de aplicar o valor 1
        printf("\n%i", ni);

        r = ni % 2;

        if(r == 0){//se o resto da divisao por 2 for 0 ele é par, caso contrario, é impar e somará o valor com o RF
            printf(" Par");
        }
        else
        {
            printf(" Impar");
            rf = ni + rf;
        }

    }
    printf("\nSoma dos impares = %i", rf);//exibição do resultado final

    return 0;
}