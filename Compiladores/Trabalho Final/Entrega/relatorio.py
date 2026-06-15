# Relatório final da compilação — consolidação das três fases analíticas
# Feito por: Igor de Matos da Rosa - 20103930


class RelatorioCompilacao:
    """
    Agrega os resultados das fases léxica, sintática e semântica
    e gera um relatório textual ao término da análise.
    """

    def __init__(self):
        self.arquivo = ""
        self.fase = "completa"
        self.tokens = []
        self.erros_lexicos = []
        self.eventos_sintaticos = []
        self.erros_sintaticos = []
        self.declaracoes = []
        self.acoes_semanticas = []
        self.erros_semanticos = []

    def limpar(self):
        """Reinicia o relatório para uma nova compilação."""
        self.arquivo = ""
        self.fase = "completa"
        self.tokens = []
        self.erros_lexicos = []
        self.eventos_sintaticos = []
        self.erros_sintaticos = []
        self.declaracoes = []
        self.acoes_semanticas = []
        self.erros_semanticos = []

    def registrar_token(self, token):
        """Armazena um token reconhecido na fase léxica."""
        self.tokens.append(token)

    def registrar_erro_lexico(self, mensagem):
        """Registra falha na tokenização."""
        self.erros_lexicos.append(mensagem)

    def registrar_sintaxe(self, mensagem):
        """Registra estrutura reconhecida pelo parser."""
        self.eventos_sintaticos.append(mensagem)

    def registrar_declaracao(self, nome, tipo, linha, escopo):
        """Registra símbolo inserido na tabela na fase semântica."""
        self.declaracoes.append(
            {"nome": nome, "tipo": tipo, "linha": linha, "escopo": escopo}
        )

    def registrar_acao_semantica(self, mensagem):
        """Registra verificação semântica bem-sucedida."""
        self.acoes_semanticas.append(mensagem)

    def _linha(self, texto="", char="="):
        return char * 78 + ("\n" + texto if texto else "") + "\n"

    def _secao_lexica(self):
        linhas = [
            self._linha("1. ANÁLISE LÉXICA", "-"),
            "Conceito: o analisador léxico (autômato finito) agrupa caracteres",
            "em tokens — unidades mínimas com significado para o parser.",
            "",
            f"Total de tokens reconhecidos: {len(self.tokens)}",
            "",
        ]
        if self.tokens:
            linhas.append(f"{'Linha':<6} {'Token':<14} {'Valor'}")
            linhas.append("-" * 78)
            for tok in self.tokens:
                linhas.append(f"{tok.lineno:<6} {tok.type:<14} {tok.value!r}")
        else:
            linhas.append("(nenhum token reconhecido)")

        linhas.append("")
        if self.erros_lexicos:
            linhas.append("Erros léxicos:")
            linhas.extend(f"  - {e}" for e in self.erros_lexicos)
            linhas.append("Status: FALHA")
        else:
            linhas.append("Status: SUCESSO — fluxo de entrada tokenizado.")
        return "\n".join(linhas)

    def _secao_sintatica(self):
        linhas = [
            self._linha("2. ANÁLISE SINTÁTICA", "-"),
            "Conceito: o parser LALR(1) aplica as produções da gramática",
            "para validar a estrutura hierárquica do programa.",
            "",
            "Estruturas reconhecidas:",
        ]
        if self.eventos_sintaticos:
            linhas.extend(f"  - {e}" for e in self.eventos_sintaticos)
        else:
            linhas.append("  (nenhuma estrutura registrada)")

        linhas.append("")
        if self.erros_sintaticos:
            linhas.append("Erros sintáticos:")
            linhas.extend(f"  - {e}" for e in self.erros_sintaticos)
            linhas.append("Status: FALHA")
        else:
            linhas.append("Status: SUCESSO — programa reconhecido pela gramática.")
        return "\n".join(linhas)

    def _secao_semantica(self):
        linhas = [
            self._linha("3. ANÁLISE SEMÂNTICA", "-"),
            "Conceito: verifica regras de contexto — declaração antes do uso,",
            "compatibilidade de tipos e validade de condições de controle.",
            "",
            "Tabela de símbolos (declarações registradas):",
        ]
        if self.declaracoes:
            linhas.append(f"  {'Nome':<12} {'Tipo':<8} {'Linha':<6} Escopo")
            linhas.append("  " + "-" * 40)
            for item in self.declaracoes:
                linhas.append(
                    f"  {item['nome']:<12} {item['tipo']:<8} "
                    f"{item['linha']:<6} {item['escopo']}"
                )
        else:
            linhas.append("  (nenhuma declaração registrada)")

        linhas.extend(["", "Ações semânticas executadas:"])
        if self.acoes_semanticas:
            linhas.extend(f"  - {a}" for a in self.acoes_semanticas)
        else:
            linhas.append("  (nenhuma ação registrada)")

        linhas.append("")
        if self.erros_semanticos:
            linhas.append("Erros semânticos:")
            linhas.extend(f"  - {e}" for e in self.erros_semanticos)
            linhas.append("Status: FALHA")
        else:
            linhas.append("Status: SUCESSO — programa semanticamente válido.")
        return "\n".join(linhas)

    def _resultado_final(self):
        falhou = (
            self.erros_lexicos
            or self.erros_sintaticos
            or self.erros_semanticos
        )
        status = "INVÁLIDO" if falhou else "VÁLIDO"
        return (
            self._linha("RESULTADO FINAL", "=")
            + f"Arquivo analisado: {self.arquivo}\n"
            f"Compilação parcial: {status}\n"
            + self._linha("", "=")
        )

    def gerar(self):
        """Monta o relatório completo conforme a fase executada."""
        partes = [
            self._linha("", "="),
            "RELATÓRIO DE COMPILAÇÃO — DEC0004-09655 (20261) Compiladores",
            self._linha("", "="),
            f"Arquivo: {self.arquivo}",
            f"Fase solicitada: {self._nome_fase()}",
            "",
        ]

        partes.append(self._secao_lexica())
        if self.fase in ("sint", "completa"):
            partes.extend(["", self._secao_sintatica()])
        if self.fase == "completa":
            partes.extend(["", self._secao_semantica()])

        partes.extend(["", self._resultado_final()])
        return "\n".join(partes)

    def _nome_fase(self):
        nomes = {
            "lex": "somente léxica",
            "sint": "léxica e sintática",
            "completa": "léxica, sintática e semântica",
        }
        return nomes.get(self.fase, self.fase)

    def exibir(self):
        """Imprime o relatório consolidado na saída padrão."""
        print(self.gerar())
