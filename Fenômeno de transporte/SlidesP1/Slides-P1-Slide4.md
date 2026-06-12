# Explicando exercícios resolvidos sobre trabalho

## 4.2

Dois motores fornecem o mesmo trabalho para operar um guindaste. Um pode prover $3F$ em um cabo e o outro $1F$. O que você pode afirmar sobre o movimento do ponto em que a força $F$ age nos dois motores?

$$W = \int F\, dx = 3F x_1 = 1F x_2$$

$$x_2 = 3 x_1$$

![Exercício 4.2](Slide%204/2.png)

## 4.9

A Figura P4.9 mostra três situações físicas. Ilustre os possíveis processos num diagrama $P$-$V$.

**(a)** Cilindro com esbarros em $V_{\text{stop}}$ — processo: vertical em $V = V_{\text{stop}}$ até $P_1$, depois horizontal (estado 1).

**(b)** Cilindro com mola — processo com inclinação positiva passando pelo ponto 1 ($V_1$, $P_1$).

**(c)** Cilindro com R-410A, pistão $m_p$, $P_0$, esbarros no topo — processo: horizontal de 1 até $V_{\text{stop}}$, depois vertical para cima.

![Exercício 4.9 — Figura P4.9](Slide%204/3.png)

## 4.27

A força de arrasto aerodinâmico num automóvel é dada por $0{,}225\, A\, \rho\, V^2$. Admita que o ar se encontre a $290\ \text{K}$ e $100\ \text{kPa}$ e que a área frontal do automóvel seja $4\ \text{m}^2$, e a velocidade do automóvel seja $90\ \text{km/h}$. Determine a quantidade de energia utilizada para vencer a resistência aerodinâmica numa viagem de $30\ \text{minutos}$.

$$\rho = \frac{1}{v} = \frac{P}{RT} = \frac{100}{0{,}287 \times 290} = 1{,}2015\ \text{kg/m}^3$$

$$V = 90\,\frac{\text{km}}{\text{h}} = 90 \times \frac{1000\ \text{m}}{3600\ \text{s}} = 25\ \text{m/s}$$

$$\Delta x = V\,\Delta t = 25\ \text{m/s} \times 30\ \text{min} \times 60\ \text{s/min} = 45\,000\ \text{m}$$

$$F = 0{,}225\, A\, \rho\, V^2 = 0{,}225 \times 4 \times 1{,}2015 \times 25^2 = 675{,}8\ \text{m}^2\,\frac{\text{kg}}{\text{m}^3} \times \frac{\text{m}^2}{\text{s}^2} = \mathbf{676\ \text{N}}$$

$$W = F\,\Delta x = 676\ \text{N} \times 45\,000\ \text{m} = 30\,420\,000\ \text{J} = \mathbf{30{,}42\ \text{MJ}}$$

![Exercício 4.27](Slide%204/4.png)

## 4.35

Um conjunto cilindro–pistão contém ar a $600\ \text{kPa}$, $290\ \text{K}$ e o volume ocupado pelo ar é $0{,}01\ \text{m}^2$. Um processo a pressão constante retira $54\ \text{kJ}$ de trabalho. Determine o volume e a temperatura no estado final do ar nesse processo.

$$W = \int P\, dV = P\,\Delta V$$

$$\Delta V = W/P = \frac{54}{600} = 0{,}09\ \text{m}^3$$

$$V_2 = V_1 + \Delta V = 0{,}01 + 0{,}09 = 0{,}1\ \text{m}^3$$

Assuming ideal gas, $PV = mRT$, then we have

$$T_2 = \frac{P_2 V_2}{mR} = \frac{P_2 V_2}{P_1 V_1}\, T_1 = \frac{V_2}{V_1}\, T_1 = \frac{0{,}1}{0{,}01} \times 290 = \mathbf{2900\ \text{K}}$$

![Exercício 4.35](Slide%204/5.png)

## Balão — pressão proporcional ao quadrado do diâmetro

