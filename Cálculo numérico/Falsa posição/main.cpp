#include <iostream>
#include "raiz.hpp" 

int main()
{
    // Calcular(valor de A ; valor de B; erro ideal ; maximo de interações ; precisao do intervalo inicial)
    float resultado = Raiz::Calcular(-5, 5, 0.001, 100, 10);
    std::cout << "Resultado:" << resultado << std::endl;

    return 0;
}
