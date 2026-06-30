---
lang: pt-BR
geometry: margin=2cm
fontsize: 10pt
header-includes:
  - \usepackage{amsmath}
  - \usepackage{enumitem}
  - \usepackage{xcolor}
  - \usepackage{framed}
  - \definecolor{resposta}{RGB}{0,70,130}
  - \newenvironment{resposta}{\begin{framed}\noindent\textbf{\textcolor{resposta}{Resposta}}\\[2pt]}{\end{framed}}
  - \setlength{\parskip}{4pt}
---

\begin{center}
\textbf{\Large Treino P4 — Questão / Resposta}\\[4pt]
\small Fenômenos de Transporte — exercícios prioritários para a prova
\end{center}

\hrule

## 1. Pitot + manômetro invertido (Slide 25, Parte 3)

**Questão:** Tubo horizontal com água ($\rho = 1000$ kg/m$^3$). Pitot-estático: $D_0 = 0{,}08$ m; manômetro invertido com $\rho_m = 900$ kg/m$^3$, deflexão $h = 2{,}5$ m. Qual a vazão volumétrica?

**Roteiro:** Manometria $\Rightarrow (p_1-p_0)/\rho = gh(1-\rho_m/\rho)$; Pitot $\Rightarrow V_0 = \sqrt{2(p_1-p_0)/\rho}$; $\dot{Q} = A_0 V_0$.

$$\dot{Q} = \pi D_0^2 \sqrt{\frac{gh}{8}\left(1-\frac{\rho_m}{\rho}\right)}$$

\begin{resposta}
$\dot{Q} = \mathbf{0{,}0111\ \text{m}^3/\text{s} = 11{,}1\ \text{L/s}}$ \quad ($V_0 \approx 2{,}22$ m/s)
\end{resposta}

---

## 2. Encontro de dois jatos — Torricelli (Slide 32, Parte 3)

**Questão:** Tanque com dois furos na parede direita. Furo inferior a profundidade $h_2$; furo superior a $h_1$ acima do inferior ($h_1$ = distância entre furos). Onde os jatos se cruzam a distância horizontal $L$ da parede?

**Roteiro:** $V_{inf}=\sqrt{2gh_2}$, $V_{sup}=\sqrt{2g(h_2-h_1)}$. Cinemática horizontal; igualar alturas $y(L)$.

\begin{resposta}
$$L = 2\sqrt{h_2(h_2-h_1)}$$

Substitua os valores numéricos do enunciado (figura do slide).
\end{resposta}

---

## 3. Venturi inclinado + manômetro (Slide 35, Parte 3)

**Questão:** Tubo inclinado $\theta$; água ($\gamma$); diâmetros $D_1$, $D_2$; cota $z_2-z_1$; manômetro diferencial invertido com fluido $SG$; deflexão $h$; distância vertical $l$. Relação $h=f(Q)$ ou $Q=f(h)$.

**Roteiro:** Bernoulli (1)→(2) + continuidade + manometria (slides 47–48).

\begin{resposta}
$$\dot{Q} = \frac{D_2^2 D_1^2}{2}\sqrt{\left(\frac{\rho_w}{\rho}-1\right)\frac{\pi^2 g\sin\theta\,L}{2(D_1^4-D_2^4)}}$$

onde $\rho_w = SG \cdot \rho_{água}$ e $L$ = comprimento inclinado entre (1) e (2). Na prova: substitua $D_1$, $D_2$, $\theta$, $L$ e $SG$ da figura.
\end{resposta}

---

## 4. Pitot calibrado em ar, usado em água — Ex. 3.23 (Slide 43, Parte 3)

**Questão:** Pitot calibrado para ler $V$ diretamente com ar padrão. Medindo água, indica $102{,}9$ m/s. Qual a velocidade real?

**Roteiro:** Mesma $\Delta p$ no manômetro; calibração usou $\rho_{ar}$; escoamento real é água ($\rho_w$).

$$V_{real} = V_{ind} \sqrt{\frac{\rho_{ar}}{\rho_w}} \qquad (\rho_{ar} \approx 1{,}225\ \text{kg/m}^3)$$

\begin{resposta}
$$V_{real} = 102{,}9 \sqrt{\frac{1{,}225}{998}} = \mathbf{3{,}61\ \text{m/s}}$$
\end{resposta}

---

## 5. Turbina — Ex. 8.91 (Slide 83, Parte 3)

**Questão:** Turbina 400 kW. Tubo ferro fundido $L=120$ m, $D=300$ mm; difusor saída $D_{s}=1$ m; queda $H=20$ m (superfície livre → saída). Efeitos viscosos desprezíveis exceto item (b). **(a)** Perdas nulas. **(b)** Só perda distribuída, $f=0{,}02$.

**Roteiro (a):** Reservatório ($V \approx 0$) → saída atmosférica:

$$H = \frac{\dot{W}}{\rho g Q} + \frac{Q^2}{2g A_{saida}^2}$$

**Roteiro (b):** Acrescentar $h_L = f(L/D)(V_{tubo}^2/2g)$ com $V_{tubo}=Q/A_{tubo}$.

\begin{resposta}
**(a)** $Q = \mathbf{2{,}08\ \text{m}^3/\text{s}}$ (considerando energia cinética na saída).

**(b)** Com $f=0{,}02$ e $V_{tubo}=Q/(\pi D^2/4)$, as perdas distribuídas são muito altas para $Q$ típico de (a) — **pode não haver solução real** (conforme observação do livro). Se houver raízes, resolva numericamente a equação cúbica em $Q$.
\end{resposta}

---

