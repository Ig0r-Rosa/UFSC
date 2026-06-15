# Tabela de símbolos — estrutura fundamental da análise semântica (Compiladores)
# Representa o escopo léxico: mapeia identificadores a atributos (tipo, linha).
# Feito por: Igor de Matos da Rosa - 20103930


class TabelaSimbolos:
    """
    Implementa escopos aninhados por pilha de dicionários.

    Conceito teórico: cada bloco { } em C abre um novo escopo; a busca
    percorre do escopo interno para o externo (regra de resolução de nomes).
    """

    def __init__(self):
        self._escopos = [{}]
        self._historico = []

    def entrar_escopo(self):
        """Abre escopo ao entrar em um bloco composto."""
        self._escopos.append({})

    def sair_escopo(self):
        """Fecha o escopo mais interno ao sair do bloco."""
        if len(self._escopos) > 1:
            self._escopos.pop()

    def declarar(self, nome, tipo, linha):
        """
        Insere símbolo no escopo atual.
        Retorna False se o identificador já existir (redeclaração).
        """
        escopo_atual = self._escopos[-1]
        if nome in escopo_atual:
            return False
        escopo = len(self._escopos)
        entrada = {"tipo": tipo, "linha": linha, "escopo": escopo}
        escopo_atual[nome] = entrada
        self._historico.append({"nome": nome, **entrada})
        return True

    def buscar(self, nome):
        """
        Consulta o identificador do escopo interno para o externo.
        Retorna None quando a variável não foi declarada.
        """
        for escopo in reversed(self._escopos):
            if nome in escopo:
                return escopo[nome]
        return None

    def limpar(self):
        """Reinicia a tabela para uma nova análise."""
        self._escopos = [{}]
        self._historico = []

    def obter_historico(self):
        """Retorna todas as declarações registradas durante a análise."""
        return list(self._historico)
