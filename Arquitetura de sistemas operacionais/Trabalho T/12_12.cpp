/**
 * Implemente aqui as funções dos sistema de arquivos que simula EXT3
 */


// includes
#include "fs.h" 
#include <iostream>
#include <cmath>
#include <fstream>
#include <cstring>
#include <sstream>
#include <vector>

void initFs(std::string fsFileName, int blockSize, int numBlocks, int numInodes)
{
    std::fstream file{fsFileName, std::ios::out | std::ios::trunc | std::ios::binary};
    if(!file.is_open()){
        std::cout << "erro ao abrir!" << std::endl;
        return;
    }

    const char zero{0x00};
    int tamMapaDeBits = std::ceil((numBlocks) / 8.0);
    char mapaBits[tamMapaDeBits]{};
    mapaBits[0] = 0x01;
    int tamVetorInodes = (sizeof(INODE) * (numInodes -1)); // Desconta o Inode do diretorio
    int tamBlocos = (blockSize * numBlocks);
    // Define o primeiro bit do mapa de bits

    // INODE do diretorio
    INODE slash{};
    slash.IS_DIR = 0x01;
    slash.IS_USED = 0x01;
    slash.NAME[0] = '/';

    // Tamanho dos blocos
    file.write((const char*)&blockSize, 1);
    // Número de blocos
    file.write((const char*)&numBlocks, 1);
    // Número de Inodes
    file.write((const char*)&numInodes, 1);
    // Mapa de bits
    file.write((const char*) mapaBits, tamMapaDeBits);
    // Inode diretorio
    file.write((const char*)&slash, sizeof(INODE));
    // Vetor de Inode
    file.write(std::string(sizeof(INODE) * (numInodes - 1), zero).data(), sizeof(INODE) * (numInodes - 1));
    // Indice do diretorio raiz
    file.write((const char*)&zero, 1);
    // Vetor de blocos
    file.write(std::string(blockSize * numBlocks, zero).data(), blockSize * numBlocks);

    file.close();
}

// Função para verificar bits livres em um mapa de bits
int encontrarPrimeiroBitLivre(char* mapaDeBits, int tamMapaDeBits, std::fstream &file) {
    for (int i = 0; i < tamMapaDeBits; ++i) {
        for (int bitPos = 0; bitPos < 8; ++bitPos) {
            if (!(mapaDeBits[i] & (1 << bitPos))) {
                mapaDeBits[i] |= (1 << bitPos);
                file.seekg(3);
                file.write(mapaDeBits, tamMapaDeBits);
                return i * 8 + bitPos;
            }
        }
    }
    return -1;
}

void zeraOBitDeIndice(char* mapaDeBits, int tamMapaDeBits, std::fstream &file, int indiceParaZerar)
{
    int bitDoByte = indiceParaZerar % 8;
    int ByteQueContemOBit = indiceParaZerar / 8;
    mapaDeBits[ByteQueContemOBit] &= ~(1 << bitDoByte);

    file.seekg(3);
    file.write(mapaDeBits, tamMapaDeBits);
}

// Função para encontrar o diretorio pai
std::string encontarDirPai(const std::string& path) {
    std::vector<std::string> segments;
    std::stringstream ss(path);
    std::string segment;
    while (std::getline(ss, segment, '/')) {
        if (!segment.empty()) {
            segments.push_back(segment);
        }
    }
    // Divida o caminho em segmentos
    if (segments.size() < 2) {
        return "/"; // Não há pai, o pai é o dir raiz
    }
    return segments[segments.size() - 2];
}

// Função para separar o ultimo diretorio/arquivo
std::string separaFilho(const std::string& path) {
    std::size_t pos = path.find_last_of('/');
    if (pos != std::string::npos) {
        return path.substr(pos + 1);
    }
    return path;
}

