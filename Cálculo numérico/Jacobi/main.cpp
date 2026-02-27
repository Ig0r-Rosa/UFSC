#include <iostream>
#include "Jacobi.hpp" 

int main()
{
    std::vector<std::vector<float>> M;
    M = {{ 6,-1, 1, 7},
         { 1, 8,-1, 16},
         { 1, 1, 5, 18}};

    Jacobi::printarMatriz(M, "M");
    Jacobi::Calcular(M, 100, 0.001);


    return 0;
}