#ifndef fs_h
#define fs_h
#include <string>
#include <cstddef>
#include <fstream>
#include <iostream>
#include <cstring>

// Struct 
struct Nodo
{
    // int de 8 bits para representar o byte
    uint8_t existe[4];
    uint8_t caracteres[20];
    uint8_t prox[4];
};

/**
 * @param arquivoDaLista nome do arquivo em disco que contem a lista encadeada
 * @param novoNome nome a ser adicionado apos depoisDesteNome
 * @param depoisDesteNome um nome presente na lista
 */
void adiciona(std::string arquivoDaLista, std::string novoNome, std::string depoisDesteNome)
{
    // Variáveis
    Nodo nodo;
    Nodo novoNodo;
    int posicaoLivre = -1;
    int posicaoNodoAtual = -1;
    int proximoNodo = -1;

    // Leitura do arquivo, com as tags de binario, input e output
    std::fstream arquivo(arquivoDaLista, std::ios::binary | std::ios::in | std::ios::out);
    if (!arquivo) {
        std::cerr << "Erro ao abrir o arquivo!" << std::endl;
        return;
    }

    // Procurar bloco livre no arquivo
    arquivo.seekg(4); // Pular os primeiros 4 bytes

    // Lê os 10 nodos possiveis
    for (int i = 0; i < 10; ++i) {
        arquivo.read(reinterpret_cast<char*>(&nodo), sizeof(Nodo));
        /*
            A linha acima, o reinterpret_cast transforma de um ponteiro para char*, para encaixar
            no nodo*.
            sizeof calcula o tamanho da estrutura.
            O read então encaixa char* na variavel nodo.
        */
        
        // Encontrou bloco livre
        if (nodo.existe[0] == 0) {
            posicaoLivre = 4 + i * sizeof(Nodo);
            break;
        }
    }

    // Se caso não encontrou o bloco livre
    if (posicaoLivre == -1) {
        arquivo.close();
        return;
    }

    // Localizar o nodo depoisDesteNome
    arquivo.clear(); // Reseta o arquivo
    arquivo.seekg(4); // Voltar ao início dos nodos

    for (int i = 0; i < 10; ++i) {
        arquivo.read(reinterpret_cast<char*>(&nodo), sizeof(Nodo));
        
        // Achou o nodo "depoisDesteNome"
        if (strncmp(reinterpret_cast<char*>(nodo.caracteres), depoisDesteNome.c_str(), depoisDesteNome.size()) == 0) {
            posicaoNodoAtual = 4 + i * sizeof(Nodo); // Encontrou o nodo
            proximoNodo = *reinterpret_cast<int*>(nodo.prox); // Captura o próximo nodo
            break;
        }
    }
    
    // Não encontrou o nodo "depoisDesteNome"
    if (posicaoNodoAtual == -1) {
        arquivo.close();
        return;
    }

    // Adicionar novo nodo
    memset(&novoNodo, 0, sizeof(Nodo));
    novoNodo.existe[0] = 1; // Agora o bloco vazio é preenchido
    // Copia o novoNome para novoNodo
    strncpy(reinterpret_cast<char*>(novoNodo.caracteres), novoNome.c_str(), sizeof(novoNodo.caracteres) - 1);
    // Definir o próximo nodo como o que estava antes do novo
    memcpy(novoNodo.prox, &proximoNodo, sizeof(novoNodo.prox));

    // Pega as variaveis da memoria e por fim grava no arquivo
    arquivo.seekp(posicaoLivre);
    arquivo.write(reinterpret_cast<const char*>(&novoNodo), sizeof(Nodo));

    // Atualizar lista
    arquivo.seekp(posicaoNodoAtual);
    arquivo.read(reinterpret_cast<char*>(&nodo), sizeof(Nodo));
    // Atualiza o próximo nodo do nodo existente para apontar para o novo nodo
    memcpy(nodo.prox, &posicaoLivre, sizeof(nodo.prox));
    arquivo.seekp(posicaoNodoAtual);
    arquivo.write(reinterpret_cast<const char*>(&nodo), sizeof(Nodo));

    arquivo.close(); // Fecha o arquivo
}

#endif /* fs_h */