// Função que retorna o primeiro byte da string e o remove
unsigned char pegaOByteERemove(std::string& str) {
    if (str.empty()) {
        throw std::runtime_error("A string está vazia");
    }

    unsigned char byte = static_cast<unsigned char>(str[0]);
    str.erase(0, 1);

    return byte;
}

void addFile(std::string fsFileName, std::string filePath, std::string fileContent)
{
    std::fstream file{fsFileName, std::ios::in | std::ios::out | std::ios::binary};
    if(!file.is_open()){
        std::cout << "erro ao abrir!" << std::endl;
        return;
    }

    // Leitura dos 3 primeiros bytes
    int T, N, I;
    char bytes[3];
    file.read(bytes, sizeof(bytes));
    T = static_cast<unsigned char>(bytes[0]);
    N = static_cast<unsigned char>(bytes[1]);
    I = static_cast<unsigned char>(bytes[2]);

    // Ler mapa de Bits
    int tamMapaDeBits = std::ceil((N) / 8.0);
    char mapaDeBits[tamMapaDeBits]{};
    file.seekg(3);
    file.read(mapaDeBits, tamMapaDeBits);

    // Variaveis
    std::string novoArq = separaFilho(filePath);
    int inodeLivre = 0;
    std::string inodePaiNome;
    int indiceInodePai;
    int indiceNovoBlocoDir;
    int primeiroInode = 3 + tamMapaDeBits;
    
    // Nome do diretorio pai
    inodePaiNome = encontarDirPai(filePath);
    
    // Prepara o novo Inode
    INODE novoInode{};
    novoInode.IS_USED = 0x01;
    novoInode.IS_DIR = 0x00;
    // Formata a string para char[10]
    strncpy(novoInode.NAME, novoArq.c_str(), sizeof(novoInode.NAME) - 1);
    novoInode.NAME[sizeof(novoInode.NAME) - 1] = '\0';
    novoInode.SIZE = static_cast<unsigned char>(fileContent.size());

    int numBlocos = std::ceil(static_cast<double>(novoInode.SIZE) / T);

    // Achar INODE pai para reservar o caminho
    for(int i = 0; i < I; i++)
    {
        INODE dadosInode;

        // Começa a ler os Inodes
        file.seekg(primeiroInode + (sizeof(INODE) * i));
        file.read(reinterpret_cast<char*>(&dadosInode), sizeof(INODE));

        std::string nomeString(dadosInode.NAME);
        if(nomeString == inodePaiNome)
        {
            indiceInodePai = i;
        }

        if(dadosInode.IS_USED == 0x00 && inodeLivre == 0)
        {
            inodeLivre = i;
        }
    }

    // Atualiza o Inode pai com seu novo filho
    INODE dadosInode{};
    file.seekg(primeiroInode + (sizeof(INODE) * indiceInodePai));
    file.read(reinterpret_cast<char*>(&dadosInode), sizeof(INODE));

    bool alocou = false;
    for(int i=0; i < sizeof(dadosInode.DIRECT_BLOCKS) ;i++)
    {
        char bloco[T];
        file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInode.DIRECT_BLOCKS[i])));
        file.read(reinterpret_cast<char*>(&bloco), T);
        
        for(int j = 0; j < T; j++)
        {
            if(static_cast<unsigned int>(bloco[j]) == 0)
            {
                bloco[j] = static_cast<unsigned char>(inodeLivre);

                file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInode.DIRECT_BLOCKS[i])));
                file.write((const char*)&bloco, T);

                alocou = true;
                break;
            }
        }
        if(alocou)
        {
            break;
        }
    }
    

    // Caso não tenha bloco aloca um para o diretorio
    if(!alocou)
    {
        indiceNovoBlocoDir = encontrarPrimeiroBitLivre(mapaDeBits, tamMapaDeBits, file);
        // Aponta o link para o novo bloco
        for(int i = 1; i < sizeof(dadosInode.DIRECT_BLOCKS) ;i++)
        {
            if(static_cast<unsigned int>(dadosInode.DIRECT_BLOCKS[i]) == 0)
            {
                dadosInode.DIRECT_BLOCKS[i] = static_cast<unsigned char>(indiceNovoBlocoDir);
                bytes[0] = static_cast<unsigned char>(inodeLivre);

                file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInode.DIRECT_BLOCKS[i])));
                file.write((const char*)&bytes, T);
                break;
            }
        }
    }

    // Atualiza o tamanho
    dadosInode.SIZE = static_cast<unsigned char>(static_cast<unsigned int>(dadosInode.SIZE) + 1);

    // Reescreve o inode pai
    file.seekg(primeiroInode + (sizeof(INODE) * indiceInodePai));
    file.write((const char*)&dadosInode, sizeof(INODE));
    
    // Escreve o indice e os blocos com conteudo
    if(numBlocos <= sizeof(novoInode.DIRECT_BLOCKS)) {
        std::string conteudo = fileContent;

        for (int i = 0; i < numBlocos; i++) {
            if (conteudo.empty()) {
                break;
            }
            int indice = encontrarPrimeiroBitLivre(mapaDeBits, tamMapaDeBits, file);
            novoInode.DIRECT_BLOCKS[i] = static_cast<unsigned char>(indice);
            char bloco[T]{};
            file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * indice));
            file.read(reinterpret_cast<char*>(&bloco), T);

            // Preenche o bloco de bytes com o conteúdo da string
            for (int j = 0; j < T; j++) {
                if (!conteudo.empty() && bloco[j] == 0) {
                    bloco[j] = pegaOByteERemove(conteudo);
                } 
                else 
                {
                    break;
                }
            }

            // Posiciona o ponteiro para o bloco correto e grava os dados
            file.seekp(primeiroInode + (sizeof(INODE) * I) + 1 + (T * indice));
            file.write((const char*)&bloco, T);
        }
    } 
    else 
    {
        std::cout << "Precisa de blocos indiretos!" << std::endl;
    }


    // Escreve por fim o novo inode
    file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * inodeLivre));
    file.write((const char*)&novoInode, sizeof(INODE));

    file.close();
}

