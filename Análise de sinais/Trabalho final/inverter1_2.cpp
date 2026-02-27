#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

// Função para inverter a primeira e a segunda coluna
int main() {
    std::string input_filename = "datatf.csv";  // Nome do arquivo de entrada
    std::string output_filename = "datatf_inverted.csv";  // Nome do arquivo de saída

    std::ifstream infile(input_filename);
    if (!infile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << input_filename << std::endl;
        return 1;
    }

    std::vector<std::pair<std::string, std::string>> data;  // Vetor para armazenar os dados das colunas

    std::string line;
    
    // Ler o arquivo e armazenar os dados no vetor
    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        std::string col1, col2;

        // Ler as duas colunas (assumindo que as colunas estão separadas por vírgulas)
        std::getline(ss, col1, ',');
        std::getline(ss, col2, ',');

        // Armazenar a troca das colunas no vetor
        data.push_back({col2, col1});  // Inverter as colunas
    }

    infile.close();

    // Abrir o arquivo de saída
    std::ofstream outfile(output_filename);
    if (!outfile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << output_filename << std::endl;
        return 1;
    }

    // Escrever os dados invertidos no arquivo de saída
    for (const auto& pair : data) {
        outfile << pair.first << "," << pair.second << std::endl;
    }

    outfile.close();

    std::cout << "Arquivo " << output_filename << " gerado com as colunas invertidas." << std::endl;

    return 0;
}