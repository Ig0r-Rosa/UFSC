/*
Aluno:Igor de Matos da Rosa
Matrícula:20103930

Atividade realizada:
Exemplo 4 (exercício):
● Faça um programa que receba um número inteiro e verifique se
esse número é positivo ou negativo. 

*/

#include <stdio.h>

int main(){
    
    int n1;

    printf("Escolha um n%cmero: \n", 163);
    scanf("%i", &n1);
    
        if(n1 > 0)
            printf("\n=-=-=-=-=-=-=-=-=-=-=-\nEste n%cmero %c positivo\n=-=-=-=-=-=-=-=-=-=-=-\n", 163, 130);
        else
            printf("\n=-=-=-=-=-=-=-=-=-=-=-\nEste n%cmero %c negativo\n=-=-=-=-=-=-=-=-=-=-=-\n", 163, 130);
    
    /*
    Eu havia feito outro metodo para evitar com que o 0 seja considerado negativo, porém fugiria da proposta da aula
    Acho interessante se houver algum tempo após a proxima aula mostrar.
    */
    
    return 0;
}
