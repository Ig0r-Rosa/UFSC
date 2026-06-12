# Calor: definição e formas de transferência

Capítulo 1.7, 2,3 e 2.4 — MORAN, M. J. & SHAPIRO, H. N. *Princípios de Termodinâmica para Engenharia*.

## O que é transferência de calor?

Transferência de calor é energia térmica em movimento devido a uma diferença de temperatura.

## O que é energia térmica?

Energia térmica é associada com a translação, rotação, vibração e os estados eletrônicos dos átomos e moléculas da matéria. Ela representa os efeitos acumulativos dessas atividades microscópicas que estão diretamente ligadas a temperatura da matéria.

**TÉRMICA** = Sensível + Latente

- **Energia sensível:** a porção da energia interna de um sistema associada às energias cinéticas das moléculas.
- **Energia latente:** energia interna associada à fase de um sistema (ligação entre as moléculas).

## Transferência de calor

- Sistemas entram em equilíbrio térmico através da transferência de calor (energia)
  - Sistema adiabático não troca calor com outros sistemas
- Sensação de quente e frio está relacionado com temperatura e com taxa de transferência de calor
  - Quando na mesma temperatura
    - Metal parece mais frio que madeira
    - A mão de uma pessoa queima mais rápido se segurar uma peça de metal ao invés de um pedaço de carvão
    - Uma pessoa exposta ao vento sente mais frio que uma pessoa num ambiente sem vento.

## Calor

**Unidades usuais, e como elas surgiram...**

- **Btu** — energia requerida para esquentar 1 lbm de água em 1 $^{\circ}\text{F}$.
- **Caloria** — energia requerida para esquentar 1 g de água em 1 $^{\circ}\text{C}$.
- **Unidade no SI units** — a mesma de trabalho — Joules.
  - $1\ \text{J} = 1\ \text{N}\cdot\text{m} = 1\ \text{kg}\cdot\text{m}^2/\text{s}^2$
- $1\ \text{cal} = 4{,}1868\ \text{J}$
- $1\ \text{Btu} = 1{,}055\ \text{kJ}$

**Usaremos o símbolo $Q$ para o calor.**

- Se $Q = 0$, não há calor sendo transferido — *processo adiabático*.

A quantidade de calor transferida do estado 1 para o estado 2 depende do processo — Calor não é uma propriedade e não pode ser usada para definir um estado.

## Semelhanças entre calor e trabalho

1. Calor & trabalho são fenômenos que ocorrem na fronteira do sistema.
2. Um sistema não tem calor nem trabalho, mas tem energia.
3. Calor ou trabalho quando atravessa a fronteira do sistema podem mudar a quantidade de energia e o estado do sistema.
4. A quantidade de calor e trabalho entre dois estados depende do tipo de processo

Sistema fechado ($m = \text{constante}$) — Fronteira do sistema — Calor — Trabalho

![Semelhanças entre calor e trabalho](Slide%205/5.png)

## Calor ou trabalho atravessa a fronteira do sistema?

**Figura 4.20** Exemplo que mostra a diferença entre calor e trabalho.

- (a) Gás — Fronteira do sistema em torno do gás — Bateria — aquecimento
- (b) Fronteira do sistema inclui gás e resistência — Bateria (+ / -)

![Figura 4.20 — calor e trabalho](Slide%205/6.png)

## Não confunda os significados de energia térmica, temperatura e transferência de calor

| Quantidade | Significado | Símbolo | Unidades |
|------------|-------------|---------|----------|
| Energia térmica (Interna) | Energia associada ao comportamento microscópico da matéria | $U$ ou $u$ | J ou J/kg |
| Temperatura | Uma maneira de determinar indiretamente a quantidade de energia térmica de uma quantidade de matéria | $T$ | K ou $^{\circ}\text{C}$ |
| Transferência de calor | Transferência de energia térmica devido a uma diferença de temperatura | | |
| Calor | Quantidade de energia térmica transferida em um intervalo de tempo $\Delta t > 0$ | $Q$ | J |
| Taxa de transferência de calor | Energia térmica transferida por unidade de tempo | $\dot{Q}$ | W |
| Fluxo de calor | Energia térmica transferida por unidade de tempo e unidade de área | $\dot{Q}''$ | W/m² |

## Formas de transferência de calor

**Condução através de um sólido ou fluido estacionário** — $T_1 > T_2$, $q''$

**Convecção de uma superfície para um fluido em movimento** — $T_s > T_\infty$, Fluido em movimento $T_\infty$

**Transferência líquida de calor por radiação entre duas superfícies** — Superfície $T_1$, Superfície $T_2$, $q''_1$, $q''_2$

