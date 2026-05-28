# Trabalho: definição e formas de calculá-lo

Capítulo 2.1, 2.2 e 2.3 — MORAN, M. J. & SHAPIRO, H. N. *Princípios de Termodinâmica para Engenharia*.

## TRABALHO

Trabalho é uma forma transferência de energia cujo o único efeito poderia ser o levantamento de um peso.

$$W\ (\text{J}) = \text{força}\ (\text{N}) \times \text{deslocamento}\ (\text{m})$$

$$1\ \text{J} = 1\ \text{N} \times 1\ \text{m}$$

Nesse contexto, trabalho feito pelo sistema é $+$, trabalho recebido pelo sistema é $-$.

**Figura 4.1** Exemplo de trabalho atravessando a fronteira de um sistema.

- (a) Bateria — Motor — Ventilador
- (b) Bateria — Motor — Polia — Peso

**Figura 4.2** Exemplo de trabalho atravessando a fronteira de um sistema devido ao fluxo de uma corrente elétrica através dela.

- Fronteira do sistema: Bateria
- Motor — Polia — Peso (fora da fronteira)

![Trabalho — definição e Figuras 4.1 e 4.2](Slide%203/2.png)

## Como calcular o trabalho?

$$\delta W = F\, ds$$

$$W_{1-2} = \int_{s_1}^{s_2} F\, ds$$

Força e deslocamento na mesma direção

$$W_{1-2} = F\,\Delta s$$

$$\dot{W} = F\,\frac{\Delta s}{\Delta t} = FV$$

Unidade no SI: $\dot{W}$ (J/s)

**Qual o trabalho nestas situações?**

- Elevator car — Motor, $F$, $ds$, $W=?$
- Carro em rampa: $30°$, $90\ \text{km/h}$, $m = 1200\ \text{kg}$

![Como calcular o trabalho?](Slide%203/3.png)

## Trabalho pelo efeito da pressão ao alterar um volume

$$\delta W = P\, dV \Rightarrow W_{1-2} = \int_{V_1}^{V_2} P\, dV$$

$$dV = A\, dl \Rightarrow W_{1-2} = A \int_{l_1}^{l_2} P\, dl$$

**Figura 4.4** Exemplo de trabalho efetuado pelo movimento da fronteira de um sistema, num processo quase-estático.

**Processo quase estático (quase equilíbrio)!**

**Figura 4.5** Uso do diagrama $P$-$V$ para mostrar o trabalho realizado na fronteira móvel de um sistema num processo quase-estático.

**Figura 3.4** O trabalho está na área tracejada do estado 1 para estado 2.

- (a) $P = c/V$
- (b) $P = c_1 - c_2 V^2$

![Trabalho pela pressão — Figuras 4.4, 4.5 e 3.4](Slide%203/4.png)

## Trabalho pelo efeito da pressão ao alterar um volume

$$\delta W = P\, dV \Rightarrow W_{1-2} = \int_{V_1}^{V_2} P\, dV$$

$$dV = A\, dl \Rightarrow W_{1-2} = A \int_{l_1}^{l_2} P\, dl$$

**Figura 4.4** Exemplo de trabalho efetuado pelo movimento da fronteira de um sistema, num processo quase-estático.

**Válido para processo quase estático ou quase em equilíbrio!**

**Figura 4.5** Uso do diagrama $P$-$V$ para mostrar o trabalho realizado na fronteira móvel de um sistema num processo quase-estático.

![Trabalho pela pressão — processo quase-estático](Slide%203/5.png)

## Trabalho pelo efeito da pressão ao alterar um volume

$$\delta W = P\, dV$$

$$P = f(V)$$

$$W_{1-2} = \int_{V_1}^{V_2} f(V)\, dV$$

**Figura 3.4** O trabalho está na área tracejada do estado 1 para estado 2.

- (a) $P = c/V$ — **Processo quase estático (quase equilíbrio)!**
- (b) $P = c_1 - c_2 V^2$

![Trabalho — $P = f(V)$ e Figura 3.4](Slide%203/6.png)

## Trabalho em uma mola

- **Posição de repouso** — elongamento: $dx$, $x$, força $F$
- Caption: Elongamento de uma mola sob ação de uma força
- $F_1 = 300\ \text{N}$, $x_1 = 1\ \text{mm}$; $F_2 = 600\ \text{N}$, $x_2 = 2\ \text{mm}$
- Caption: Alongamento da mola quando a força é duplicada

**Figura P3.62** — cilindro com $H_2O$, mola, $P_0$

$$\delta W = F\, dx \quad ; \quad F = k(x - x_0)\ \text{(mola com constante de deformação linear)}$$

