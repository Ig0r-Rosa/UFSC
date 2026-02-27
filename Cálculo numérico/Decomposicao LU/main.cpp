#include <iostream>
#include "DecLU.hpp" 

int main()
{
    std::vector<std::vector<float>> M;
    M = {{ 1, 1, 2, 4},
         { 2,-1,-1, 0},
         { 1,-1,-1,-1}};

    DecLU::printarMatriz(M, "M");
    DecLU::Calcular(M);


    return 0;
}