# ATIVIDADE PRÁTICA - reconhecedor de estruturas em C (analisador léxico com PLY)

import ply.lex as lex

# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    # Tipos (declaração de variáveis)
    "int": "INT",
    "char": "CHAR",
    "float": "KW_FLOAT",
    "double": "DOUBLE",
    "void": "VOID",
    "short": "SHORT",
    "long": "LONG",
    "signed": "SIGNED",
    "unsigned": "UNSIGNED",
    # Controle de fluxo
    "if": "IF",
    "else": "ELSE",
    "for": "FOR",
    "while": "WHILE",
    "return": "RETURN",
    # Ponto de entrada
    "main": "MAIN",
}

tokens = [
    "EQ",
    "EQUALS",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "POWER",
    "LPAREN",
    "RPAREN",
    "LT",
    "LE",
    "GT",
    "GE",
    "NE",
    "COMMA",
    "INTEGER",
    "FLOAT",
    "STRING",
    "ID",
    "NEWLINE",
    "SEMICOLON",
    "RBRACES",
    "LBRACES",
] + list(reserved.values())

t_ignore = " \t"


def t_COMMENT(t):
    r"//[^\n]*"
    pass


def t_EQ(t):
    r"=="
    return t


t_EQUALS = r"="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_POWER = r"\^"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_RBRACES = r"\}"
t_LBRACES = r"\{"
t_LT = r"<"
t_LE = r"<="
t_GT = r">"
t_GE = r">="
t_NE = r"!="
t_COMMA = r","
t_SEMICOLON = r";"
t_INTEGER = r"\d+"
t_FLOAT = r"((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))"
t_STRING = r"\".*?\""


def t_NEWLINE(t):
    r"\n"
    t.lexer.lineno += 1
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

# Teste com todas as estruturas pedidas: tipos/declarações, main(), if/if-else, for, while
data = """
int main(void) {
    int x, y;
    float z;
    char c;

    x = 0;
    y = 10;
    z = 1.5;

    if (x < y) {
        x = x + 1;
    } else {
        if (x > y) {
            y = x;
        } else {
            x = 0;
            y = 0;
        }
    }

    for (x = 0; x < 10; x = x + 1) {
        y = y + 1;
    }

    while (y > 0) {
        y = y - 1;
    }

    return 0;
}
"""

lexer.input(data)

for tok in lexer:
    print(tok)
