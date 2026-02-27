#ifndef METNEW_HPP
#define METNEW_HPP 

#include <cmath> 
#include <iostream>

class metNewton
{
    private:

    public:
    metNewton(){};
    ~metNewton(){};

    static float Funcao(float x)
    {
        // Função f(x) = 2x - sen(x) - 4
        return (2 * x) - std::sin(x) - 4; 
    };

    static float Funcao_D1(float x)
    {
        // Função f'(x) = 2 - cos(x)
        return 2 - std::cos(x);
    };

    static float Funcao_D2(float x)
    {
        // Função f''(x) = sen(x)
        return std::sin(x);
    };

    static float Calcular(float a, float b, float erro, int inte, float precisaoIni)
    {
        // Variaveis
        float A = a; // Menor valor do intervalo
        float B = b; // Maior valor do intervalo
        float X; // Valor de X na função
        float Xant;
        int interacao = 0; // interacao atual
        float intervalo = fabsf(B - A) / precisaoIni; // intervalo de observação entre A e B

        // Achar pontos
        // Varre o intervalo de A até B com intervalo calculado
        X = A;
        while(X <= B)
        {
            // Achou o 0 entre A e B
            if((Funcao(X) > 0 && Funcao(X + intervalo) < 0) || (Funcao(X) < 0 && Funcao(X + intervalo) > 0))
            {
                A = X;
                B = X + intervalo;
                std::cout << "  A: " << A << std::endl;
                std::cout << "  B: " << B << std::endl;
                break;
            }
            X += intervalo;
        }

        // Define o X
        if((Funcao(A) * Funcao_D2(A)) > 0)
        {
            X = A;
            Xant = B;
        }   
        else
        {   
            X = B;
            Xant = A;
        }

        std::cout << "  Primeiro X: " << X << std::endl;
    
        // Loop
        while(interacao < inte && fabsf(X - Xant) > erro)
        {
            // Atualiza X
            float Xaux = X;
            X = Xant -(Funcao(Xant) / Funcao_D1(Xant));
            Xant = Xaux;

            // imprime a interação
            std::cout << " -=-=-=-=-   interacao: " << interacao + 1 << "   -=-=-=-=- " << std::endl;
            std::cout << "  X: " << X << std::endl;
            std::cout << "  f(X): " << Funcao(X) << std::endl;
            std::cout << "  erro: " << fabsf((Xant - X)) << std::endl;
            std::cout << " -=-=-=-=- fim da interacao -=-=-=-=- " << std::endl;
            std::cout << std::endl;
            interacao++;
        }

        std::cout << "  ultimo erro: " << fabsf((Xant - X)) << std::endl;
        return X;
    };

};

#endif