Um balão se comporta de tal modo que a pressão interna é proporcional ao quadrado do diâmetro. Esse balão contém $2\ \text{kg}$ de amônia inicialmente a $0\,^{\circ}\text{C}$ e volume de $1{,}8\ \text{m}^3$. O balão e a amônia são então aquecidos até que a pressão interna final atinja $600\ \text{kPa}$. Considerando a amônia como sistema, qual é o trabalho realizado durante o processo?

![Exercício — balão e amônia](Slide%204/6.png)

## 4.78

Uma bolha de sabão apresenta tensão superficial igual a $3 \times 10^{-4}\ \text{N/cm}$. Inicialmente, o filme de líquido está plano e apoiado num anel rígido com diâmetro de $50\ \text{mm}$. Você sopra sobre o filme e, desse modo, obtém uma superfície semiesférica com diâmetro igual a $5\ \text{cm}$. Determine o trabalho realizado sobre o filme de líquido nesse processo.

$${}_1W_2 = \int F\, dx = \int S\, dA = S\,\Delta A$$

$$= 2 \times S \times \left(\frac{\pi}{2} D^2 - \frac{\pi}{4} D^2\right)$$

$$= 2 \times 3 \times 10^{-4}\ \text{N/cm} \times 100\ \text{cm/m} \times \frac{\pi}{2}\, 0{,}05^2\ \text{m}^2\, (1 - 0{,}5) = \mathbf{1{,}18 \times 10^{-4}\ \text{J}}$$

$$A_1 = \frac{\pi}{4} D^2 \quad , \quad A_2 = \frac{1}{2}\pi D^2$$

![Exercício 4.78](Slide%204/7.png)

## 4.88

A potência utilizada para mover um automóvel a $100\ \text{km/h}$ é $25\ \text{HP}$. Determine o módulo da força motora entre os pneus e a pista.

$$dW = F \cdot dx \Rightarrow \frac{dW}{dt} = \dot{W} = F\,\frac{dx}{dt} = FV$$

$$F = \dot{W}/V$$

$$\dot{W} = 25\ \text{hp} = 25 \times 0{,}7355\ \text{kW} = 18{,}39\ \text{kW}$$

$$V = 100 \times \frac{1000}{3600} = 27{,}78\ \text{m/s}$$

$$F = \dot{W}/V = \frac{18{,}39\ \text{kW}}{27{,}78\ \text{m/s}} = \mathbf{0{,}66\ \text{kN}}$$

Units: $\text{kW}/(\text{ms}^{-1}) = \text{kW s m}^{-1} = \text{kJ s}^{-1}\,\text{s m}^{-1} = \text{kN m m}^{-1} = \text{kN}$

![Exercício 4.88](Slide%204/8.png)

## 4.90

Um guindaste levanta verticalmente um recipiente cheio de concreto com massa total igual a $450\ \text{kg}$, com velocidade de ascensão da carga constante e igual a $2{,}0\ \text{m/s}$. Determine a potência utilizada para realizar esse movimento.

$$\dot{W} = FV = mg \times V = 450\ \text{kg} \times 9{,}807\ \text{ms}^{-2} \times 2\ \text{ms}^{-1} = 8826\ \text{J/s}$$

$$\dot{W} = \mathbf{8{,}83\ \text{kW}}$$

![Exercício 4.90](Slide%204/9.png)

## 4.97

Uma bateria bem isolada termicamente está sendo carregada com uma tensão de carga de $12{,}3\ \text{V}$ e uma corrente igual a $6\ \text{A}$. Considerando a bateria como o sistema, determine a taxa instantânea de transferência de trabalho e o trabalho realizado num período de $4$ horas.

Battery thermally insulated $\Rightarrow$ $Q = 0$

For constant voltage $E$ and current $i$,

$$\text{Power} = E \cdot i = 12{,}3 \times 6 = \mathbf{73{,}8\ \text{W}}$$

[Units $\text{V} \times \text{A} = \text{W}$]

