# Analisador léxico e sintático (PLY) para subconjunto de C
# Base: Exemplo Analisador Léxico/Sintático C - Professor (PLY)
# Feito por: Igor de Matos da Rosa - 20103930

import os
import sys

import ply.lex as lex
import ply.yacc as yacc

# Arquivos de teste
base = os.path.dirname(os.path.abspath(__file__))
testes = [
    os.path.join(base, "Testes", "Teste1.c"),
    os.path.join(base, "Testes", "Teste2.c"),
    os.path.join(base, "Testes", "Teste3.c"),
]

# Palavras reservadas <palavra>:<TOKEN>
reserved = {
    "if": "IF",
    "else": "ELSE",
    "int": "INT",
    "main": "MAIN",
    "float": "FLOAT",
    "char": "CHAR",
    "double": "DOUBLE",
    "void": "VOID",
    "return": "RETURN",
    "while": "WHILE",
    "for": "FOR",
}

tokens = [
    "EQ",
    "EQUALS",
    "INCREMENT",
    "DECREMENT",
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
    "CHARACTER",
    "ID",
    "SEMICOLON",
    "RBRACES",
    "LBRACES",
] + list(reserved.values())

t_ignore = " \t\r"


def t_COMMENT_BLOCK(t):
    r"/\*(.|\n)*?\*/"
    t.lexer.lineno += t.value.count("\n")


def t_COMMENT_LINE(t):
    r"//[^\n]*"
    pass


# Operadores compostos precisam ser reconhecidos antes dos simples.
t_EQ = r"=="
t_LE = r"<="
t_GE = r">="
t_NE = r"!="
t_INCREMENT = r"\+\+"
t_DECREMENT = r"--"
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
t_STRING = r"\".*?\""
t_CHARACTER = r"'([^\\']|\\.)'"


def t_FLOAT_N(t):
    r"((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))"
    return t


def t_INTEGER(t):
    r"\d+"
    return t


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
erros_sintaticos = []


def p_programa(p):
    "programa : funcao_principal semicolon_opcional"
    p[0] = p[1]
    print("Reconheci programa principal.")


def p_funcao_principal(p):
    "funcao_principal : INT MAIN LPAREN parametro_main RPAREN bloco"
    p[0] = ("main", p[4], p[6])
    print("Reconheci bloco main().")


def p_parametro_main(p):
    """parametro_main : VOID
    | empty"""
    p[0] = p[1]


def p_bloco(p):
    "bloco : LBRACES lista_comandos RBRACES"
    p[0] = p[2]


def p_lista_comandos(p):
    """lista_comandos : lista_comandos comando
    | empty"""
    p[0] = p[1] if len(p) == 2 else p[1] + [p[2]]


def p_comando(p):
    """comando : declaracao SEMICOLON
    | atribuicao SEMICOLON
    | incremento SEMICOLON
    | chamada_funcao SEMICOLON
    | retorno SEMICOLON
    | comando_condicional
    | comando_repeticao
    | bloco"""
    p[0] = p[1]


def p_declaracao(p):
    "declaracao : tipo lista_declaradores"
    p[0] = ("declaracao", p[1], p[2])
    print(f"Reconheci declaração de variável do tipo {p[1]}.")


def p_tipo(p):
    """tipo : INT
    | FLOAT
    | CHAR
    | DOUBLE"""
    p[0] = p[1]


def p_lista_declaradores(p):
    """lista_declaradores : lista_declaradores COMMA declarador
    | declarador"""
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]


def p_declarador(p):
    """declarador : ID
    | ID EQUALS expressao"""
    p[0] = ("id", p[1]) if len(p) == 2 else ("id", p[1], p[3])


def p_atribuicao(p):
    "atribuicao : ID EQUALS expressao"
    p[0] = ("atribuicao", p[1], p[3])


def p_incremento(p):
    """incremento : ID INCREMENT
    | ID DECREMENT"""
    p[0] = ("incremento", p[1], p[2])


def p_retorno(p):
    "retorno : RETURN expressao_opcional"
    p[0] = ("return", p[2])


def p_comando_condicional(p):
    """comando_condicional : IF LPAREN condicao RPAREN comando %prec IFX
    | IF LPAREN condicao RPAREN comando ELSE comando"""
    if len(p) == 6:
        p[0] = ("if", p[3], p[5])
    else:
        p[0] = ("if_else", p[3], p[5], p[7])
    print("Reconheci estrutura condicional.")


