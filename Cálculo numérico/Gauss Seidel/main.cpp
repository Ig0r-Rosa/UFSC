#include <iostream>
#include "GaussSeidel.hpp" 

int main()
{
    std::vector<std::vector<float>> M;
    M = {{ 10, 1, 1, 12},
         { 2, 8,-4, 6},
         { 1, 5, 9, 15}};

    GaussSeidel::printarMatriz(M, "M");
    GaussSeidel::Calcular(M, 100, 0.001);


    return 0;
}