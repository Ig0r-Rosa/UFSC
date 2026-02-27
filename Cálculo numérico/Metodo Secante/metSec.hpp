#ifndef METSEC_HPP
#define METSEC_HPP  

#include <cmath> 
#include <iostream>

class metSecante
{
    private:

    public:
    metSecante(){};
    ~metSecante(){};

    static float Funcao(float x)
    {
        // Função f(x) = x² + x - 6
        return pow(x,2) + x - 6;
    };

    static float Calcular(float a, float b, float erro, int inte, float precisaoIni)
    {
        // Variaveis
        float A = a; // Menor valor do intervalo
        float B = b; // Maior valor do intervalo
        float X; // Valor de X na função
        float Xant;
        float Xant2;
        int interacao = 0; // interacao atual
        float intervalo = fabsf(B - A) / precisaoIni; // intervalo de observação entre A e B
        
        Xant = 1.7;
        Xant2 = 1.5;
    
        // Loop
        while(interacao < inte && fabs(X - Xant) > erro)
        {
            // Atualiza X
            float Xaux = X;
            float Xaux2 = Xant;

            X = Xant - ((Funcao(Xant)*(Xant2 - Xant)) / (Funcao(Xant2) - Funcao(Xant)));

            Xant2 = Xaux2;
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

        std::cout << "  ultimo erro: " << fabsf(Funcao(X)) << std::endl;
        return X;
    };

};

#endif