- **Condução:** Transferência de calor em um sólido ou e um fluido estacionário (gás ou líquido) devido ao movimento aleatório dos átomos, moléculas ou elétrons.
- **Convecção:** Transferência de calor devido ao efeito combinado dos movimentos aleatórios e preferenciais de um fluido ecoando sobre uma superfície.
- **Radiação:** Energia que é emitida pela matéria devido a mudanças na configuração dos elétrons dos seus átomos ou moléculas, e é transportada por ondas eletromagnéticas (ou fótons).

- Condução e convecção requerem a presença de variações de temperatura em um meio material.
- Radiação se origina da matéria, porém seu transporte não necessita de um meio material, e ocorre melhor no vácuo.

![Formas de transferência de calor](Slide%205/8.png)

## Formas de transferência de calor — Condução

**Forma geral (vetorial) da Lei de Fourier:**

$$\dot{Q}'' = -k\,\nabla T$$

- $\dot{Q}''$: Fluxo de calor — W/m²
- $k$: Condutividade térmica — W/(m$\cdot$K)
- $\nabla T$: Gradiente de temperatura — K/m ou $^{\circ}\text{C}$/m

Condução unidimensional, estacionária através de uma parede plana de condutividade térmica constante

$$q''_x = -k\,\frac{dT}{dx} = -k\,\frac{T_2 - T_1}{L} = k\,\frac{T_1 - T_2}{L}$$

**Taxa de transferência de calor (W):**

$$\dot{Q} = -kA\,\frac{dT}{dx}\quad (\text{W})$$

![Condução — Lei de Fourier](Slide%205/9.png)

## Formas de transferência de calor — Condutividade térmica

Condutividade térmica ($k$) ~ $100\ \text{W/mK}$ para metais, ~1-10 para sólidos e líquidos não metálicos, ~0,1 para materiais isolantes, & 0,1 to 0,01 para gases.

**Fig. 2.4** Faixa da condutividade térmica para vários estados da matéria em condições normais de temperatura e de pressão.

![Fig. 2.4 — condutividade térmica](Slide%205/10.png)

## 4.103 — Panela de aço

Uma panela de aço com condutibilidade térmica igual a $50\ \text{W/mK}$ e espessura de $5\ \text{mm}$ na parede do fundo, contém água líquida a $15\,^{\circ}\text{C}$. O diâmetro da panela é $0{,}2\ \text{m}$. A panela é colocada sobre uma resistência elétrica que transfere $250\ \text{W}$ de calor. Admitindo que a temperatura da superfície interna da panela seja uniforme e igual a $15\,^{\circ}\text{C}$, determine a temperatura da superfície inferior externa da panela.

$$\dot{Q} = k \cdot A \cdot \frac{\Delta T}{\Delta x} \Rightarrow \Delta T = \frac{\dot{Q} \cdot \Delta x}{k \cdot A}$$

$$\Delta T = \frac{250\ \text{W} \times 0{,}005\ \text{m}}{50\ \text{W/mK} \times \frac{\pi}{4} \times 0{,}2^2\ \text{m}^2} = 0{,}796\ \text{K}$$

$$T = 15 + 0{,}796 \cong \mathbf{15{,}8\,^{\circ}\text{C}}$$

![Exercício 4.103](Slide%205/11.png)

## Formas de transferência de calor — Convecção

Há uma relação entre convecção e escoamento sobre uma superfície, e desenvolvimento das camadas limite de velocidade e térmica

**Fig. 1.4** Desenvolvimento da camada limite na transferência de calor por convecção.

- Superfície aquecida — $T_s$, $q''$
- Fluido — Distribuição de velocidade $u(y)$, $u_\infty$
- Distribuição de temperatura $T(y)$, $T_\infty$

**Lei de resfriamento de Newton:**

$$\dot{Q}'' = h\,\Delta T\quad (\text{W/m}^2)$$

$h$: Coeficiente de transferência de calor por convecção (W/m²·K)

**Valores típicos:**

- Convecção natural em gás: 5–25 W/m²K
- Convecção natural em líquido: 50-1000 W/m²K
- Convecção forçada em gás: 25-250 W/m²K
- Convecção forçada em líquido: 50-20 000 W/m²K
- Ebulição: 2500 - 100 000 W/m²K

![Convecção](Slide%205/12.png)

## Para-brisa — convecção e condução

