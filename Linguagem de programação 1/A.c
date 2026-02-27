/*
Nome:Igor de Matos da Rosa
Matrícula:20103930
Exercicio realizado: A.
Programa recebe as escolhas dos 10 eleitores e calcula os votos para 5 
candidatos.
• Modifique programa permitindo:
◦ receber a quantidade de votos a ser analisada
◦ receber os votos para 7 candidatos
◦ calcular a percentagem de votos de cada candidato e votos nulos
*/
#include <stdio.h>

int main(){

    const int aS = 7;//alteração livre de numero de candidatos
    int cand[aS];
    int i, v;
    int n = -1;
    int quantidade;//quantidade de votos
    float q;//correção do erro onde o float não apresenta casas após a virgula
    float porcentagem;// float responsavel pela exibição das porcentagens


    printf("Quantas pessoas ir%co votar\?: ", 132);
    scanf("%i", &quantidade);//número de votos

    printf("\nApura%c%co de votos: ", 135, 132);
    for(i = 0; i <= aS; i++)
        cand[i]=0;
        

    for(i = 0; i < quantidade; i++)// i irá até a quantidade escolhida pelo usuario.
    {
        printf("\nEscolha o candidato: 1...%i:  ", aS);// mudança na exibição de acordo com o número de candidatos
        scanf("%i", &v);
        if(v >= 0 && v <= aS)
            cand[v]++;
        else
            cand[0]++;
    }
    q = quantidade;//correção do erro onde o float não apresenta casas após a virgula
    printf("\nCandidato       Votos             porcentagem\n");
    for(i= 1; i <= aS; i++){
        porcentagem = (cand[i] * 100) / q;//conta de regra de 3 para porcentagem
        printf("%i                  %i                %.2f%%\n", i, cand[i], porcentagem);//exibição da porcentagem logo em seguida
        }
    porcentagem = (cand[0] * 100) / q;//conta de regra de 3 para porcentagem, votos nulos
    printf("\nVotos nulos: %i                %.2f%%\n", cand[0], porcentagem);

    return 0;
}