# Compilador parcial para subconjunto de C — DEC0004-09655 (20261) Compiladores
# Fases: análise léxica (T1), sintática (T2) e semântica (T3)
# Biblioteca: PLY (Python Lex-Yacc) — gerador LALR(1)
# Feito por: Igor de Matos da Rosa - 20103930

import os
import sys

import ply.lex as lex
import ply.yacc as yacc

from relatorio import RelatorioCompilacao
from semantica import AnalisadorSemantico, TIPOS_NUMERICOS
from tabela_simbolos import TabelaSimbolos

# Diretório base do projeto
BASE = os.path.dirname(os.path.abspath(__file__))

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

# Componentes globais compartilhados entre léxico, sintaxe e semântica
tabela_simbolos = TabelaSimbolos()
relatorio = RelatorioCompilacao()
semantica = AnalisadorSemantico(tabela_simbolos, relatorio)
erros_sintaticos = []


def _linha(p, indice=1):
  """
  Obtém a linha do símbolo na produção corrente.
  Usado nos diagnósticos semânticos (referência à posição no fonte).
  """
  try:
    linha = p.lineno(indice)
    if linha:
      return linha
  except (AttributeError, IndexError):
    pass
  return lexer.lineno


def t_COMMENT_BLOCK(t):
  r"/\*(.|\n)*?\*/"
  t.lexer.lineno += t.value.count("\n")


def t_COMMENT_LINE(t):
  r"//[^\n]*"
  pass


# Operadores compostos devem ser reconhecidos antes dos simples (conflito léxico)
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
  mensagem = (
      f"Erro léxico na linha {t.lexer.lineno}: caractere {t.value[0]!r}"
  )
  relatorio.registrar_erro_lexico(mensagem)
  t.lexer.skip(1)


lexer = lex.lex()


# --- Gramática e ações semânticas (atributos sintetizados em p[0]) ---


def p_programa(p):
  """programa : funcao_principal semicolon_opcional"""
  p[0] = p[1]
  relatorio.registrar_sintaxe("programa principal (int main)")


def p_funcao_principal(p):
  """funcao_principal : INT MAIN LPAREN parametro_main RPAREN bloco"""
  p[0] = ("main", p[4], p[6])
  relatorio.registrar_sintaxe("função main() com bloco composto")


def p_parametro_main(p):
  """parametro_main : VOID
  | empty"""
  p[0] = p[1]


def p_abre_bloco(p):
  """abre_bloco : LBRACES"""
  # Ação semântica: novo escopo léxico ao abrir bloco (conceito de tabela de símbolos)
  tabela_simbolos.entrar_escopo()


def p_bloco(p):
  """bloco : abre_bloco lista_comandos RBRACES"""
  tabela_simbolos.sair_escopo()
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
  """declaracao : tipo lista_declaradores"""
  tipo = p[1]
  for declarador in p[2]:
    nome = declarador[1]
    semantica.declarar_variavel(nome, tipo, _linha(p, 2))
    if len(declarador) == 3:
      tipo_ini = semantica.no_tipo(declarador[2])
      if not semantica.tipos_compativeis_atribuicao(tipo, tipo_ini):
        semantica.registrar_erro(
          f"inicialização inválida de '{nome}': esperado {tipo}, "
          f"recebido {tipo_ini}",
          _linha(p, 2),
        )
  p[0] = ("declaracao", tipo, p[2])
  nomes = ", ".join(d[1] for d in p[2])
  relatorio.registrar_sintaxe(f"declaração de variáveis ({tipo}: {nomes})")


def p_tipo(p):
  """tipo : INT
  | FLOAT
  | CHAR
  | DOUBLE"""
  p[0] = semantica.tipo_de_token(p.slice[1].type)


def p_lista_declaradores(p):
  """lista_declaradores : lista_declaradores COMMA declarador
  | declarador"""
  p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]


def p_declarador(p):
  """declarador : ID
  | ID EQUALS expressao"""
  p[0] = ("id", p[1]) if len(p) == 2 else ("id", p[1], p[3])


def p_atribuicao(p):
  """atribuicao : ID EQUALS expressao"""
  tipo_expr = semantica.no_tipo(p[3])
  semantica.verificar_atribuicao(p[1], tipo_expr, _linha(p, 1))
  p[0] = ("atribuicao", p[1], p[3])


