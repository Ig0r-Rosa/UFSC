# Exemplo MoonBit — Seminário de Compiladores

Mini projeto para demonstração ao vivo em aula.

## Pré-requisitos

```bash
curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash
source ~/.zshrc   # ou reinicie o terminal
```

## Comandos

| Comando | O que faz |
|---------|-----------|
| `moon run cmd/main` | Executa o programa |
| `moon test` | Roda os testes |
| `moon check` | Verifica tipos e compila |
| `moon fmt` | Formata o código |

## O que o exemplo mostra

| Conceito | Onde |
|----------|------|
| `enum` (AST) | `exemplo_moonbit.mbt` |
| Pattern matching | função `eval` |
| Funções públicas (`pub`) | `eval`, `fib`, `demo_expr` |
| Testes integrados | `exemplo_moonbit_test.mbt` |

## Saída esperada

```
Expressao: (2 + 3) * 4
Resultado: 20
fib(10) = 89
```
