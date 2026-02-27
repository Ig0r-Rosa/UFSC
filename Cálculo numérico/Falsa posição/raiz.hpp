#ifndef RAIZ_HPP
#define RAIZ_HPP

#include <math.h>  
#include <iostream>

class Raiz
{
    private:

    public:
    Raiz(){};
    ~Raiz(){};

    static float Funcao(float x)
    {
        // Função f(x) = x³ -9*x +3
        return pow(x,3)-(9 * x) + 3;
    };

    static float FalsaPosicao(float A, float B)
    {
        return ((A*Funcao(B))-(B*Funcao(A))) / (Funcao(B) - Funcao(A));
    };

    static float Calcular(float a, float b, float erro, int inte, float precisaoIni)
    {
        // Variaveis
        float A = a; // Menor valor do intervalo
        float B = b; // Maior valor do intervalo
        int interacao = 0; // interacao atual
        float X = 0; // Valor de X na função
        float intervalo = fabsf(B - A) / precisaoIni; // intervalo de observação entre A e B

        // Achar pontos
        // Varre o intervalo de A até B com intervalo calculado
        X = B;
        while(X >= A)
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
            X -= intervalo;
        }
    
        // Loop
        while(interacao < inte && fabsf(Funcao(X)) >= erro)
        {
            // Atualiza X
            //X = (A+B) / 2;
            X = FalsaPosicao(A,B);

            if(Funcao(A) * Funcao(X) < 0)
            {
                B = X;
            }
            else
            {
                A = X;
            }

            X = FalsaPosicao(A,B);

            // imprime a interação
            std::cout << " -=-=-=-=-   interacao: " << interacao + 1 << "   -=-=-=-=- " << std::endl;
            std::cout << "  X: " << X << std::endl;
            std::cout << "  f(X): " << Funcao(X) << std::endl;
            std::cout << "  A: " << A << std::endl;
            std::cout << "  f(A): " << Funcao(A) << std::endl;
            std::cout << "  B: " << B << std::endl;
            std::cout << "  f(B): " << Funcao(B) << std::endl;
            std::cout << "  f(A)*F(X) : " << Funcao(A) * Funcao(X) << std::endl;
            std::cout << "  f(B)*F(X) : " << Funcao(B) * Funcao(X) << std::endl;
            std::cout << " -=-=-=-=- fim da interacao -=-=-=-=- " << std::endl;
            std::cout << std::endl;
            interacao++;
        }

        std::cout << "  ultimo erro: " << fabsf(Funcao(X)) << std::endl;
        return X;
    };

};

#endif