def p_incremento(p):
  """incremento : ID INCREMENT
  | ID DECREMENT"""
  semantica.verificar_uso(p[1], _linha(p, 1))
  p[0] = ("incremento", p[1], p[2])


def p_retorno(p):
  """retorno : RETURN expressao_opcional"""
  p[0] = ("return", p[2])


def p_comando_condicional(p):
  """comando_condicional : IF LPAREN condicao RPAREN comando %prec IFX
  | IF LPAREN condicao RPAREN comando ELSE comando"""
  if len(p) == 6:
    p[0] = ("if", p[3], p[5])
  else:
    p[0] = ("if_else", p[3], p[5], p[7])
  relatorio.registrar_sintaxe("estrutura condicional if/else")


def p_comando_repeticao(p):
  """comando_repeticao : WHILE LPAREN condicao RPAREN comando
  | FOR LPAREN inicio_for SEMICOLON condicao_opcional SEMICOLON atualizacao_for RPAREN comando"""
  nome = "while" if p[1] == "while" else "for"
  p[0] = (nome, p[3:])
  relatorio.registrar_sintaxe(f"estrutura de repetição {nome}")


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
  if p[1] is not None:
    semantica.verificar_condicao(semantica.no_tipo(p[1]), _linha(p, 1))


def p_condicao(p):
  """condicao : expressao operador_relacional expressao
  | expressao"""
  if len(p) == 2:
    tipo = semantica.no_tipo(p[1])
    semantica.verificar_condicao(tipo, _linha(p, 1))
    p[0] = (tipo, ("condicao_simples", p[1]))
  else:
    tipo_esq = semantica.no_tipo(p[1])
    tipo_dir = semantica.no_tipo(p[3])
    tipo = semantica.tipo_resultante_binario(p[2], tipo_esq, tipo_dir, _linha(p, 2))
    semantica.verificar_condicao(tipo, _linha(p, 2))
    p[0] = (tipo, ("condicao", p[2], p[1], p[3]))


def p_operador_relacional(p):
  """operador_relacional : LT
  | LE
  | GT
  | GE
  | NE
  | EQ"""
  mapa = {"LT": "<", "LE": "<=", "GT": ">", "GE": ">=", "NE": "!=", "EQ": "=="}
  p[0] = mapa[p.slice[1].type]


def p_expressao_opcional(p):
  """expressao_opcional : expressao
  | empty"""
  p[0] = p[1]


def p_expressao(p):
  """expressao : expressao PLUS termo
  | expressao MINUS termo
  | termo"""
  if len(p) == 2:
    p[0] = p[1]
  else:
    tipo_esq = semantica.no_tipo(p[1])
    tipo_dir = semantica.no_tipo(p[3])
    op = p.slice[2].value if hasattr(p.slice[2], "value") else p[2]
    tipo = semantica.tipo_resultante_binario(op, tipo_esq, tipo_dir, _linha(p))
    p[0] = (tipo, ("expressao", op, p[1], p[3]))


def p_termo(p):
  """termo : termo TIMES potencia
  | termo DIVIDE potencia
  | potencia"""
  if len(p) == 2:
    p[0] = p[1]
  else:
    tipo_esq = semantica.no_tipo(p[1])
    tipo_dir = semantica.no_tipo(p[3])
    op = p.slice[2].value if hasattr(p.slice[2], "value") else p[2]
    tipo = semantica.tipo_resultante_binario(op, tipo_esq, tipo_dir, _linha(p))
    p[0] = (tipo, ("termo", op, p[1], p[3]))


def p_potencia(p):
  """potencia : fator POWER potencia
  | fator"""
  if len(p) == 2:
    p[0] = p[1]
  else:
    tipo_esq = semantica.no_tipo(p[1])
    tipo_dir = semantica.no_tipo(p[3])
    tipo = semantica.tipo_resultante_binario("^", tipo_esq, tipo_dir, _linha(p))
    p[0] = (tipo, ("potencia", p[1], p[3]))


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
    if p.slice[1].type in ("INTEGER", "FLOAT_N", "STRING", "CHARACTER"):
      tipo = semantica.tipo_literal(p.slice[1].type)
      p[0] = (tipo, ("literal", p[1], tipo))
    elif p.slice[1].type == "ID":
      tipo = semantica.verificar_uso(p[1], _linha(p, 1))
      p[0] = (tipo, ("id", p[1]))
    else:
      p[0] = p[1]
  elif p[1] == "-":
    tipo = semantica.no_tipo(p[2])
    if tipo not in TIPOS_NUMERICOS:
      semantica.registrar_erro(f"operador unário '-' inválido para {tipo}", _linha(p))
      tipo = "erro"
    p[0] = (tipo, ("negativo", p[2]))
  else:
    p[0] = p[2]


