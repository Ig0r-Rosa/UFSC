#ifndef JACOBI_HPP
#define JACOBI_HPP

#include <math.h>  
#include <iostream>
#include <vector>
#include <iomanip>

class Jacobi
{
    private:

    public:
    Jacobi(){};
    ~Jacobi(){};

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

        int linhas = a.size();
        int colunas = a.at(0).size();

        for (int i = 0; i < linhas; i++) 
        {
            for (int j = 0; j < colunas; j++) 
            {
                a[i][j] = M[i][j];
            }
            b[i] = M[i][colunas -1];

            // Setar valores iniciais
            X[i] = 0;
        }


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
        float erroAtual = 10000000;
        while(numInt < maxInt && erroAtual >= erro)
        {
            numInt++;

            for(int l = 0; l < ; l++)
            {
                for(int c = 0; c < ; c++)
                {

                }
            }
            
        }

    };

};

#endif