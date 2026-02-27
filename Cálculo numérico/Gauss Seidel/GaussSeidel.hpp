#ifndef SEIDEL_HPP
#define SEIDEL_HPP

#include <math.h>  
#include <iostream>
#include <vector>
#include <iomanip>

class GaussSeidel
{
    private:

    public:
    GaussSeidel(){};
    ~GaussSeidel(){};

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
                std::cout << std::fixed << std::setprecision(3) << std::setw(8) << M.at(i).at(j) << " ";
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
            std::cout << std::fixed << std::setprecision(3) << std::setw(8) << elemento << " ";
        }

        std::cout << std::endl << std::endl;
    };

    static void Calcular(std::vector<std::vector<float>> &M, int maxInt, float erro)
    {
         // Verifica se a matriz está vazia
        if (M.empty() || M.at(0).empty()) 
        {
            std::cout << "Matriz vazia ou com linhas vazias." << std::endl;
            return;
        }

        std::vector<std::vector<float>> a(M.size(), std::vector<float>(M[0].size() - 1));
        std::vector<float> b(M.size());
        std::vector<float> X(M.size());
        std::vector<float> Xant(M.size());

        int linhas = a.size();
        int colunas = a.at(0).size();

        for (int i = 0; i < linhas; i++) 
        {
            for (int j = 0; j < colunas; j++) 
            {
                a[i][j] = M[i][j];
            }
            b[i] = M[i][colunas];

            // Setar valores iniciais
            X[i] = 0;
            Xant[i] = 0;
        }

        /*X[0] = 0;
        X[1] = 0.75;
        X[2] = 1.25;
        Xant = X;*/

        printarMatriz(a, "A");
        printarVetor(b, "b");


        // Testa convergência
        bool convergencia = true;

        for(int pivo = 0; pivo < std::min(linhas, colunas); pivo++)
        {
            int sumLinha = 0;
            for(int c = 0; c < colunas; c++)
            {
                if(c!= pivo)
                {
                    sumLinha += fabsf(a[pivo][c]);
                }
            }
            std::cout << sumLinha << std::endl;
            if(fabsf(a[pivo][pivo]) <= sumLinha)
            {
                convergencia = false;
                std::cout  << "Diagonal não dominante!" << std::endl;
            }
        }
        if(convergencia == true)
        {
            std::cout  << "Diagonal dominante!" << std::endl;
        }

        // Loop principal
        int numInt = 0;
        while (numInt < maxInt)
        {
            numInt++;
            bool atingiuErro = true;

            for (int i = 0; i < linhas; i++)
            {
                float sum = 0;
                for (int j = 0; j < i; j++)
                {
                    sum -= a[i][j] * X[j];
                }   
                for (int j = i + 1; j < colunas; j++)
                {
                    sum -= a[i][j] * Xant[j];
                }   

                X[i] = (b[i] + sum) / a[i][i];

                // Calcular o erro relativo
                float erroAtual = fabsf(X[i] - Xant[i]);
                std::cout << "Erro atual: " << erroAtual << std::endl;

                if (erroAtual > erro)
                {
                    atingiuErro = false;
                }
            }

            // Atualizar Xant para a próxima iteração
            Xant = X;

            if (atingiuErro)  // Se o erro para todas as variáveis for menor que o limite, parar
            {
                break;
            }

            std::cout << std::endl << "  Iteração " << numInt << std::endl;
            printarVetor(X, "X");
        }

    };

};

#endif