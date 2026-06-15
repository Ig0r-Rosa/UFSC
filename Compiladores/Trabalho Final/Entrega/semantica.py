# Ações semânticas — verificação de tipos e consistência (análise semântica)
# Feito por: Igor de Matos da Rosa - 20103930

# Tipos aceitos pelo subconjunto da linguagem
TIPOS_PRIMITIVOS = {"int", "float", "double", "char", "string"}

# Tipos que participam de operações aritméticas e relacionais
TIPOS_NUMERICOS = {"int", "float", "double", "char"}

# Mapeamento token léxico -> tipo semântico
TIPO_POR_TOKEN = {
    "INT": "int",
    "FLOAT": "float",
    "DOUBLE": "double",
    "CHAR": "char",
}


class AnalisadorSemantico:
    """
    Concentra as ações semânticas exigidas pelo trabalho final:
    1) registro de declarações na tabela de símbolos;
    2) verificação de uso de variável declarada;
    3) verificação de compatibilidade de tipos em expressões e atribuições;
    4) validação de condições em estruturas de controle.
    """

    def __init__(self, tabela, relatorio=None):
        self.tabela = tabela
        self.relatorio = relatorio
        self.erros = []

    def limpar_erros(self):
        """Zera a lista de erros antes de uma nova compilação."""
        self.erros = []

    def registrar_erro(self, mensagem, linha=None):
        """Acumula diagnósticos semânticos com referência de linha."""
        if linha is not None:
            self.erros.append(f"Erro semântico na linha {linha}: {mensagem}")
        else:
            self.erros.append(f"Erro semântico: {mensagem}")

    def tipo_de_token(self, token_tipo):
        """Converte o terminal da gramática (ex.: INT) em tipo semântico."""
        return TIPO_POR_TOKEN.get(token_tipo)

    def declarar_variavel(self, nome, tipo, linha):
        """
        Ação semântica de declaração: insere o identificador no escopo.
        Detecta redeclaração no mesmo bloco (violação de escopo).
        """
        if not self.tabela.declarar(nome, tipo, linha):
            self.registrar_erro(
                f"redeclaração da variável '{nome}' no mesmo escopo", linha
            )
            return
        if self.relatorio:
            info = self.tabela.buscar(nome)
            self.relatorio.registrar_declaracao(
                nome, tipo, linha, info["escopo"] if info else 0
            )
            self.relatorio.registrar_acao_semantica(
                f"declaração de '{nome}' como {tipo} (linha {linha})"
            )

    def registrar_uso_variavel(self, nome, tipo, linha):
        """Registra referência válida a variável declarada."""
        if self.relatorio:
            self.relatorio.registrar_acao_semantica(
                f"uso de '{nome}' validado (tipo {tipo}, linha {linha})"
            )

    def verificar_uso(self, nome, linha):
        """
        Ação semântica de referência: toda variável usada deve estar declarada.
        Retorna o tipo associado ou 'erro' quando o identificador é inválido.
        """
        info = self.tabela.buscar(nome)
        if info is None:
            self.registrar_erro(
                f"variável '{nome}' utilizada sem declaração prévia", linha
            )
            return "erro"
        self.registrar_uso_variavel(nome, info["tipo"], linha)
        return info["tipo"]

    def tipos_compativeis_atribuicao(self, tipo_destino, tipo_origem):
        """
        Verifica se o tipo da expressão pode ser atribuído à variável.
        Permite promoção numérica (int -> float/double) conforme regras de C.
        """
        if tipo_destino == "erro" or tipo_origem == "erro":
            return False
        if tipo_destino == tipo_origem:
            return True
        if tipo_destino in TIPOS_NUMERICOS and tipo_origem in TIPOS_NUMERICOS:
            ordem = {"char": 0, "int": 1, "float": 2, "double": 3}
            return ordem.get(tipo_origem, -1) <= ordem.get(tipo_destino, -1)
        return False

    def verificar_atribuicao(self, nome, tipo_expr, linha):
        """Valida atribuição: variável declarada e tipos compatíveis."""
        tipo_var = self.verificar_uso(nome, linha)
        if tipo_var == "erro":
            return
        if not self.tipos_compativeis_atribuicao(tipo_var, tipo_expr):
            self.registrar_erro(
                f"atribuição inválida: '{nome}' é {tipo_var}, "
                f"mas a expressão é {tipo_expr}",
                linha,
            )
            return
        if self.relatorio:
            self.relatorio.registrar_acao_semantica(
                f"atribuição a '{nome}' validada ({tipo_var} = {tipo_expr})"
            )

    def tipo_literal(self, token_type):
        """Infere o tipo semântico de literais reconhecidos pelo léxico."""
        mapa = {
            "INTEGER": "int",
            "FLOAT_N": "float",
            "STRING": "string",
            "CHARACTER": "char",
        }
        return mapa.get(token_type, "erro")

    def tipo_resultante_binario(self, operador, tipo_esq, tipo_dir, linha):
        """
        Calcula o tipo de expressões aritméticas (+, -, *, /, ^).
        Operadores relacionais sempre produzem 'int' (0 ou 1) em C.
        """
        if tipo_esq == "erro" or tipo_dir == "erro":
            return "erro"
        if operador in ("<", "<=", ">", ">=", "==", "!="):
            if tipo_esq not in TIPOS_NUMERICOS or tipo_dir not in TIPOS_NUMERICOS:
                self.registrar_erro(
                    f"operador relacional '{operador}' exige operandos numéricos "
                    f"({tipo_esq} e {tipo_dir})",
                    linha,
                )
                return "erro"
            return "int"
        if tipo_esq == "string" or tipo_dir == "string":
            if operador == "+":
                return "string"
            self.registrar_erro(
                f"operação '{operador}' inválida entre {tipo_esq} e {tipo_dir}",
                linha,
            )
            return "erro"
        if tipo_esq not in TIPOS_NUMERICOS or tipo_dir not in TIPOS_NUMERICOS:
            self.registrar_erro(
                f"operação '{operador}' inválida entre {tipo_esq} e {tipo_dir}",
                linha,
            )
            return "erro"
        if operador in ("+", "-", "*", "/", "^"):
            ordem = {"char": 0, "int": 1, "float": 2, "double": 3}
            maior = max(tipo_esq, tipo_dir, key=lambda t: ordem.get(t, -1))
            return maior
        return "erro"

    def verificar_condicao(self, tipo_expr, linha):
        """
        Em if/while/for a condição deve ser expressão numérica ou relacional.
        Strings não são válidas como condição neste subconjunto.
        """
        if tipo_expr == "erro":
            return
        if tipo_expr not in TIPOS_NUMERICOS:
            self.registrar_erro(
                f"condição deve ser numérica, encontrado tipo '{tipo_expr}'",
                linha,
            )
            return
        if self.relatorio:
            self.relatorio.registrar_acao_semantica(
                f"condição validada (tipo {tipo_expr}, linha {linha})"
            )

    def no_tipo(self, no):
        """Extrai o tipo sintetizado de um nó da árvore atribuída."""
        if no is None:
            return "erro"
        if isinstance(no, tuple) and len(no) >= 1:
            return no[0]
        if isinstance(no, str):
            return self.tipo_literal(no) if no in TIPO_POR_TOKEN else no
        return "erro"