Um automóvel percorre uma estrada num dia em que a temperatura ambiente é $-15\,^{\circ}\text{C}$. A temperatura externa no para-brisa é mantida a $2\,^{\circ}\text{C}$ devido ao escoamento de ar quente sobre a superfície interna do para-brisa. Admitindo que a área do para-brisa seja $0{,}5\ \text{m}^2$ e que o coeficiente de transferência de calor por convecção na superfície externa do para-brisa seja $250\ \text{W/m}^2\cdot\text{K}$, determine a taxa de transferência de calor para o ambiente externo através do para-brisa. Para essa taxa de transferência de calor e um vidro de $5\ \text{mm}$ de espessura com $k = 1{,}25\ \text{W/mK}$, qual é a temperatura da superfície interna do para-brisa?

$$\dot{Q}_{\text{conv}} = h \cdot A \cdot \Delta T = 250 \times 0{,}5 \times [2 - (-15)] = 250 \times 0{,}5 \times 17 = \mathbf{2125\ \text{W}}$$

$$\dot{Q}_{\text{cond}} = k \cdot A \cdot \frac{\Delta T}{\Delta x} \Rightarrow \Delta T = \frac{\dot{Q}}{kA}\,\Delta x$$

$$\Delta T = \frac{2125\ \text{W}}{1{,}25\ \text{W/mK} \times 0{,}5\ \text{m}^2} \times 0{,}005\ \text{m} = 17\ \text{K}$$

$$T_{\text{in}} = T_{\text{out}} + \Delta T = 2 + 17 = \mathbf{19\,^{\circ}\text{C}}$$

![Para-brisa](Slide%205/13.png)

## Geladeira — trocador de calor

A lâmpada de iluminação interna de uma geladeira (25 W) permanece acesa por falha no fechamento da porta e a transferência de calor do ambiente para o espaço refrigerado é igual a 50 W. Qual deve ser a diferença de temperatura para o ambiente a $20\,^{\circ}\text{C}$ que o refrigerador deve apresentar em seu trocador de calor com $1\ \text{m}^2$ de área e coeficiente médio de transferência de calor de $15\ \text{W/m}^2\text{K}$ para rejeitar o calor que vaza para o interior do espaço refrigerado?

$$\dot{Q}_{\text{tot}} = 25 + 50 = 75\ \text{W to go out}$$

$$\dot{Q} = hA\,\Delta T = 15 \times 1 \times \Delta T = 75\ \text{W}$$

$$\Delta T = \frac{\dot{Q}}{hA} = \frac{75}{15 \times 1} = 5\,^{\circ}\text{C}$$

![Geladeira — trocador de calor](Slide%205/14.png)

## Formas de transferência de calor — Radiação

Radiação (A mais importante forma de transferência de calor !!!!!)

Transferência de calor em uma interface gás/superfície envolve emissão de radiação da superfície e também pode envolver absorção da radiação incidente do meio ambiente (irradiação, $G$), assim como convecção (se $T_s \neq T_\infty$)

**Energia saindo da superfície devido a emissão:**

- Potência emissiva: $E = \epsilon E_b = \epsilon \sigma T_s^4$ (W/m²)
- Emissividade da superfície: $0 \leq \epsilon \leq 1$
- Potência emissiva de um corpo negro (emissor perfeito): $E_b$ (W/m²)
- $\sigma =$ Constante de Stefan – Boltzmann ($5{,}67 \times 10^{-8}\ \text{W/m}^2\cdot\text{K}^4$)

**Energia absorvida devido a irradiação:**

- Radiação incidente absorvida: $G_{\text{abs}} = \alpha G$ (W/m²)
- Absorvividade da superfície: $0 \leq \alpha \leq 1$
- Irradiação: $G$ (W/m²)

Superfície com emissividade $\epsilon$, absorvividade $\alpha$ e temperatura $T_s$ — Gás $T_\infty$, $h$ — $G$, $E$, $q''_{\text{conv}}$

![Radiação](Slide%205/15.png)

## Irradiação — ambiente infinito

**Irradiação:** Caso particular de uma superfície exposta a um ambiente "infinito" de temperatura uniforme ($T_{\text{sur}}$)

Superfície de emissividade $\epsilon = \alpha$, área $A$ e temperatura $T_s$ — Vizinhanças a $T_{\text{viz}}$ — Gás, $T_\infty$, $h$ — $q''_{\text{rad}}$, $q''_{\text{conv}}$

$$G = G_{\text{sur}} = \sigma T_{\text{sur}}^4$$

Se $\alpha = \epsilon$, o fluxo líquido de radiação na superfície devido a troca de energia com o ambiente é

$$\dot{Q}''_{\text{rad}} = \epsilon E_b - \alpha G = \epsilon \sigma (T_s^4 - T_{\text{sur}}^4)$$

![Irradiação — ambiente infinito](Slide%205/16.png)

## Convecção + radiação

As diferenças de temperatura são geralmente consideradas positivas e portanto, quando $T_s > T_0$ e $T_{\text{surr}}$

