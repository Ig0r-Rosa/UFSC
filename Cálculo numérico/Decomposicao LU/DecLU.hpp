#ifndef DECLU_HPP
#define DECLU_HPP

#include <math.h>  
#include <iostream>
#include <vector>
#include <iomanip>

class DecLU
{
    private:

    public:
    DecLU(){};
    ~DecLU(){};

    static void printarMatriz(std::vector<std::vector<float>> &M, std::string nomeMatriz = "")
    {
        // Verifica se a matriz está vazia
        if (M.empty() || M[0].empty())
        {
            std::cout << "Matriz vazia ou com linhas vazias." << std::endl;
            return;
        }

        int linhas = M.size();
        int colunas = M.at(0).size();
        std::cout << " Matriz -= " << nomeMatriz << " =-" << std::endl;

        for (int i = 0; i < linhas; i++)
        {
            std::cout << "    ";
            for (int j = 0; j < colunas; j++)
            {
                std::cout << std::fixed << std::setprecision(2) << std::setw(8) << M.at(i).at(j) << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    };

    static void printarVetor(const std::vector<float> &V, std::string nomeVetor = "")
    {
        // Verifica se o vetor está vazio
        if (V.empty())
        {
            std::cout << "Vetor vazio." << std::endl;
            return;
        }

        std::cout << "Vetor -= " << nomeVetor << " =-" << std::endl;
        std::cout << "    ";

        // Imprime cada elemento do vetor
        for (const auto &elemento : V)
        {
            std::cout << std::fixed << std::setprecision(2) << std::setw(8) << elemento << " ";
        }

        std::cout << std::endl << std::endl;
    }

    static void Calcular(std::vector<std::vector<float>> &M)
    {
        // Verifica se a matriz está vazia
        if (M.empty() || M.at(0).empty()) 
        {
            std::cout << "Matriz vazia ou com linhas vazias." << std::endl;
            return;
        }

        std::vector<std::vector<float>> a(M.size(), std::vector<float>(M[0].size() - 1));
        std::vector<float> b(M.size());
        std::vector<float> Y(M.size());
        std::vector<float> X(M.size());

        int linhas = a.size();
        int colunas = a.at(0).size();

        for (int i = 0; i < linhas; i++) 
        {
            for (int j = 0; j < colunas; j++) 
            {
                a[i][j] = M[i][j];
            }
            b[i] = M[i][colunas];
            Y[i] = 0;
            X[i] = 0;
        }

        printarMatriz(a, "a");
        printarVetor(b, "b");

        std::vector<std::vector<float>> U = a;
        std::vector<std::vector<float>> L(linhas, std::vector<float>(colunas, 0));
        for (int i = 0; i < std::min(linhas, colunas); i++) 
        {
            L[i][i] = 1;
        }
        printarMatriz(U, "U");

        for (int pivo = 0; pivo < std::min(linhas, colunas - 1); pivo++) 
        {
            if (U[pivo][pivo] == 0) 
            {
                for (int k = pivo + 1; k < linhas; k++) 
                {
                    if (U[k][pivo] != 0) 
                    {
                        std::swap(U[pivo], U[k]);
                        std::swap(b[pivo], b[k]);
                        std::swap(a[pivo], a[k]);
                        break;
                    }
                }
            }

            for (int l = pivo + 1; l < linhas; l++) 
            {
                float m = U[l][pivo] / U[pivo][pivo];
                L[l][pivo] = m;

                for (int c = pivo; c < colunas; c++) 
                {
                    U[l][c] -= m * U[pivo][c];
                }
            }

            printarMatriz(U, "U");
            printarMatriz(L, "L");
        }

        // Achar os valores de Y
        for (int i = 0; i < linhas; i++)
        {
            float soma = 0;
            for (int j = 0; j < i; j++) // Soma os termos anteriores de L * Y
            {
                soma += L[i][j] * Y[j];
            }
            Y[i] = (b[i] - soma) / L[i][i]; // Resolve para Y
        }
        printarVetor(Y, "Y");

        // Achar os valores de X
        for (int i = linhas -1; i >= 0; i--)
        {
            float soma = 0;
            for (int j = i + 1; j < colunas; j++) // Soma os termos anteriores de L * Y
            {
                soma += U[i][j] * X[j];
            }
            X[i] = (Y[i] - soma) / U[i][i]; // Resolve para X
        }
        printarVetor(X, "X");

    };

};

#endif