def p_comando_repeticao(p):
    """comando_repeticao : WHILE LPAREN condicao RPAREN comando
    | FOR LPAREN inicio_for SEMICOLON condicao_opcional SEMICOLON atualizacao_for RPAREN comando"""
    nome = "while" if p[1] == "while" else "for"
    p[0] = (nome, p[3:])
    print(f"Reconheci estrutura de repetição {nome}.")


def p_inicio_for(p):
    """inicio_for : declaracao
    | atribuicao
    | incremento
    | empty"""
    p[0] = p[1]


def p_atualizacao_for(p):
    """atualizacao_for : atribuicao
    | incremento
    | empty"""
    p[0] = p[1]


def p_condicao_opcional(p):
    """condicao_opcional : condicao
    | empty"""
    p[0] = p[1]


def p_condicao(p):
    """condicao : expressao operador_relacional expressao
    | expressao"""
    p[0] = p[1] if len(p) == 2 else ("condicao", p[2], p[1], p[3])


def p_operador_relacional(p):
    """operador_relacional : LT
    | LE
    | GT
    | GE
    | NE
    | EQ"""
    p[0] = p[1]


def p_expressao_opcional(p):
    """expressao_opcional : expressao
    | empty"""
    p[0] = p[1]


def p_expressao(p):
    """expressao : expressao PLUS termo
    | expressao MINUS termo
    | termo"""
    p[0] = p[1] if len(p) == 2 else ("expressao", p[2], p[1], p[3])


def p_termo(p):
    """termo : termo TIMES potencia
    | termo DIVIDE potencia
    | potencia"""
    p[0] = p[1] if len(p) == 2 else ("termo", p[2], p[1], p[3])


def p_potencia(p):
    """potencia : fator POWER potencia
    | fator"""
    p[0] = p[1] if len(p) == 2 else ("potencia", p[1], p[3])


def p_fator(p):
    """fator : INTEGER
    | FLOAT_N
    | STRING
    | CHARACTER
    | ID
    | chamada_funcao
    | LPAREN expressao RPAREN
    | MINUS fator"""
    if len(p) == 2:
        p[0] = p[1]
    elif p[1] == "-":
        p[0] = ("negativo", p[2])
    else:
        p[0] = p[2]


def p_chamada_funcao(p):
    "chamada_funcao : ID LPAREN argumentos_opcionais RPAREN"
    p[0] = ("chamada", p[1], p[3])


def p_argumentos_opcionais(p):
    """argumentos_opcionais : lista_argumentos
    | empty"""
    p[0] = p[1]


def p_lista_argumentos(p):
    """lista_argumentos : lista_argumentos COMMA expressao
    | expressao"""
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]


def p_semicolon_opcional(p):
    """semicolon_opcional : SEMICOLON
    | empty"""
    p[0] = None


def p_empty(p):
    "empty :"
    p[0] = []


precedence = (
    ("nonassoc", "IFX"),
    ("nonassoc", "ELSE"),
)


def p_error(p):
    if p:
        msg = f"Erro sintático na linha {p.lineno}: token {p.type} ({p.value!r})"
    else:
        msg = "Erro sintático: fim inesperado do arquivo"
    erros_sintaticos.append(msg)
    print(msg)


parser = yacc.yacc(start="programa", write_tables=False, debug=False)


def tokenizar_fonte(data, mostrar=True):
    lexer.lineno = 1
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


def analisar_sintaxe(fonte):
    erros_sintaticos.clear()
    lexer.lineno = 1
    resultado = parser.parse(fonte, lexer=lexer)
    if erros_sintaticos:
        print("Análise sintática finalizada com erro.")
        return False
    print("Análise sintática concluída: fonte reconhecida.")
    return resultado is not None


def analisar_arquivo(caminho, somente_lexico=False):
    caminho = os.path.abspath(caminho)
    with open(caminho, encoding="utf-8") as f:
        fonte = f.read()
    if somente_lexico:
        print(f"\n=== Análise léxica: {caminho} ===\n")
        tokenizar_fonte(fonte, mostrar=True)
        return
    print(f"\n=== Análise sintática: {caminho} ===\n")
    analisar_sintaxe(fonte)


def main():
    somente_lexico = "--lex" in sys.argv
    arquivos = [a for a in sys.argv[1:] if a != "--lex"]
    if not arquivos:
        arquivos = testes
    for path in arquivos:
        if not os.path.isfile(path):
            print(f"Arquivo não encontrado: {path}", file=sys.stderr)
            continue
        analisar_arquivo(path, somente_lexico=somente_lexico)


if __name__ == "__main__":
    main()
