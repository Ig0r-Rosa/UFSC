# Analisador léxico (PLY Lex) para subconjunto de C — T1 Compiladores UFSC
# Base: Exemplo Analisador Léxico C - Professor (PLY)
# Feito por: Igor de Matos da Rosa - 20103930

import os
import sys

import ply.lex as lex

# Arquivos de teste
base = os.path.dirname(os.path.abspath(__file__))
testes = [
        os.path.join(base, "Teste1.c"),
        os.path.join(base, "Teste2.c"),
    ]

# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    "if": "IF",
    "else": "ELSE",
    "int": "INT",
    "main": "MAIN",
    "float": "FLOAT",
    "while": "WHILE",
    "for": "FOR",
}

tokens = [
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
    "FLOAT_N",
    "STRING",
    "ID",
    "SEMICOLON",
    "RBRACES",
    "LBRACES",
] + list(reserved.values())

t_ignore = " \t\r"

# Ordem: operadores compostos antes dos simples
t_LE = r"<="
t_GE = r">="
t_NE = r"!="
t_LT = r"<"
t_GT = r">"
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
t_COMMA = r","
t_SEMICOLON = r";"
t_INTEGER = r"\d+"
t_FLOAT_N = r"((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))"
t_STRING = r"\".*?\""


def t_COMMENT(t):
    r"//[^\n]*"
    pass


def t_NEWLINE(t):
    r"\n"
    t.lexer.lineno += 1


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_error(t):
    print(f"Caractere ilegal na linha {t.lexer.lineno}: {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex.lex()


def tokenizar_fonte(data, mostrar=True):
    lexer.input(data)
    saida = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        saida.append(tok)
        if mostrar:
            print(tok)
    return saida


def analisar_arquivo(caminho):
    caminho = os.path.abspath(caminho)
    with open(caminho, encoding="utf-8") as f:
        fonte = f.read()
    print(f"\n=== Análise léxica: {caminho} ===\n")
    tokenizar_fonte(fonte, mostrar=True)


def main():
    arquivos = [a for a in sys.argv[1:] if a != "--lex"]
    if not arquivos:
        arquivos = testes
    for path in arquivos:
        if not os.path.isfile(path):
            print(f"Arquivo não encontrado: {path}", file=sys.stderr)
            continue
        analisar_arquivo(path)


if __name__ == "__main__":
    main()
