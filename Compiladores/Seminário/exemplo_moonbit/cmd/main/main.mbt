///|
/// Ponto de entrada — execute com: moon run cmd/main
fn main {
  let expr = @lib.demo_expr()
  let result = @lib.eval(expr)
  println("Expressao: (2 + 3) * 4")
  println("Resultado: \{result}")
  println("fib(10) = \{@lib.fib(10)}")
}