$${}_1W_2 = \int_1^2 k(x - x_0)\, dx = k\left[\frac{(x_2^2 - x_1^2)}{2} - x_0(x_2 - x_1)\right]$$

![Trabalho em uma mola](Slide%203/7.png)

## Trabalho de eixo

Torque: $\vec{T} = \vec{F} \times \vec{r} = Fr\sin(90°) = Fr$

$$\Delta S = 2\pi r$$

$$W = F\,\Delta S = \frac{T}{r}\,2\pi r = 2\pi T$$

Velocidade angular: $\dfrac{d\theta}{dt} = 2\pi n = \omega$ (radianos/s); $n$ = nº de rev/s

Velocidade circunferencial: $\dfrac{dx}{dt} = r\,\dfrac{d\theta}{dt} = 2\pi r n$

Potência de eixo: $\dot{W} = \dfrac{dW}{dt} = F\,\dfrac{dx}{dt} = \dfrac{T}{r}\,2\pi r n = 2\pi n T$

ou: $\dot{W} = T\,\dfrac{d\theta}{dt} = 2\pi n T = T\omega$

$W_{sh} = 2\pi n T$ — Torque = $Fr$

![Trabalho de eixo](Slide%203/8.png)

## E como calcular o trabalho em processos de não-equilíbrio?

**Figura 4.14** Esboço para o Exemplo 4.5.

- $P_0$, $m_p$, $P_1$

$${}_1W_2 = \int_1^2 P\, dV$$

**Figura 4.15** Pressão no sistema em função do tempo.

$${}_1W_2 = \int_1^2 P\, dV = P_0(V_2 - V_1)$$

![Trabalho em processos de não-equilíbrio](Slide%203/9.png)

## E qual o trabalho para encher um espaço evacuado

**Figura 4.17** Exemplo de um processo que apresenta variação de volume e trabalho nulo.

- (a) Gás | Vácuo — Fronteira do sistema
- (b) Gás (volume total) — Fronteira do sistema

(a): Se o sistema for o gás, há mudança de volume, mas o trabalho não pode ser calculado

$${}_1W_2 \neq \int_1^2 P\, dV$$

**processo não em equilíbrio**

O processo não é quase estático e pressão contra a expansão é zero.

$${}_1W_2 = \int_1^2 P\, dV = P_0(V_2 - V_1)$$

$$W_{1-2} = \int_{V_1}^{V_2} 0\, dV = 0$$

![Trabalho para encher espaço evacuado](Slide%203/10.png)

## Trabalho de fronteira móvel em um processo com volume constante

Sistema **AR**:

- $P_1 = 500\ \text{kPa}$, $T_1 = 150°C$
- $P_2 = 400\ \text{kPa}$, $T_2 = 65°C$

Energia (saída)

Diagrama $P$-$V$: processo vertical de 500 kPa (estado 1) para 400 kPa (estado 2).

Nenhum trabalho de eixo, nenhum trabalho de campo gravitacional, nenhum trabalho de energia potencial (ex. mola)

$${}_1W_2 = \int_1^2 P\, dV\ \text{; como}\ V = \text{constante,}$$

$$dV = 0,\ \text{e}\ {}_1W_2 = 0$$

![Trabalho — volume constante](Slide%203/11.png)

## Trabalho de fronteira móvel em um processo com pressão constante

$H_2O$: $m = 10\ \text{lbm}$, $P = 60\ \text{psia}$ — Energia (entrada)

Diagrama $P$-$v$: $P = 60\ \text{psia}$ constante; $v_1 = 7{,}485$; $v_2 = 8{,}353$; $P_0 = 60\ \text{psia}$; Area = $w_b$

Se $P = \text{constante}$, **Processo Isobárico:**

$${}_1W_2 = P \int_1^2 dV = P(V_2 - V_1)$$

![Trabalho — pressão constante](Slide%203/12.png)

## Trabalho de fronteira móvel em um processo com temperatura constante

**Ar**: $V_1 = 0{,}4\ \text{m}^3$, $P_1 = 100\ \text{kPa}$, $T_0 = 80°C = \text{const.}$ — calor (saída)

Diagrama $P$-$V$: $T_0 = 80°C = \text{const.}$; estados em $V = 0{,}4$ e $V = 0{,}1$

Se $T = \text{constante}$, **Processo isotérmico:**

Se a substância é um gás ideal:

$$P_1 V_1 = mRT = P_2 V_2 = C \Rightarrow P = C/V$$

$${}_1W_2 = \int_1^2 P\, dV = \int_1^2 \frac{C}{V}\, dV = C \cdot \ln\frac{V_2}{V_1}$$

![Trabalho — temperatura constante](Slide%203/13.png)

## Trabalho em um processo politrópico

