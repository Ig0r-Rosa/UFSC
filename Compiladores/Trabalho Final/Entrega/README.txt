Trabalho Final - Compilador Parcial (subconjunto de C)
Disciplina: DEC0004-09655 (20261) - Compiladores - UFSC
Autor: Igor de Matos da Rosa - 20103930

DESCRIÇÃO
---------
Implementação parcial de compilador com três fases:
  1. Análise léxica  - reconhecimento de tokens (PLY Lex)
  2. Análise sintática - gramática LALR(1) com PLY Yacc
  3. Análise semântica - tabela de símbolos e verificação de tipos

Arquivos principais:
  - compilador_c.py    : léxico, sintaxe e integração semântica
  - tabela_simbolos.py : escopos e declarações de variáveis
  - semantica.py       : ações semânticas (tipos, atribuições, condições)

REQUISITOS
----------
- Python 3.8 ou superior
- Biblioteca PLY (python3-ply ou pip install ply)

  sudo apt install python3-ply
  # ou
  pip install ply

EXECUÇÃO
--------
Na pasta "Trabalho Final", informe um único arquivo .c por execução:

  # Análise completa (léxica + sintática + semântica)
  python3 compilador_c.py Testes/ExemploEnunciado.c

Ao final da execução, é exibido um relatório consolidado com:
  - tokens reconhecidos (análise léxica)
  - estruturas validadas pela gramática (análise sintática)
  - tabela de símbolos e ações semânticas (análise semântica)
  - resultado final da compilação parcial

  # Somente análise léxica (lista de tokens)
  python3 compilador_c.py --lex Testes/Teste1.c

  # Léxico + sintaxe, sem verificação semântica
  python3 compilador_c.py --sint Testes/Teste1.c

TESTES
------
Programas válidos (devem concluir sem erros semânticos):
  Testes/ExemploEnunciado.c  - exemplo do enunciado do trabalho final
  Testes/Teste1.c            - if/else aninhado
  Testes/Teste2.c            - laço while
  Testes/Teste3.c            - for, while e condicionais

Programas com erro semântico esperado:
  Testes/Erro_VariavelNaoDeclarada.c
  Testes/Erro_Redeclaracao.c
  Testes/Erro_TipoIncompativel.c
  Testes/Erro_CondicaoInvalida.c

Entregáveis deste trabalho:
  - Código fonte (compilador_c.py e módulos auxiliares)
  - README.txt (instruções de execução)
  - Relatorio.pdf (relatório teórico-prático em PDF)
  - Relatorio.tex (fonte LaTeX do relatório, para edição)

AÇÕES SEMÂNTICAS IMPLEMENTADAS
------------------------------
1. Registro de declarações na tabela de símbolos (com escopos de bloco)
2. Verificação de variável declarada antes do uso
3. Verificação de redeclaração no mesmo escopo
4. Compatibilidade de tipos em atribuições e inicializações
5. Verificação de tipos em expressões aritméticas e relacionais
6. Validação de condições em if/while/for

RELATÓRIO ACADÊMICO
--------------------
O arquivo Relatorio.pdf descreve a implementação e relaciona cada fase
às Unidades 1--4 da disciplina (Introdução, Análise Léxica, Sintática e
Semântica). Para recompilar o PDF a partir do LaTeX:

  pdflatex Relatorio.tex
  pdflatex Relatorio.tex