$$\dot{Q}'' = \dot{Q}''_{\text{conv}} + \dot{Q}''_{\text{rad}} = h(T_s - T_0) + \epsilon E_b - \alpha G = h(T_s - T_0) + \epsilon \sigma (T_s^4 - T_{\text{surr}}^4)$$

$T_s$ é a temperatura da superfície, $T_0$ é a temperatura do fluido, e $T_{\text{surr}}$ é a temperatura do entorno da superfície, que pode ou não ser igual a $T_0$.

![Convecção e radiação combinadas](Slide%205/17.png)

## Emissão de radiação — casa

A temperatura e a emissividade da superfície de uma casa são iguais a $30\,^{\circ}\text{C}$ e $0{,}7$. A temperatura do ambiente que circunda a casa é igual a $15\,^{\circ}\text{C}$ e a emissividade média é $0{,}9$. Determine a taxa de emissão de radiação por unidade de área para cada superfície.

$$\dot{Q}/A = \epsilon \sigma T^4$$

$$\sigma = 5{,}67 \times 10^{-8}\ \text{W/m}^2\text{K}^4$$

a) $\dot{Q}/A = 0{,}7 \times 5{,}67 \times 10^{-8} \times (273{,}15 + 30)^4 = \mathbf{335\ \text{W/m}^2}$

b) $\dot{Q}/A = 0{,}9 \times 5{,}67 \times 10^{-8} \times 288{,}15^4 = \mathbf{352\ \text{W/m}^2}$

![Emissão de radiação — casa](Slide%205/18.png)

## 4.105

Um aquecedor de água apresenta área superficial igual a $3\ \text{m}^2$ e está coberto com uma camada de isolante térmico. As temperaturas interna e externa da camada de isolante são respectivamente iguais a $75$ e $18\,^{\circ}\text{C}$, e o material isolante apresenta condutibilidade térmica igual a $0{,}08\ \text{W/mK}$. Qual deve ser a espessura da camada de isolante para que a transferência de calor do aquecedor seja igual a $200\ \text{W}$?

## 4.106

Um condensador de grande porte (trocador de calor) que vai ser utilizado numa central de potência precisa transferir $100\ \text{MW}$ da água que escoa no ciclo de potência para a água bombeada do mar. Admita que a parede de aço que separa a água do ciclo da água do mar apresente espessura de $4\ \text{mm}$, que a condutibilidade térmica do aço seja igual a $15\ \text{W/mK}$ e que a diferença máxima de temperatura permitida entre os dois fluidos seja de $5\,^{\circ}\text{C}$. Determine a área mínima de transferência de calor desse condensador, desprezando-se a resistência à transferência de calor por convecção nos escoamentos.

![Exercícios 4.105 e 4.106](Slide%205/19.png)

## 4.111

A grade preta atrás de um refrigerador tem a temperatura da superfície igual a $35\,^{\circ}\text{C}$ e uma superfície total de $1\ \text{m}^2$. A transferência de calor para o ambiente a $20\,^{\circ}\text{C}$ se dá com um coeficiente de transferência de calor médio por convecção de $15\ \text{W/m}^2\text{ K}$. Quanto de energia pode ser removida durante $15\ \text{min}$ de operação?

## 4.115

Um aquecedor por radiação cilíndrico apresenta comprimento e diâmetro iguais a $0{,}5\ \text{m}$ e $5\ \text{mm}$. A potência dissipada no aquecedor é $400\ \text{W}$. Admitindo que a emissividade da superfície do aquecedor seja igual a $0{,}9$ e desprezando a radiação que incide no aquecedor, determine a temperatura superficial desse aquecedor.

![Exercícios 4.111 e 4.115](Slide%205/20.png)

## 1.24

Em condições nas quais a mesma temperatura ambiente é mantida por um sistema de aquecimento ou resfriamento, é comum para uma pessoa sentir-se incomodada com um pouco de frio no inverno mas confortável no verão. Dê uma explicação plausível para essa situação (com cálculos que apóiem sua colocação), considerando que a temperatura do ar ambiente seja mantida a $20\,^{\circ}\text{C}$ durante todo o ano e as paredes da sala a $27\,^{\circ}\text{C}$ e $14\,^{\circ}\text{C}$ no verão e no inverno, respectivamente. A superfície exposta de uma pessoa na sala pode ser considerada a uma temperatura de $32\,^{\circ}\text{C}$ no decorrer do ano com uma emissividade de $0{,}90$. O coeficiente associado à transferência de calor por convecção natural entre a pessoa e o ar ambiente é aproximadamente $2\ \text{W/m}^2\cdot\text{K}$.

![Exercício 1.24](Slide%205/21.png)