## 6. Circuito fechado com bomba — Ex. 8.93 (Slide 80, Parte 3)

**Questão:** Circuito fechado com reservatório. Bomba: $\dot{W}=272$ W. Tubo $D=31$ mm, $L=61$ m, $\varepsilon/D=0{,}01$. Perdas locais: $K_{ent}=0{,}8$; $K_{filtro}=12{,}0$; $K_{valv}=6{,}0$; $K_{saida}=1{,}0$; 4 curvas $K_{curva}=1{,}5$ cada.

**Roteiro:** Circuito fechado (mesma cota): $h_{bomba} = h_L$.

$$h_{bomba} = \frac{\dot{W}}{\rho g Q}, \quad h_L = \left(f\frac{L}{D} + \sum K_L\right)\frac{V^2}{2g}, \quad V=\frac{Q}{A}$$

Iterar: chute $Q$ → Re → Colebrook → $f$ → balancear.

\begin{resposta}
$Q \approx \mathbf{1{,}45\ \text{L/s}}$ \quad ($1{,}45 \times 10^{-3}$ m$^3$/s)

Re $\approx 5{,}9 \times 10^4$; $f \approx 0{,}039$; $\sum K_L = 25{,}8$
\end{resposta}

---

## 7. Jato em placa inclinada (Slide 50, Parte 4)

**Questão:** Jato horizontal $A_0 = 80$ cm$^2 = 0{,}008$ m$^2$, $V_0 = 5$ m/s. Placa inclinada $\alpha = 40°$ com a horizontal. Sem atrito. Força na placa $N$; áreas de saída $A_1$, $A_2$ (jatos ao longo da placa).

**Roteiro:** $V_0=V_1=V_2$; continuidade $A_0=A_1+A_2$; momento $x$ e $y$ (sistema do slide 51–52).

\begin{resposta}
$$N = \mathbf{126{,}8\ \text{N}} \qquad A_1 = \mathbf{0{,}0071\ \text{m}^2} \qquad A_2 = \mathbf{0{,}0009\ \text{m}^2}$$
\end{resposta}

---

## 8. Placa em canal aberto — Ex. 5.48 (Slide 35, Parte 4)

**Questão:** Canal 2D; seção (1): profundidade $1{,}22$ m, $V_1=3{,}0$ m/s, pressão hidrostática; placa inclinada $20°$ da vertical; jato livre na seção (2) espessura $0{,}3$ m. Força para imobilizar placa (por unidade de largura $b$).

**Roteiro:** VC; continuidade $V_1 h_1 = V_2 h_2$; momento $x$ e $y$; pressão hidrostática na entrada $F_p = \rho g h_c A$.

\begin{resposta}
Força por metro de largura do canal:

$$F_x' \approx 3003\ \text{N/m}, \quad F_y' \approx 41\,875\ \text{N/m}, \quad F' = \sqrt{F_x'^2+F_y'^2} \approx \mathbf{4{,}2 \times 10^4\ \text{N/m}}$$

(problema bidimensional — resultado em N/m)
\end{resposta}

---

## 9. Continuidade em tanque — Ex. 5.15 (Slide 18, Parte 4)

**Questão:** Compressor alimenta $Q_{in}=0{,}283$ m$^3$/s de ar padrão ($\rho_{std}=1{,}225$ kg/m$^3$). Tanque $V=0{,}57$ m$^3$. Saída: $D=30{,}5$ mm, $V=213$ m/s, $\rho=1{,}80$ kg/m$^3$.

**(a)** Taxa de variação da massa no tanque. **(b)** Taxa de variação de $\rho$.

**Roteiro:** $\dot{m}=\rho Q$; $\dot{m}_{in}-\dot{m}_{out} = dm/dt$; $d\rho/dt = (dm/dt)/V$.

\begin{resposta}
**(a)** $\dot{m}_{in} = 0{,}347$ kg/s; $\dot{m}_{out} = 0{,}280$ kg/s $\Rightarrow$ $\mathbf{dm/dt = +0{,}067\ \text{kg/s}}$ (massa aumenta)

**(b)** $\mathbf{d\rho/dt = 0{,}117\ \text{kg/(m}^3\text{·s)}}$
\end{resposta}

---

## 10. Bomba no porão — Ex. 5.24 (Slide 20, Parte 4)

**Questão:** Infiltração eleva superfície livre a $25{,}4$ mm/h. Área do porão $139{,}4$ m$^2$. **(a)** Capacidade da bomba para nível constante. **(b)** Capacidade para baixar nível a $76{,}2$ mm/h (mesma infiltração).

**Roteiro:** $Q_{inf} = A \cdot dh_{inf}/dt$; (a) $Q_{bomba}=Q_{inf}$; (b) $Q_{bomba}=Q_{inf}+A \cdot dh_{dreno}/dt$.

\begin{resposta}
**(a)** $Q = \mathbf{0{,}984\ \text{L/s}}$ \quad ($9{,}84 \times 10^{-4}$ m$^3$/s)

**(b)** $Q = \mathbf{3{,}93\ \text{L/s}}$ \quad ($3{,}93 \times 10^{-3}$ m$^3$/s)
\end{resposta}

---

\vspace{0.5em}
\hrule
\small
\textbf{Dica geral:} Converta unidades antes (cm→m, mm/h→m/s). Use $g=9{,}81$ m/s$^2$. Em tubos: Re $\leq 2100$ laminar; Re $\geq 4000$ turbulento + Colebrook. Figuras originais: `SlidesP4/ConteudoP4/MD/Slides-P4-Parte3-Exercicios.md` e `Slides-P4-Parte4-Exercicios.md`.