$$W = \int \text{power}\, dt = \text{power}\,\Delta t = 73{,}8 \times 4 \times 60 \times 60 = 1\,062\,720\ \text{J} = \mathbf{1062{,}7\ \text{kJ}}$$

![Exercício 4.97](Slide%204/10.png)

## 4.76

Um fio de cobre com diâmetro de $2\ \text{mm}$ e comprimento de $10\ \text{m}$ está esticado entre dois pontos. A tensão normal $\sigma = E(L - L_0)/L_0$ depende do comprimento $L$, do comprimento do corpo não tracionado $L_0$ e do módulo de Young, $E = 1{,}1 \times 10^8\ \text{kPa}$. A força, $F = A\sigma$, foi medida e é $110\ \text{N}$. Quanto o fio alongou e qual foi o trabalho aplicado?

## 4.80

Considere o processo de enchimento de um balão com gás hélio de um tanque. O hélio fornece o trabalho $\int P\, dV$ utilizado para esticar o material do balão $\int \mathcal{S}\, dA$ e, também, para deslocar a posição da atmosfera $\int P_0\, dV$. Estabeleça uma relação entre a pressão no hélio, a tensão superficial, a pressão atmosférica e o raio do balão a partir do balanço infinitesimal $\delta W_{\text{He}} = \delta W_{\text{esticar}} + \delta W_{\text{atm}}$.

## 4.116

Uma mola não linear apresenta uma relação entre força e deslocamento dada por $F = k_m(x - x_0)^n$. Se a extremidade da mola se move de $x_1$ a partir do estado relaxado, determine a fórmula do trabalho realizado.

![Exercícios 4.76, 4.80 e 4.116](Slide%204/11.png)

## 4.119

Gás butano ($C_4H_{10}$) está armazenado num cilindro-pistão com volume de $0{,}020\ \text{m}^3$ a $300\,^{\circ}\text{C}$ e $100\ \text{kPa}$. O gás é então comprimido lentamente, num processo isotérmico, até $300\ \text{kPa}$.

a) É razoável admitir que o butano se comporte como gás ideal durante esse processo?

b) Determine o trabalho feito pelo butano durante o processo.

## 4.126

O espaço localizado acima do nível d'água num tanque fechado contém nitrogênio a $25\,^{\circ}\text{C}$ e $0{,}1\ \text{MPa}$. O volume total do tanque é de $4\ \text{m}^3$ e contém $500\ \text{kg}$ de água a $25\,^{\circ}\text{C}$. Uma quantidade adicional de $500\ \text{kg}$ de água é forçada para dentro do tanque. Admitindo que a temperatura permaneça constante no processo, calcule a pressão final no nitrogênio e o trabalho realizado sobre o nitrogênio durante o processo.

## 4.128

Ar a $200\ \text{kPa}$ e $30\,^{\circ}\text{C}$ está contido num cilindro-pistão. O volume do cilindro é $0{,}1\ \text{m}^3$ e a pressão contrabalança a pressão ambiente externa de $100\ \text{kPa}$, acrescida de uma força imposta externamente que é proporcional a $V^{0{,}5}$. Transfere-se calor ao ar até que a pressão atinja $225\ \text{kPa}$. Determine a temperatura final do ar e o trabalho efetuado durante o processo.

![Exercícios 4.119, 4.126 e 4.128](Slide%204/12.png)

## 4.61

O conjunto cilindro-pistão mostrado na Fig. P4.61 contém ar. Inicialmente o ar está a $150\ \text{kPa}$ e $400\,^{\circ}\text{C}$. O conjunto é então resfriado até $20\,^{\circ}\text{C}$. Pergunta-se:

a) O pistão está encostado nos esbarros no estado final? Qual é a pressão final no ar?

b) Qual é o trabalho por unidade de massa realizado neste processo?

**Figura P4.61** — cilindro com **Ar**; esbarros; $1\ \text{m}$ (base aos esbarros); $1\ \text{m}$ (esbarros ao pistão).

![Exercício 4.61 — Figura P4.61](Slide%204/13.png)
