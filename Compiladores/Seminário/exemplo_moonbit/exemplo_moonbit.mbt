///|
/// AST de expressões aritméticas — bloco básico de um compilador/interpretador.
enum Expr {
  Num(Int)
  Add(Expr, Expr)
  Mul(Expr, Expr)
}

///|
/// Avalia a árvore recursivamente (interpretador sobre AST).
pub fn eval(expr : Expr) -> Int {
  match expr {
    Num(n) => n
    Add(a, b) => eval(a) + eval(b)
    Mul(a, b) => eval(a) * eval(b)
  }
}

///|
/// Fibonacci iterativo — exemplo clássico da documentação MoonBit.
pub fn fib(n : Int) -> Int64 {
  for i = 0, a = 0L, b = 1L; i < n; i = i + 1, a = b, b = a + b {
  } nobreak {
    b
  }
}

///|
/// Expressão de demonstração: (2 + 3) * 4 = 20
pub fn demo_expr() -> Expr {
  Mul(Add(Num(2), Num(3)), Num(4))
}