void addDir(std::string fsFileName, std::string dirPath)
{
    std::fstream file{fsFileName, std::ios::in | std::ios::out | std::ios::binary};
    if(!file.is_open()){
        std::cout << "erro ao abrir!" << std::endl;
        return;
    }

    // Leitura dos 3 primeiros bytes
    int T, N, I;
    char bytes[3];
    file.read(bytes, sizeof(bytes));
    T = static_cast<unsigned char>(bytes[0]);
    N = static_cast<unsigned char>(bytes[1]);
    I = static_cast<unsigned char>(bytes[2]);

    // Ler mapa de Bits
    int tamMapaDeBits = std::ceil((N) / 8.0);
    char mapaDeBits[tamMapaDeBits]{};
    file.seekg(3);
    file.read(mapaDeBits, tamMapaDeBits);

    // Variaveis
    std::string novoDir = separaFilho(dirPath);;
    int inodeLivre;
    std::string inodePai = encontarDirPai(dirPath);;
    int indiceInodePai;
    int indiceNovoBlocoDir = encontrarPrimeiroBitLivre(mapaDeBits, tamMapaDeBits, file);;
    int primeiroInode = 3 + tamMapaDeBits;

    // Prepara o novo Inode
    INODE novoInode{};
    novoInode.IS_USED = 0x01;
    novoInode.IS_DIR = 0x01;
    // Formata a string para char[10]
    strncpy(novoInode.NAME, novoDir.c_str(), sizeof(novoInode.NAME) - 1);
    novoInode.NAME[sizeof(novoInode.NAME) - 1] = '\0';
    
    // Aponta o link para o novo bloco
    for(int i=0; i < sizeof(novoInode.DIRECT_BLOCKS) ;i++)
    {
        if(static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[i]) == 0)
        {
            novoInode.DIRECT_BLOCKS[i] = static_cast<unsigned char>(indiceNovoBlocoDir);
            break;
        }
    }

    for(int i = 0; i < I; i++)
    {
        INODE dadosInode;

        // Começa a ler os Inodes
        file.seekg(primeiroInode + (sizeof(INODE) * i));
        file.read(reinterpret_cast<char*>(&dadosInode), sizeof(INODE));

        std::string nomeString(dadosInode.NAME);
        if(nomeString == inodePai)
        {
            indiceInodePai = i;
        }

        if(dadosInode.IS_USED == 0x00)
        {
            inodeLivre = i;

            // Aloca um bloco para o diretorio
            file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * inodeLivre));
            file.write((const char*)&novoInode, sizeof(INODE));
            
            break;
        }
    }

    // Atualiza o Inode pai com seu novo filho
    novoInode = INODE{};
    file.seekg(primeiroInode + (sizeof(INODE) * indiceInodePai));
    file.read(reinterpret_cast<char*>(&novoInode), sizeof(INODE));

    bool alocou = false;
    if(static_cast<unsigned int>(novoInode.SIZE) > 0)
    {
        for(int i=0; i < sizeof(novoInode.DIRECT_BLOCKS) ;i++)
        {
            char bloco[T]{};
            file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[i])));
            file.read(reinterpret_cast<char*>(&bloco), T);
            
            for(int j = 0; j < T; j++)
            {
                if(static_cast<unsigned int>(bloco[j]) == 0)
                {
                    bloco[j] = static_cast<unsigned char>(inodeLivre);

                    file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[i])));
                    file.write((const char*)&bloco, T);

                    alocou = true;
                    break;
                }
            }
            if(alocou)
            {
                break;
            }
        }
    }
    else
    {
        char bloco[T]{};
        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[0])));
        file.read(reinterpret_cast<char*>(&bloco), T);
        bloco[0] = inodeLivre;
        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[0])));
        file.write((const char*)&bloco, T);
        alocou = true;
    }

    // Caso não tenha bloco aloca um para o diretorio
    if(!alocou)
    {
        indiceNovoBlocoDir = encontrarPrimeiroBitLivre(mapaDeBits, tamMapaDeBits, file);
        char bloco[T]{};

        // Aponta o link para o novo bloco
        for(int i = 0; i < sizeof(novoInode.DIRECT_BLOCKS) ;i++)
        {
            if(static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[i]) == 0)
            {
                novoInode.DIRECT_BLOCKS[i] = static_cast<unsigned char>(indiceNovoBlocoDir);
                bloco[0] = static_cast<unsigned char>(inodeLivre);

                file.seekg(primeiroInode + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(novoInode.DIRECT_BLOCKS[i])));
                file.write((const char*)&bloco, T);
                break;
            }
        }
    }

    // Atualiza o tamanho
    novoInode.SIZE = static_cast<unsigned char>(static_cast<unsigned int>(novoInode.SIZE) + 1);

    // Reescreve o inode pai
    file.seekg(primeiroInode + (sizeof(INODE) * indiceInodePai));
    file.write((const char*)&novoInode, sizeof(INODE));

    file.close();
}