def p_chamada_funcao(p):
  """chamada_funcao : ID LPAREN argumentos_opcionais RPAREN"""
  semantica.verificar_uso(p[1], _linha(p, 1))
  p[0] = ("int", ("chamada", p[1], p[3]))


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
  """empty :"""
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
  relatorio.erros_sintaticos.append(msg)


parser = yacc.yacc(start="programa", write_tables=False, debug=False)


def tokenizar_fonte(fonte):
  """
  Executa a análise léxica e armazena os tokens no relatório.
  Conceito: autômato finito definido por expressões regulares (PLY Lex).
  """
  lexer.lineno = 1
  lexer.input(fonte)
  saida = []
  while True:
    tok = lexer.token()
    if not tok:
      break
    saida.append(tok)
    relatorio.registrar_token(tok)
  return saida


def finalizar_relatorio():
  """Copia erros semânticos e exibe o relatório consolidado."""
  relatorio.erros_semanticos = list(semantica.erros)
  relatorio.exibir()


def analisar_fonte(fonte, fase="completa", arquivo=""):
  """
  Pipeline do compilador parcial:
  - 'lex': somente tokenização;
  - 'sint': léxico + parser LALR(1);
  - 'completa': léxico + sintaxe + semântica.
  """
  erros_sintaticos.clear()
  semantica.limpar_erros()
  tabela_simbolos.limpar()
  relatorio.limpar()
  relatorio.arquivo = arquivo
  relatorio.fase = fase
  lexer.lineno = 1

  tokenizar_fonte(fonte)

  if fase == "lex":
    finalizar_relatorio()
    return not relatorio.erros_lexicos

  lexer.lineno = 1
  lexer.input(fonte)
  resultado = parser.parse(fonte, lexer=lexer)
  relatorio.erros_sintaticos = list(erros_sintaticos)

  if fase == "sint":
    finalizar_relatorio()
    return resultado is not None and not erros_sintaticos

  relatorio.erros_semanticos = list(semantica.erros)
  finalizar_relatorio()
  return (
      resultado is not None
      and not erros_sintaticos
      and not semantica.erros
  )


def analisar_arquivo(caminho, fase="completa"):
  """Lê arquivo .c, executa a análise e gera o relatório final."""
  caminho = os.path.abspath(caminho)
  with open(caminho, encoding="utf-8") as arquivo:
    fonte = arquivo.read()
  return analisar_fonte(fonte, fase=fase, arquivo=caminho)


def exibir_uso():
  """Exibe instruções de uso quando o arquivo fonte não é informado."""
  print(
    "Uso: python3 compilador_c.py [--lex | --sint] <arquivo.c>\n"
    "\n"
    "  --lex   executa somente a análise léxica\n"
    "  --sint  executa análise léxica e sintática\n"
    "  (sem flag) executa análise completa (léxica, sintática e semântica)\n"
    "\n"
    "Exemplo:\n"
    "  python3 compilador_c.py Testes/ExemploEnunciado.c",
    file=sys.stderr,
  )


def main():
  """Ponto de entrada: exige um único arquivo .c informado na linha de comando."""
  fase = "completa"
  if "--lex" in sys.argv:
    fase = "lex"
  elif "--sint" in sys.argv:
    fase = "sint"

  arquivos = [a for a in sys.argv[1:] if not a.startswith("--")]
  if len(arquivos) != 1:
    exibir_uso()
    sys.exit(1)

  caminho = arquivos[0]
  if not os.path.isfile(caminho):
    print(f"Arquivo não encontrado: {caminho}", file=sys.stderr)
    sys.exit(1)

  analisar_arquivo(caminho, fase=fase)


if __name__ == "__main__":
  main()
