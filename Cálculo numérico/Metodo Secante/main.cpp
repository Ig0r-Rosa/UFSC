#include <iostream> 
#include "metSec.hpp"  

int main()
{
    // Calcular(valor de A ; valor de B; erro ideal ; maximo de interações ; precisao do intervalo inicial)
    float resultado = metSecante::Calcular(-5, 5, 0.01, 100, 11);
    std::cout << "Resultado:" << resultado << std::endl;

    return 0;
}