- A maneira como a “$P$” varia com o “$v$” depende do processo e das propriedades da substância.
- O processo politrópico é um processo onde $P \cdot V^n = \text{constante}$
- Para um processo com gás ideal a $T$ constante $P \cdot V^n = mRT = \text{constante}$ e $n = 1$

Diagrama $P$-$V$: $T_0 = 80°C = \text{const.}$; $V = 0{,}1$ (estado 2) a $V = 0{,}4$ (estado 1)

**Como encontrar o valor de $n$ quando os estados iniciais e finais são conhecidos?**

![Trabalho em processo politrópico](Slide%203/14.png)

## Trabalho líquido com fronteira móvel

Diagrama $P$-$V$: estados 1 e 2; caminhos A, B, C de 1 para 2.

- $W_A = 10\ \text{kJ}$
- $W_B = 8\ \text{kJ}$
- $W_C = 5\ \text{kJ}$

O trabalho depende do processo, e dos estados inicial e final.

Trabalho não é uma propriedade, e não pode ser utilizado para definir um estado

Ciclo: área $W_{\text{liq}}$ entre caminhos A e B (2→1 e 1→2).

O trabalho líquido em um ciclo é a diferença entre o trabalho realizado pelo sistema e o trabalho recebido pelo sistema

![Trabalho líquido com fronteira móvel](Slide%203/15.png)

## Outras formas de trabalho de fronteira:

### Alongamento de um filme de líquido

**Figura 4.16** Arranjo esquemático, mostrando o trabalho realizado sobre uma película superficial.

- Armação de arame — Fio corrediço — Película — $F$

Tensão superficial, $\sigma$ (N/m)

$$W = -\int_1^2 \sigma\, dA = -\int_1^2 \sigma\, 2b\, dx\quad (\text{J})$$

### Alongamento de um fio

$$W = -\int_1^2 F\, dL\quad (\text{J})$$

![Outras formas de trabalho de fronteira](Slide%203/16.png)

## Trabalho elétrico

$V$ é diferença de potencial, $dZ$ é quantidade de carga elétrica, e corrente $I$ é $\dfrac{dZ}{dt}$

**Potência elétrica**

$$\dot{W}_e = VI\quad (\text{W})$$

E o trabalho quando a diferença de potencial varia no tempo

$$W_e = \int_1^2 VI\, dt\quad (\text{J})$$

E o trabalho quando a diferença de potencial é constante no tempo

$$W_e = VI\,\Delta t\quad (\text{J})$$

$$\dot{W}_e = VI = I^2 R = V^2/R$$

Potência elétrica em termos de resistência $R$, corrente $I$, e diferença de potencial $V$.

![Trabalho elétrico](Slide%203/17.png)

## O trabalho total é a soma de todas as formas de trabalho

$$\delta W = p\, dV - \tau\, dL - \sigma\, dA - V\, dZ + \dots$$

![O trabalho total é a soma de todas as formas de trabalho](Slide%203/18.png)

## E qual a relação entre trabalho e variação de energia cinética?

Trajetória — Corpo — $s$, $ds$ — $\mathbf{v}$, $\mathbf{F}$, $\mathbf{F}_s$, $\mathbf{F}_n$

$$F_s = m\,\frac{dV}{dt}$$

$$F_s = m\,\frac{dV}{ds}\,\frac{ds}{dt} = mV\,\frac{dV}{ds}$$

$$\int_{V_1}^{V_2} mV\, dV = \int_{s_1}^{s_2} F_s\, ds$$

$$\int_{V_1}^{V_2} mV\, dV = \left[\frac{1}{2}mV^2\right]_{V_1}^{V_2} = \frac{1}{2}m(V_2^2 - V_1^2)$$

$$\Delta EC = EC_2 - EC_1 = \frac{1}{2}m(V_2^2 - V_1^2)$$

$$\frac{1}{2}m(V_2^2 - V_1^2) = \int_{s_1}^{s_2} \mathbf{F} \cdot d\mathbf{s}$$

![Trabalho e energia cinética](Slide%203/19.png)

## E qual a relação entre trabalho e variação de energia potencial?

Superfície da Terra — eixo $z$ — $z_1$, $z_2$ — forças $R$ e $mg$

$$\frac{1}{2}m(V_2^2 - V_1^2) = \int_{z_1}^{z_2} R\, dz - \int_{z_1}^{z_2} mg\, dz$$

$$\int_{z_1}^{z_2} mg\, dz = mg(z_2 - z_1)$$

$$\frac{1}{2}m(V_2^2 - V_1^2) + mg(z_2 - z_1) = \int_{z_1}^{z_2} R\, dz$$

$$\Delta EP = EP_2 - EP_1 = mg(z_2 - z_1)$$

![Trabalho e energia potencial](Slide%203/20.png)
