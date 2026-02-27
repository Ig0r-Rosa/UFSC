#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int main() {
    // Nome do arquivo CSV original e do arquivo de saída
    std::string input_filename = "datatf.csv";
    std::string output_filename = "datatf_fixed.csv";

    // Abrir o arquivo de entrada
    std::ifstream infile(input_filename);
    if (!infile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << input_filename << std::endl;
        return 1;
    }

    // Abrir o arquivo de saída
    std::ofstream outfile(output_filename);
    if (!outfile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << output_filename << std::endl;
        return 1;
    }

    std::string line;
    
    // Ler cada linha do arquivo de entrada
    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        std::string col1, col2;

        // Ler as duas primeiras colunas
        std::getline(ss, col1, ',');
        std::getline(ss, col2, ',');

        // Adicionar uma terceira coluna (por exemplo, com o valor '0')
        outfile << col1 << "," << col2 << ",0" << std::endl;
    }

    // Fechar os arquivos
    infile.close();
    outfile.close();

    std::cout << "Arquivo " << output_filename << " gerado com a terceira coluna." << std::endl;
    
    return 0;
}
