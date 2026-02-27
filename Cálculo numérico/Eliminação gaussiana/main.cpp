#include <iostream>
#include "eliminGaussiana.hpp" 

int main()
{
    std::vector<std::vector<float>> M = 
        {{ 2, 4, 6, 2, 4},
         { 1, 2,-1, 3, 8},
         {-3, 1,-2, 1,-2},
         { 1, 3,-3,-2, 6}};

    EliminGaussiana::printarMatriz(M);
    EliminGaussiana::Calcular(M);


    return 0;
}