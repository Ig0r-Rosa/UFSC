int main() {
    int i = 0;
    int total = 0;
    float media = 0.0;

    for (i = 0; i < 10; i = i + 1) {
        total = total + i;
    }

    while (total > 10) {
        total = total - 1;
    }

    if (total == 10) {
        media = total / 2;
    } else {
        if (total < 10) {
            media = 1.5;
        } else {
            media = 0.0;
        }
    }
}