void remove(std::string fsFileName, std::string path)
{
    std::fstream file{fsFileName, std::ios::in | std::ios::out | std::ios::binary};
    if(!file.is_open()){
        std::cout << "erro ao abrir!" << std::endl;
        return;
    }

    // Leitura dos 3 primeiros bytes
    int T, N, I;
    char bytes[3];
    file.read(bytes, sizeof(bytes));
    T = static_cast<unsigned char>(bytes[0]);
    N = static_cast<unsigned char>(bytes[1]);
    I = static_cast<unsigned char>(bytes[2]);

    // Ler mapa de Bits
    int tamMapaDeBits = std::ceil((N) / 8.0);
    char mapaDeBits[tamMapaDeBits]{};
    file.seekg(3);
    file.read(mapaDeBits, tamMapaDeBits);

    // Variaveis
    std::string arqRem = separaFilho(path);
    int indiceInodeRem = 0;
    std::string inodePaiNome;
    int indiceInodePai;
    
    // Nome do diretorio pai
    inodePaiNome = encontarDirPai(path);
    
    INODE dadosInodeRem;
    INODE dadosInodePai;

    for(int i = 0; i < I; i++)
    {
        INODE dadosInode;

        // Começa a ler os Inodes
        file.seekg(3+ tamMapaDeBits + (sizeof(INODE) * i));
        file.read(reinterpret_cast<char*>(&dadosInode), sizeof(INODE));

        std::string dirPaiNome(dadosInode.NAME);
        if(dirPaiNome == inodePaiNome)
        {
            indiceInodePai = i;
            dadosInodePai = dadosInode;
        }

        std::string arqRemNome(dadosInode.NAME);
        if(arqRemNome == arqRem)
        {
            indiceInodeRem = i;
            dadosInodeRem = dadosInode;
        }
    }

    for(int i=0; i < sizeof(dadosInodeRem.DIRECT_BLOCKS) ;i++)
    {
        if(static_cast<unsigned int>(dadosInodeRem.DIRECT_BLOCKS[i]) != 0)
        {
            zeraOBitDeIndice(mapaDeBits, tamMapaDeBits, file, dadosInodeRem.DIRECT_BLOCKS[i]);
        }
    }

    // Diz que não esta sendo usado
    dadosInodeRem.IS_USED = 0x00;
    file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * indiceInodeRem));
    file.write((const char*)&dadosInodeRem.IS_USED, sizeof(dadosInodeRem.IS_USED));

    // Atualiza o pai, e bloco que continha o indice
    std::string blocos{};
    int posLeitura = 0;
    int indiceLimpar = -1;
    int numBlocosNecessarios = static_cast<unsigned int>(dadosInodePai.SIZE) / T;
    for(int i = 0; i < sizeof(dadosInodePai.DIRECT_BLOCKS); i++)
    {
        char bloco[T]{};
        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * dadosInodePai.DIRECT_BLOCKS[i]));
        file.read(reinterpret_cast<char*>(&bloco), T);

        for(int j = 0; j < T; j++)
        {
            posLeitura++;
            if(posLeitura <= static_cast<unsigned int>(dadosInodePai.SIZE))
            {
                blocos.push_back(bloco[j]);
                if(bloco[j] == indiceInodeRem)
                {
                    indiceLimpar = posLeitura;
                }
            }
        }
    }

    for (int i = indiceLimpar -1; i < blocos.size() -1; i++) {
        blocos.at(i) = blocos.at(i + 1);
    }

    for(int i = 0; i < numBlocosNecessarios; i++)
    {
        char bloco[T]{};
        for(int j = 0; j < T; j++)
        {
            if(!blocos.empty())
            {
                bloco[j] = static_cast<unsigned char>(blocos.at(0));
                blocos.erase(0, 1);
            }
            else
            {
                break;
            }
        }
        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * dadosInodePai.DIRECT_BLOCKS[i]));
        file.write((const char*)(&bloco), T);
    
    }
    
    dadosInodePai.SIZE = static_cast<unsigned char>(static_cast<unsigned int>(dadosInodePai.SIZE) - 1);
    
    // Limpa bloco caso não ocupe
    if(numBlocosNecessarios > 0)
    {
        for(int i = numBlocosNecessarios; i < sizeof(dadosInodePai.DIRECT_BLOCKS); i++)
        {
            if(dadosInodePai.DIRECT_BLOCKS[i] != 0)
            {
                zeraOBitDeIndice(mapaDeBits, tamMapaDeBits, file, dadosInodePai.DIRECT_BLOCKS[i]);
                dadosInodePai.DIRECT_BLOCKS[i] = 0;
            }
        }
    }

    file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * indiceInodePai));
    file.write((const char*)&dadosInodePai, sizeof(INODE));
    
    file.close();
}

