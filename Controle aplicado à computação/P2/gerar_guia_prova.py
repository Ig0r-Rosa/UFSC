#!/usr/bin/env python3
"""PDF modo gorila — sem frescura, só o que colar na prova."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "/home/igor/Documentos/UFSC/Git/Controle aplicado à computação/P2/GUIA_PROVA_UN5_UN6.pdf"


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("T", parent=s["Title"], fontSize=22, alignment=TA_CENTER,
                         textColor=colors.HexColor("#1a365d"), spaceAfter=10))
    s.add(ParagraphStyle("H", parent=s["Heading1"], fontSize=15, spaceBefore=12, spaceAfter=6,
                         textColor=colors.HexColor("#c53030"), fontName="Helvetica-Bold"))
    s.add(ParagraphStyle("H2", parent=s["Heading2"], fontSize=12, spaceBefore=8, spaceAfter=4,
                         textColor=colors.HexColor("#2b6cb0"), fontName="Helvetica-Bold"))
    s.add(ParagraphStyle("P", parent=s["Normal"], fontSize=11, leading=15, spaceAfter=5))
    s.add(ParagraphStyle("BIG", parent=s["Normal"], fontSize=13, leading=18, spaceAfter=6,
                          backColor=colors.HexColor("#ffffcc"), borderPadding=8))
    s.add(ParagraphStyle("STEP", parent=s["Normal"], fontSize=11, leading=16, leftIndent=8,
                         spaceAfter=4, backColor=colors.HexColor("#e6fffa")))
    s.add(ParagraphStyle("WARN", parent=s["Normal"], fontSize=11, leading=15,
                         textColor=colors.HexColor("#c53030"), backColor=colors.HexColor("#fff5f5"),
                         borderPadding=6, spaceAfter=6))
    return s


def tbl(data, widths=None, big=False, header=True):
    fs = 11 if big else 10
    t = Table(data, colWidths=widths, hAlign="LEFT")
    style = [
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), fs),
        ("GRID", (0, 0), (-1, -1), 0.8, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    if header:
        style.extend([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2b6cb0")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ])
    t.setStyle(TableStyle(style))
    return t


def questao(st, s, num, titulo, enunciado, linhas, resposta):
    """Bloco padrão: enunciado + tabela passo a passo + gabarito."""
    st.append(Paragraph(f"QUESTÃO {num} — {titulo}", s["H"]))
    st.append(Paragraph(f"<b>Enunciado:</b> {enunciado}", s["P"]))
    st.append(tbl([["Passo", "O que você faz", "Resultado"]] + linhas,
                  [1.2 * cm, 6.3 * cm, 7.5 * cm]))
    st.append(Paragraph(f"<b>Gabarito:</b> {resposta}", s["BIG"]))
    st.append(Spacer(1, 0.25 * cm))


def questoes_completas(st, s):
    st.append(PageBreak())
    st.append(Paragraph("QUESTÕES COMPLETAS — UMA DE CADA", s["T"]))
    st.append(Paragraph(
        "Cada questão = um tipo que pode cair. Leia o enunciado, tente sozinho, depois confere o passo a passo.",
        s["P"],
    ))
    st.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#2b6cb0")))
    st.append(Spacer(1, 0.2 * cm))

    # Q1 — Análise LR (ângulo + K)
    questao(st, s, 1,
            "Análise do LR — ponto está no lugar das raízes?",
            "Malha fechada com G(s) = (s+1)/(s+2), H(s)=1, controlador C(s)=K. "
            "Existe K para ter um polo em p = −3/2?",
            [
                ["1", "Ache polos e zeros de malha aberta", "Zero em −1 (○) · Polo em −2 (×)"],
                ["2", "p = −1,5 está no eixo real, entre −1 e −2", "Use o atalho do eixo real"],
                ["3", "Zero −1 está à DIREITA de p", "Conta 180°"],
                ["4", "Polo −2 está à DIREITA de p", "Conta 0°"],
                ["5", "∠GH = 180° − 0° = 180°", "Condição de ângulo OK ✓"],
                ["6", "K = distância p→polo / distância p→zero", "K = |−1,5+2| / |−1,5+1| = 0,5/0,5"],
            ],
            "SIM. K = 1. (Se fosse p = −1+j, daria 45° → NÃO existe K.)")

    # Q2 — Análise LR complexo
    questao(st, s, 2,
            "Análise do LR — ponto complexo",
            "G(s) = K/[s(s+4)], H=1. Existe K para polo em p = −2 + j2?",
            [
                ["1", "Polos em 0 e −4. Sem zeros", "Marque no plano s"],
                ["2", "Ângulo do polo em 0 até p", "Vetor −2+j2 → 180°−45° = 135°"],
                ["3", "Ângulo do polo em −4 até p", "Vetor 2+j2 → arctan(2/2) = 45°"],
                ["4", "∠GH = 0° − 135° − 45°", "−180° = 180° (mod 360°) ✓"],
                ["5", "Distância p até 0", "|p| = √(4+4) = √8"],
                ["6", "Distância p até −4", "|p+4| = √(4+4) = √20"],
                ["7", "K = √8 · √20", "K = √160 ≈ 12,65"],
            ],
            "SIM. K ≈ 12,65.")

    st.append(PageBreak())

    # Q3 — Traçado LR
    questao(st, s, 3,
            "Traçado do LR — desenhar",
            "G(s)H(s) = K/[s(s+2)(s+4)]. Esboce o lugar das raízes.",
            [
                ["1", "Marque polos em 0, −2 e −4", "3 polos, 0 zeros"],
                ["2", "K=0: LR começa nos polos", "3 ramos saem de 0, −2, −4"],
                ["3", "K→∞: sem zeros → vão pro ∞", "3 ramos ao infinito"],
                ["4", "Eixo real: ímpar à esquerda?", "(−∞,−4): 3 à direita → SIM"],
                ["5", "Eixo real: entre −4 e −2", "2 à direita → NÃO"],
                ["6", "Eixo real: entre −2 e 0", "1 à direita → SIM"],
                ["7", "Centroide assíntotas", "σa = (0−2−4)/3 = −2"],
                ["8", "Ângulos das assíntotas", "60°, 180°, 300°"],
                ["9", "Desenhe simétrico", "Parte de cima = espelho de baixo"],
            ],
            "LR no eixo real em (−∞, −4) e (−2, 0). Dois ramos complexos + um no eixo.")

    # Q4 — Projeto Mp e Ts
    questao(st, s, 4,
            "Projeto pelo LR — Mp e Ts",
            "G(s) = 4/[s(s+2)], malha fechada com C(s)=K. Quer Mp ≤ 10% e Ts ≤ 1 s. "
            "Como escolher o polo dominante?",
            [
                ["1", "Mp ≤ 10% → tabela", "ζ ≥ 0,6"],
                ["2", "Ts ≤ 1 s → σ = 4/Ts", "σ ≥ 4 → Re(s) ≤ −4"],
                ["3", "Região boa no plano s", "À esquerda de −4, dentro do cone ζ=0,6"],
                ["4", "Escolha p na região (exemplo)", "p = −4 + j5,3 (ζ≈0,6)"],
                ["5", "Verifique se p está no LR", "Use ângulo = 180°"],
                ["6", "Se OK, calcule K", "Condição de módulo com distâncias"],
                ["7", "Se p NÃO está no LR", "Precisa compensador lead ou PID"],
            ],
            "Primeiro traduz specs em desenho (cone + linha vertical). Depois escolhe p na interseção com o LR.")

    st.append(PageBreak())

    # Q5 — Compensador Lead
    questao(st, s, 5,
            "Compensador LEAD (avanço de fase)",
            "Planta G(s) = 1/(s+1). Só ganho K não coloca polo onde você quer. "
            "Precisa lead Gc = K(s+z)/(s+p) com z < p. Polo desejado p₀ = −3 + j3.",
            [
                ["1", "Esboce LR só com K", "Vê que p₀ não está no LR"],
                ["2", "Coloque ZERO do lead embaixo de p₀", "z ≈ 3 (zero em −3)"],
                ["3", "Calcule ângulo que falta em p₀", "Some todos os ângulos → deve dar 180°"],
                ["4", "Posicione POLO do lead para fechar 180°", "Polo mais à esquerda que o zero"],
                ["5", "Condição de módulo em p₀", "Ache K final"],
                ["6", "Lead puxa LR pra esquerda", "Resposta mais rápida e estável"],
            ],
            "Lead = zero perto do ponto desejado + polo calculado pro ângulo fechar 180°.")

    # Q6 — Compensador Lag
    questao(st, s, 6,
            "Compensador LAG (atraso de fase)",
            "Sistema já tem transient bom com lead, mas erro estacionário alto. "
            "Quer reduzir erro sem estragar a resposta.",
            [
                ["1", "Transient já OK?", "Sim → não mexe nos polos dominantes"],
                ["2", "Calcule erro atual (ess ou Kv)", "Anote o valor"],
                ["3", "Compare com erro desejado", "Razão = ess_atual / ess_desejado"],
                ["4", "Lag: razão = z/p do compensador", "z > p (zero mais à direita)"],
                ["5", "Coloque z e p JUNTINHOS perto de 0", "Ângulo em p₀ < 5° (quase não muda LR)"],
                ["6", "Confirme LR ainda passa por p₀", "Transient continua bom"],
            ],
            "Lag = aumenta ganho estático. z e p colados perto da origem.")

    st.append(PageBreak())

    # Q7 — PID pelo LR
    questao(st, s, 7,
            "PID pelo Lugar das Raízes",
            "G(s) = 1/(s+1), realimentação unitária. Quer 0,5 ≤ ζ ≤ 0,75 e 0,5 s ≤ Ts ≤ 1 s. "
            "Use GPID = K(s+a+jb)(s+a−jb)/s.",
            [
                ["1", "Ts ≤ 0,5 → σ = 4/0,5 = 8", "Re(s) entre −8 e −4"],
                ["2", "ζ entre 0,5 e 0,75", "Região em forma de cone no plano s"],
                ["3", "Escolha p na região (slide)", "p = −6 + j6"],
                ["4", "Condição de ângulo com zeros −a±jb", "Chute a = 12, ache b = 2,55"],
                ["5", "Zeros ficam em −10 ± j2,55", "Dois zeros do PID"],
                ["6", "Condição de módulo em p", "K = 0,917"],
                ["7", "I (polo em 0) zera erro estacionário", "Bônus do PID"],
            ],
            "Zeros em −10±j2,55 · K = 0,917 · (valores do slide do professor).")

    # Q8 — ZN malha fechada
    questao(st, s, 8,
            "Sintonia PID — Ziegler-Nichols MALHA FECHADA",
            "G(s) = 20/[(s+1)(s+2)(s+5)]. Com Ki=0 e Kd=0, subiu Kp até oscilar sem parar. "
            "Mediu KC = 6,3 e TC = 1,52 s. Ache Kp, Ki, Kd do PID.",
            [
                ["1", "Anote KC e TC do experimento", "KC=6,3 · TC=1,52"],
                ["2", "Abra tabela ZN fechada (PID)", "Não confunda com malha aberta!"],
                ["3", "Kp = 0,6 · KC", "0,6 × 6,3 = 3,78"],
                ["4", "Ki = 1,2 · KC / TC", "1,2 × 6,3 / 1,52 = 4,97"],
                ["5", "Kd = 0,6 · KC · TC / 8", "0,6 × 6,3 × 1,52 / 8 = 0,72"],
                ["6", "Ajuste fino se precisar", "Mais Kd = menos overshoot"],
            ],
            "Kp = 3,78 · Ki = 4,97 · Kd = 0,72.")

    st.append(PageBreak())

    # Q9 — ZN malha aberta
    questao(st, s, 9,
            "Sintonia PID — Ziegler-Nichols MALHA ABERTA",
            "Mesma planta. Deu degrau e mediu no gráfico: K=2, T=2,11 s, L=0,36 s. "
            "Ache Kp, Ki, Kd do PID.",
            [
                ["1", "K = valor final / degrau", "Ganho estacionário = 2"],
                ["2", "T = distância horizontal na tangente", "Constante de tempo = 2,11 s"],
                ["3", "L = atraso até tangente cruzar eixo", "Tempo morto = 0,36 s"],
                ["4", "Abra tabela ZN aberta (PID)", "Fórmulas usam K, T, L"],
                ["5", "Kp = 1,2 · T / (K·L)", "1,2 × 2,11 / (2 × 0,36) = 3,5"],
                ["6", "Ki = 0,6 · T / (K·L²)", "0,6 × 2,11 / (2 × 0,36²) = 4,9"],
                ["7", "Kd = 0,6 · T / K", "0,6 × 2,11 / 2 = 0,63"],
            ],
            "Kp = 3,5 · Ki = 4,9 · Kd = 0,63.")

    # Q10 — PI e erro estacionário
    questao(st, s, 10,
            "PI — erro estacionário zero",
            "G(s) = 5/(s+3), degrau na referência. Por que só P não zera o erro? O que fazer?",
            [
                ["1", "Só P → sistema tipo 0 com degrau", "Erro estacionário ≠ 0"],
                ["2", "Adicionar I = Ki/s", "Coloca polo em 0 no controlador"],
                ["3", "Polo em 0 → tipo aumenta", "Sistema passa a ter integrador"],
                ["4", "Com PI, erro de degrau vai a zero", "Ki elimina erro final"],
                ["5", "Comece com ZN ou chute Kp, depois Ki", "Ki demais = lento e oscila"],
            ],
            "Erro zero → precisa I (PI ou PID). P sozinho não resolve.")

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("MAPA RÁPIDO — QUAL QUESTÃO ESTUDAR?", s["H2"]))
    st.append(tbl([
        ["Conteúdo da prova", "Questão #"],
        ["Ponto no LR? / calcular K", "Q1 e Q2"],
        ["Desenhar / traçar LR", "Q3"],
        ["Mp, Ts, escolher polo", "Q4"],
        ["Compensador lead", "Q5"],
        ["Compensador lag", "Q6"],
        ["PID pelo LR", "Q7"],
        ["ZN malha fechada", "Q8"],
        ["ZN malha aberta", "Q9"],
        ["Erro estacionário / PI", "Q10"],
    ], [10 * cm, 5 * cm], big=True))


def story(s):
    st = []

    st.append(Paragraph("GUIA MODO GORILA", s["T"]))
    st.append(Paragraph("Lugar das Raízes + PID · Prova amanhã · Não pense, siga o roteiro", s["P"]))
    st.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#c53030")))
    st.append(Spacer(1, 0.2 * cm))

    # PÁGINA 1 — O MÍNIMO
    st.append(Paragraph("O QUE É ISSO? (30 segundos)", s["H"]))
    st.append(Paragraph(
        "Você tem um sistema (planta). Quer que ele responda do jeito certo.<br/>"
        "O <b>Lugar das Raízes (LR)</b> = desenho de onde os polos vão parar quando você aumenta o ganho K.<br/>"
        "O <b>PID</b> = 3 botões (P, I, D) pra ajustar o sistema sem entender física.",
        s["P"],
    ))

    st.append(Paragraph("SÓ 3 COISAS PRA DECORAR", s["H2"]))
    st.append(tbl([
        ["#", "Frase burra", "Pra quê"],
        ["1", "Ângulo = 180°?", "Ponto tá no LR?"],
        ["2", "Mp → ζ na tabela", "Saber se oscila demais"],
        ["3", "Ts → linha vertical em −4/Ts", "Saber se demora demais"],
    ], [1 * cm, 7 * cm, 7 * cm]))

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("TABELA Mp → ζ (DECORE OU COPIE)", s["H2"]))
    st.append(tbl([
        ["Mp pedido", "ζ"],
        ["5%", "0,7"],
        ["10%", "0,6"],
        ["15%", "0,5"],
        ["16%", "0,5"],
        ["20%", "0,45"],
    ], [4 * cm, 4 * cm], big=True))

    st.append(Spacer(1, 0.2 * cm))
    st.append(Paragraph(
        "<b>Ts (tempo de acomodação):</b> Re(s) do polo = −4/Ts<br/>"
        "Ex: Ts &lt; 2s → polo tem que estar à esquerda de −2 no plano s",
        s["BIG"],
    ))

    st.append(PageBreak())

    # PÁGINA 2 — RECEITA LR
    st.append(Paragraph("RECEITA 1 — “EXISTE K PRA POLO EM p?”", s["H"]))
    st.append(Paragraph("Faça EXATAMENTE nesta ordem. Não inverta.", s["WARN"]))

    steps = [
        "<b>1.</b> Marque no desenho: × = polo, ○ = zero",
        "<b>2.</b> Trace uma seta de cada polo/zero até o ponto p",
        "<b>3.</b> Some os ângulos dos ZEROS, subtraia os ângulos dos POLOS",
        "<b>4.</b> Deu 180° (ou 540°, 900°...)? → SIM, existe K. Vai pro passo 5",
        "<b>5.</b> Não deu 180°? → PARA. Resposta = NÃO. Não calcule K.",
        "<b>6.</b> Se SIM: K = (multiplica distâncias p→polos) ÷ (multiplica distâncias p→zeros)",
    ]
    for step in steps:
        st.append(Paragraph(step, s["STEP"]))

    st.append(Spacer(1, 0.2 * cm))
    st.append(Paragraph("ATALHO NO EIXO REAL (só quando p é número real)", s["H2"]))
    st.append(Paragraph(
        "Elemento à <b>DIREITA</b> de p → conta 180°<br/>"
        "Elemento à <b>ESQUERDA</b> de p → conta 0°<br/>"
        "Tem que dar 180° no final.",
        s["BIG"],
    ))

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("EXEMPLO A — NÃO (do slide)", s["H2"]))
    st.append(tbl([
        ["Dado", "Valor"],
        ["G(s)", "(s+1)/(s+2)"],
        ["p", "−1 + j"],
        ["Ângulo zero (−1)", "90°"],
        ["Ângulo polo (−2)", "45°"],
        ["Total", "90° − 45° = 45° ≠ 180°"],
        ["Resposta", "NÃO existe K"],
    ], [5 * cm, 10 * cm]))

    st.append(Spacer(1, 0.2 * cm))
    st.append(Paragraph("EXEMPLO B — SIM (do slide)", s["H2"]))
    st.append(tbl([
        ["Dado", "Valor"],
        ["p", "−1,5 (no eixo real)"],
        ["Zero −1 à direita", "180°"],
        ["Polo −2 à direita", "0°"],
        ["Total", "180° ✓"],
        ["K", "|−1,5+2| / |−1,5+1| = 0,5/0,5 = 1"],
        ["Resposta", "SIM, K = 1"],
    ], [5 * cm, 10 * cm]))

    st.append(PageBreak())

    # PÁGINA 3 — DESENHAR LR
    st.append(Paragraph("RECEITA 2 — “DESENHE O LR”", s["H"]))
    st.append(tbl([
        ["Passo", "O que fazer"],
        ["1", "Marque polos (×) e zeros (○)"],
        ["2", "K=0: LR COMEÇA nos polos"],
        ["3", "K→∞: LR TERMINA nos zeros (ou vai pro infinito)"],
        ["4", "No eixo real: LR fica à ESQUERDA de ímpar par de polos+zeros"],
        ["5", "Desenho é SIMÉTRICO em cima/baixo do eixo real"],
    ], [1.5 * cm, 13.5 * cm]))

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("RECEITA 3 — “PROJETO COM Mp E Ts”", s["H"]))
    st.append(tbl([
        ["Passo", "O que fazer"],
        ["1", "Mp → olha tabela → acha ζ"],
        ["2", "Ts → calcula −4/Ts → risca linha vertical"],
        ["3", "Desenha o cone do ζ (região boa no plano s)"],
        ["4", "Onde região boa cruza o LR → escolhe um ponto p"],
        ["5", "Calcula K com distâncias (receita 1, passo 6)"],
        ["6", "Só K não resolve? → compensador ou PID"],
    ], [1.5 * cm, 13.5 * cm]))

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("SE PEDIREM COMPENSADOR", s["H2"]))
    st.append(tbl([
        ["Tipo", "Pra que", "Lembra assim"],
        ["Lead (avanço)", "Melhorar resposta rápida", "Puxa LR pra esquerda = mais estável"],
        ["Lag (atraso)", "Diminuir erro final", "Polo e zero juntinhos perto do zero"],
    ], [3 * cm, 5 * cm, 7 * cm]))

    st.append(PageBreak())

    # PÁGINA 4 — PID
    st.append(Paragraph("RECEITA 4 — PID (O QUE CADA BOTÃO FAZ)", s["H"]))
    st.append(tbl([
        ["Botão", "Faz o quê", "Quando o prof pede"],
        ["P (Kp)", "Erro grande → manda mais", "Sempre"],
        ["I (Ki)", "Erro que não some → força mais", "“Erro estacionário zero”"],
        ["D (Kd)", "Erro subindo rápido → freia", "“Menos sobressinal”"],
    ], [2.5 * cm, 6 * cm, 6.5 * cm]))

    st.append(Spacer(1, 0.2 * cm))
    st.append(Paragraph(
        "Fórmula: C(s) = Kp + Ki/s + Kd·s<br/>"
        "PI = sem D · PD = sem I · PID = os 3",
        s["BIG"],
    ))

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("RECEITA 5 — ZIEGLER-NICHOLS (COPIA A TABELA)", s["H"]))
    st.append(Paragraph("<b>Método A — Malha FECHADA</b> (oscila e não para)", s["H2"]))
    st.append(Paragraph("1) Ki=0, Kd=0 · 2) Sobe Kp até oscilar · 3) Anota KC e TC", s["P"]))
    st.append(tbl([
        ["", "Kp", "Ki", "Kd"],
        ["P", "0,5·KC", "0", "0"],
        ["PI", "0,45·KC", "0,54·KC/TC", "0"],
        ["PID", "0,6·KC", "1,2·KC/TC", "0,6·KC·TC/8"],
    ], [2 * cm, 3.5 * cm, 4 * cm, 3.5 * cm], big=True))

    st.append(Spacer(1, 0.2 * cm))
    st.append(Paragraph("<b>Exemplo slide:</b> KC=6,3, TC=1,52 → Kp=3,78, Ki=4,97, Kd=0,72", s["STEP"]))

    st.append(Spacer(1, 0.3 * cm))
    st.append(Paragraph("<b>Método B — Malha ABERTA</b> (degrau na planta)", s["H2"]))
    st.append(Paragraph("Acha K, T, L no gráfico da resposta ao degrau (curva em S)", s["P"]))
    st.append(tbl([
        ["", "Kp", "Ki", "Kd"],
        ["P", "T/(K·L)", "0", "0"],
        ["PI", "0,9·T/(K·L)", "0,27·T/(K·L²)", "0"],
        ["PID", "1,2·T/(K·L)", "0,6·T/(K·L²)", "0,6·T/K"],
    ], [2 * cm, 3.5 * cm, 4 * cm, 3.5 * cm], big=True))

    st.append(Paragraph("<b>Exemplo slide:</b> K=2, T=2,11, L=0,36 → Kp=3,5, Ki=4,9, Kd=0,63", s["STEP"]))

    st.append(PageBreak())

    # PÁGINA 5 — DECISÃO + QUESTÃO
    st.append(Paragraph("QUAL RECEITA USAR? (COLA ISSO)", s["H"]))
    st.append(tbl([
        ["A prova pergunta...", "Abre a receita..."],
        ["Existe K para polo em p?", "RECEITA 1"],
        ["Desenhe / trace o LR", "RECEITA 2"],
        ["Mp e Ts / projeto", "RECEITA 3"],
        ["Compensador lead ou lag", "Tabela compensador (pág. 3)"],
        ["Sintonize PID / Ziegler", "RECEITA 5"],
        ["Erro estacionário zero", "Precisa I (PI ou PID)"],
    ], [6.5 * cm, 8.5 * cm], big=True))

    st.append(Spacer(1, 0.4 * cm))
    st.append(Paragraph("QUESTÃO PRONTA — COPIA O RACIOCÍNIO", s["H"]))
    st.append(Paragraph("G(s) = K / [s(s+4)]. Ponto p = −2 + j2.", s["P"]))

    st.append(tbl([
        ["Pergunta", "Resposta pronta"],
        ["(a) p tá no LR?", "Ângulo polo 0: 135°. Polo −4: 45°. Total −180° = 180° → SIM"],
        ["(b) Quanto é K?", "K = √8 · √20 = √160 ≈ 12,65"],
        ["(c) Mp=16%, Ts?", "ζ≈0,5. σ=2 → Ts≈4/2=2s"],
    ], [4 * cm, 11 * cm]))

    st.append(Spacer(1, 0.4 * cm))
    st.append(Paragraph("NÃO FAÇA ISSO (PERDE PONTO)", s["H"]))
    st.append(tbl([
        ["Erro burro", "Certo"],
        ["Calcular K antes do ângulo", "Ângulo PRIMEIRO"],
        ["Ângulo deu 45° e você força K", "45° ≠ 180° → resposta é NÃO"],
        ["Confundir tabela ZN fechada e aberta", "Fechada=KC,TC · Aberta=K,T,L"],
        ["Ts = 4/ωn", "Ts = 4/(ζωn) = 4/σ"],
        ["Esquecer I quando pede erro zero", "Ki tem que ser ≠ 0"],
    ], [6 * cm, 9 * cm]))

    st.append(Spacer(1, 0.5 * cm))
    st.append(HRFlowable(width="100%", thickness=1, color=colors.grey))
    st.append(Paragraph(
        "<b>Ordem de estudo 3h:</b> Receita 1 (1h) → Receita 5 tabelas (45min) → "
        "Receita 3 (45min) → Receita 2 (30min). Depois faça as 10 questões.",
        s["P"],
    ))

    questoes_completas(st, s)

    return st


def main():
    s = styles()
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        rightMargin=1.3 * cm, leftMargin=1.3 * cm,
        topMargin=1.3 * cm, bottomMargin=1.3 * cm,
    )
    doc.build(story(s))
    print(f"PDF gerado: {OUTPUT}")


if __name__ == "__main__":
    main()
