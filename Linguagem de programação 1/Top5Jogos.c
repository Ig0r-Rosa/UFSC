//Arquivo = Top5Jogos.c
//Titulo = Top 5 Jogos
//Feito por = Igor(20103930) e Dimitri(20205560).
//Data = 29/04/2021
//Objetivo = O objetivo do programa é inicialmente perguntar ao usuário, se ele deseja alterar os jogos armazenados, gravando novos jogos, ou ler os jogos 
//que ja estão armazenados no arquivo "Top5Jogos.txt", caso ele queira gravar novos jogos no arquivo, irá pedir o nome, estilo e ano de 5 jogos, caso
//ele deseje ler, irá apresentar os 5 jogos ja armazenados no arquivo.
//Metodo geral =
//1- escolha do usuário entre ler ou gravar dados
//2.1- caso queira gravar dados e abra o arquivo com sucesso, irá pedir os dados de 5 jogos
//    3- irá imprimir os dados no arquivo "Top5Jogos.txt".
//2.2- caso queira ler os dados e abra o arquivo com sucesso, irá ler os dados ja escritos
//Funções = 
// -modificar = irá gravar os dados no arquivo "Top5Jogos.txt"
// -lerL = irá ler os dados do arquivo "Top5Jogos.txt"
//Arquivos incluidos = stdio.h, locale.h, stdlib.h, string.h.
//Arquivos de dados =  "Top5Jogos"


#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>

struct Jogos
{
    int anoJ;
    char title[50];
    char estilo[50];
};


void modificar();
void lerL();
int main(){
    setlocale(LC_ALL,"Portuguese");
    int escolha;
    
    printf("\nDigite '1' para alterar os jogos escolhidos\nDigite '0' para ler os jogos escolhidos\n");
    printf("Escolha:  ");
    scanf("%i", &escolha);
    if(escolha == 1){
        modificar();
    }
    else if (escolha == 0){
        lerL();
    }
    else{
        printf("\nDigitação inválida!\n");
    }
}

void modificar(){
    FILE *filePtr;
    const int lib_size = 5;
    struct Jogos Lib[lib_size];
    int i;

    filePtr = fopen("Top5Jogos.txt", "w");
    
    if(filePtr == NULL)
    {
        printf("\n Erro! Não foi possível criar arquivo! \n");
        return 1;
    }

    fprintf(filePtr, "\n______Jogos______\n");
    for(i=1;i<=lib_size; i++){
        printf("\n\nEntrada de dados para Jogo %i: \n", i);
        
        printf("\nTitulo do Jogo: ");
        scanf("%s", Lib[i].title);

        printf("\nEstilo do Jogo: ");
        scanf("%s", Lib[i].estilo);

        printf("\nAno do Jogo: ");
        scanf("%i", &Lib[i].anoJ);

        fprintf(filePtr, "\n\nAno do Jogo = %d\nNome do jogo = %s\nEstilo do jogo = %s\n\n", Lib[i].anoJ, Lib[i].title, Lib[i].estilo);
    }  

    printf("\n");
    printf("\nO programa gravou os jogos para o arquivo Top5Jogos.txt\n");
    fclose(filePtr);

    return 0;
}

void lerL(){
    FILE *filePtr;
    int id;
    char leitura[100];
    int i=2;
    
    filePtr = fopen("Top5Jogos.txt", "r");

    if(filePtr == NULL){
        printf("\n Erro! Não foi possível criar arquivo! \n");
        return 1;
    }

    printf("\nPrograma fez a leitura do arquivo\n");

    while(fscanf(filePtr, "%i", &id)!= EOF){
        fscanf(filePtr, "%i", &id);
        fgets(leitura, 100, filePtr);
        printf("%s", leitura);
        i++;
        if(i==3){
            printf("\n\n");
            i=0;
        }
    }
    fclose(filePtr);
    return 0;
}