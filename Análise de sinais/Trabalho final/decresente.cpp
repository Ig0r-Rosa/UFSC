#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

// Estrutura para armazenar os dados de tempo e valor
struct DataPoint {
    double time;
    double value;
};

// Função para comparar os tempos (para ordenar)
bool compareByTime(const DataPoint& a, const DataPoint& b) {
    return a.time < b.time;
}

int main() {
    std::string input_filename = "datatf.csv";  // Arquivo de entrada
    std::string output_filename = "datatf_sorted.csv";  // Arquivo de saída

    std::ifstream infile(input_filename);
    if (!infile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << input_filename << std::endl;
        return 1;
    }

    std::vector<DataPoint> data;  // Vetor para armazenar os dados

    std::string line;
    
    // Ler o arquivo e armazenar os dados no vetor
    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        DataPoint dp;

        // Ler o tempo e o valor
        ss >> dp.time;
        ss.ignore(1, ',');  // Ignora a vírgula
        ss >> dp.value;

        // Armazenar no vetor
        data.push_back(dp);
    }

    infile.close();

    // Ordenar os dados por tempo
    std::sort(data.begin(), data.end(), compareByTime);

    // Abrir o arquivo de saída
    std::ofstream outfile(output_filename);
    if (!outfile.is_open()) {
        std::cerr << "Erro ao abrir o arquivo " << output_filename << std::endl;
        return 1;
    }

    // Escrever os dados ordenados no arquivo de saída
    for (const auto& dp : data) {
        outfile << dp.time << "," << dp.value << std::endl;
    }

    outfile.close();

    std::cout << "Arquivo " << output_filename << " gerado com os dados ordenados." << std::endl;

    return 0;
}
