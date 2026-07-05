///|
test "eval expressao demo" {
  inspect(@exemplo_moonbit.eval(@exemplo_moonbit.demo_expr()), content="20")
}

///|
test "fibonacci" {
  inspect(@exemplo_moonbit.fib(10), content="89")
}
