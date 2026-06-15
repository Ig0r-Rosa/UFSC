// Erro semântico esperado: condição não numérica em if
int main() {
    int ok = 1;
    if ("nao e numero") {
        ok = 0;
    }
}
