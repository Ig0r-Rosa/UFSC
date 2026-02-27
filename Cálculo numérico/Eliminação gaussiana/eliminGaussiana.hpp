#ifndef ELIMINGAUSSIANA_HPP
#define ELIMINGAUSSIANA_HPP

#include <math.h>  
#include <iostream>
#include <vector>

class EliminGaussiana
{
    private:

    public:
    EliminGaussiana(){};
    ~EliminGaussiana(){};

    static void printarMatriz(std::vector<std::vector<float>> &M)
    {
        // Verifica se a matriz está vazia
        if (M.empty() || M[0].empty()) {
            std::cout << "Matriz vazia ou com linhas vazias." << std::endl;
            return;
        }
        int linhas  = M.size();
        int colunas = M[0].size();
        std::cout << " Matriz:" << std::endl;
        for(int i = 0; i < linhas; i++)
        {
            std::cout << "    ";
            for(int j = 0; j < colunas; j++)
            {
                if(M[i].at(j) >= 0)
                {
                    std::cout << " " << M[i][j] << " ";
                }
                else
                {
                    std::cout << M[i][j] << " ";
                }
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    };

    static void Calcular(std::vector<std::vector<float>> &M)
    {
        if (M.empty() || M[0].empty()) {
            std::cout << "Matriz vazia ou com linhas vazias." << std::endl;
            return;
        }

        int linhas = M.size();
        int colunas = M[0].size();
        
        for (int pivoAtual = 0; pivoAtual < std::min(linhas, colunas); pivoAtual++)
        {
            // Troca de linha se o pivo for zero
            if (M[pivoAtual][pivoAtual] == 0) {
                for (int k = pivoAtual + 1; k < linhas; k++)
                {
                    if (M[k][pivoAtual] != 0) {
                        std::swap(M[pivoAtual], M[k]);
                        break;
                    }
                }
            }

            // Se o pivô ainda for zero, continue para a próxima coluna
            if (M[pivoAtual][pivoAtual] == 0) continue;

            // Realiza a eliminação
            for (int i = pivoAtual + 1; i < linhas; i++)
            {
                float a = M[i][pivoAtual] / M[pivoAtual][pivoAtual];
                for (int j = pivoAtual; j < colunas; j++)
                {
                    M[i][j] -= a * M[pivoAtual][j];
                }
            }

            // Exibe o resultado da matriz
            std::cout << "Ite. " << pivoAtual + 1 << std::endl;
            printarMatriz(M);
        }
    };

};

#endif