void move(std::string fsFileName, std::string oldPath, std::string newPath)
{
    std::fstream file{fsFileName, std::ios::in | std::ios::out | std::ios::binary};
    if(!file.is_open()){
        std::cout << "erro ao abrir!" << std::endl;
        return;
    }

    // Leitura dos 3 primeiros bytes
    int T, N, I;
    char bytes[3];
    file.read(bytes, sizeof(bytes));
    T = static_cast<unsigned char>(bytes[0]);
    N = static_cast<unsigned char>(bytes[1]);
    I = static_cast<unsigned char>(bytes[2]);

    // Ler mapa de Bits
    int tamMapaDeBits = std::ceil((N) / 8.0);
    char mapaDeBits[tamMapaDeBits]{};
    file.seekg(3);
    file.read(mapaDeBits, tamMapaDeBits);

    // Variaveis
    std::string arqMov = separaFilho(oldPath);
    std::string arqMovNovoNome = separaFilho(newPath);
    int indiceInodeMov = 0;
    std::string inodePaiNome;
    int indiceInodePai;
    std::string inodeNovoPaiNome;
    int indiceInodeNovoPai;
    
    // Nome do diretorio pai
    inodePaiNome = encontarDirPai(oldPath);
    inodeNovoPaiNome = encontarDirPai(newPath);
    
    INODE dadosInodeMov;
    INODE dadosInodePai;
    INODE dadosInodeNovoPai;

    for(int i = 0; i < I; i++)
    {
        INODE dadosInode;

        // Começa a ler os Inodes
        file.seekg(3+ tamMapaDeBits + (sizeof(INODE) * i));
        file.read(reinterpret_cast<char*>(&dadosInode), sizeof(INODE));

        std::string dirPaiNome(dadosInode.NAME);
        if(dirPaiNome == inodePaiNome)
        {
            indiceInodePai = i;
            dadosInodePai = dadosInode;
        }

        std::string dirNovoPaiNome(dadosInode.NAME);
        if(dirNovoPaiNome == inodeNovoPaiNome)
        {
            indiceInodeNovoPai = i;
            dadosInodeNovoPai = dadosInode;
        }

        std::string arqMovNome(dadosInode.NAME);
        if(arqMovNome == arqMov)
        {
            indiceInodeMov = i;
            dadosInodeMov = dadosInode;
        }
    }

    // Renomeia arquivo caso mude
    if(arqMov != arqMovNovoNome)
    {
        arqMovNovoNome.copy(dadosInodeMov.NAME, sizeof(dadosInodeMov.NAME) - 1);
        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * indiceInodeMov) + 2);
        file.write((const char*)&dadosInodeMov.NAME, sizeof(dadosInodeMov.NAME));
    }

    // Atualiza o pai, e bloco que continha o indice
    if(inodePaiNome != inodeNovoPaiNome)
    {
        std::string blocos{};
        int posLeitura = 0;
        int indiceLimpar = -1;
        int numBlocosNecessarios = static_cast<unsigned int>(dadosInodePai.SIZE) / T;
        for(int i = 0; i < sizeof(dadosInodePai.DIRECT_BLOCKS); i++)
        {
            char bloco[T]{};
            file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * dadosInodePai.DIRECT_BLOCKS[i]));
            file.read(reinterpret_cast<char*>(&bloco), T);

            for(int j = 0; j < T; j++)
            {
                posLeitura++;
                if(posLeitura <= static_cast<unsigned int>(dadosInodePai.SIZE))
                {
                    blocos.push_back(bloco[j]);
                    if(bloco[j] == indiceInodeMov)
                    {
                        indiceLimpar = posLeitura;
                    }
                }
            }
        }

        for (int i = indiceLimpar -1; i < blocos.size() -1; i++) {
            blocos.at(i) = blocos.at(i + 1);
        }

        for(int i = 0; i < numBlocosNecessarios; i++)
        {
            char bloco[T]{};
            for(int j = 0; j < T; j++)
            {
                if(!blocos.empty())
                {
                    bloco[j] = static_cast<unsigned char>(blocos.at(0));
                    blocos.erase(0, 1);
                }
                else
                {
                    break;
                }
            }
            file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * dadosInodePai.DIRECT_BLOCKS[i]));
            file.write((const char*)(&bloco), T);
        
        }
        
        dadosInodePai.SIZE = static_cast<unsigned char>(static_cast<unsigned int>(dadosInodePai.SIZE) - 1);
        
        // Limpa bloco caso não ocupe
        if(numBlocosNecessarios > 0)
        {
            for(int i = numBlocosNecessarios; i < sizeof(dadosInodePai.DIRECT_BLOCKS); i++)
            {
                if(dadosInodePai.DIRECT_BLOCKS[i] != 0)
                {
                    zeraOBitDeIndice(mapaDeBits, tamMapaDeBits, file, dadosInodePai.DIRECT_BLOCKS[i]);
                    dadosInodePai.DIRECT_BLOCKS[i] = 0;
                }
            }
        }

        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * indiceInodePai));
        file.write((const char*)&dadosInodePai, sizeof(INODE));

        // Atualiza o novo pai
        bool alocou = false;
        if(static_cast<unsigned int>(dadosInodeNovoPai.SIZE) > 0)
        {
            char bloco[T]{};
            for(int i=0; i < sizeof(dadosInodeNovoPai.DIRECT_BLOCKS) ;i++)
            {
                file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInodeNovoPai.DIRECT_BLOCKS[i])));
                file.read(reinterpret_cast<char*>(&bloco), T);
                
                for(int j = 0; j < T; j++)
                {
                    if(static_cast<unsigned int>(bloco[j]) == 0)
                    {
                        bloco[j] = static_cast<unsigned char>(indiceInodeMov);

                        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInodeNovoPai.DIRECT_BLOCKS[i])));
                        file.write((const char*)&bloco, T);

                        alocou = true;
                        break;
                    }
                }
                if(alocou)
                {
                    break;
                }
            }
        }
        else
        {
            char bloco[T]{};
            file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInodeNovoPai.DIRECT_BLOCKS[0])));
            file.read(reinterpret_cast<char*>(&bloco), T);
            bloco[0] = indiceInodeMov;
            file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInodeNovoPai.DIRECT_BLOCKS[0])));
            file.write((const char*)&bloco, T);
            alocou = true;
        }

        // Caso não tenha bloco aloca um para o diretorio
        int indiceNovoBlocoDir;
        if(!alocou)
        {
            indiceNovoBlocoDir = encontrarPrimeiroBitLivre(mapaDeBits, tamMapaDeBits, file);
            char bloco[T]{};

            // Aponta o link para o novo bloco
            for(int i = 1; i < sizeof(dadosInodeNovoPai.DIRECT_BLOCKS) ;i++)
            {
                if(static_cast<unsigned int>(dadosInodeNovoPai.DIRECT_BLOCKS[i]) == 0)
                {
                    dadosInodeNovoPai.DIRECT_BLOCKS[i] = static_cast<unsigned char>(indiceNovoBlocoDir);
                    std::memset(bloco, 0, sizeof(bloco));
                    bloco[0] = static_cast<unsigned char>(indiceInodeMov);

                    file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * I) + 1 + (T * static_cast<unsigned int>(dadosInodeNovoPai.DIRECT_BLOCKS[i])));
                    file.write((const char*)&bloco, T);
                    break;
                }
            }
        }

        // Atualiza o tamanho
        dadosInodeNovoPai.SIZE = static_cast<unsigned char>(static_cast<unsigned int>(dadosInodeNovoPai.SIZE) + 1);

        // Reescreve o inode pai
        file.seekg(3 + tamMapaDeBits + (sizeof(INODE) * indiceInodeNovoPai));
        file.write((const char*)&dadosInodeNovoPai, sizeof(INODE));
    }

    file.close();
}