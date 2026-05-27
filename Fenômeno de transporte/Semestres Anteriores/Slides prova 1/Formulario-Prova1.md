# Formulário — Fenômenos de Transporte (Prova 1)

> Compilado a partir dos prints em `Slides prova 1/Slide 1..4`.

## Convenções rápidas (para não errar sinal/uso)

- **Pressão manométrica (gauge)**: $P_{gage} = P_{abs} - P_{atm}$
- **Eixo vertical**: nos slides, o **eixo $z$** é vertical e o **peso atua em $-\hat{k}$**.
- **Peso específico**: $\gamma = \rho g$

## 1) Conceitos de “sistema” (termodinâmica aplicada)

- **Sistema (sistema fechado)**: quantidade de matéria com **massa e identidade fixas**. Tudo externo é o **ambiente/vizinhança**; separação pela **fronteira**.
- **Volume de controle (sistema aberto)**: volume que envolve equipamento(s) (ou parte deles). O entorno é a **superfície de controle**. **Massa, calor e trabalho** podem atravessar a superfície.

## 2) Propriedades e definições úteis

### Temperatura e equilíbrio térmico (lei zero)

- **Temperatura (interpretação física)**: proporcional à quantidade de energia térmica contida em uma substância; é uma **medida indireta da agitação molecular**.
- **Lei zero da termodinâmica**:
  - **Enunciado**: se dois corpos $A$ e $B$ estão em equilíbrio térmico com um terceiro corpo $C$, então $A$ e $B$ estão em equilíbrio térmico entre si.
  - **Quando usar**: justificar **medição de temperatura** por comparação (termometria). No slide: $C$ é o termômetro; $A$ o meio de calibração; $B$ o meio cuja $T$ se deseja.

### Massa específica, volume específico, peso específico

- **Massa específica (densidade)**:
  - **Fórmula**: $\rho = \frac{m}{V}$
  - **Variáveis**: $\rho$ (kg/m³), $m$ (kg), $V$ (m³)
  - **Quando usar**: converter massa↔volume; hidrostática; balanços.

- **Volume específico**:
  - **Fórmula**: $v = \frac{V}{m} = \frac{1}{\rho}$
  - **Variáveis**: $v$ (m³/kg), $V$ (m³), $m$ (kg), $\rho$ (kg/m³)
  - **Quando usar**: tabelas de propriedades/termo; gás ideal; compressibilidade.

- **Peso específico**:
  - **Fórmula**: $\gamma = \frac{W}{V} = \rho g$
  - **Variáveis**: $\gamma$ (N/m³), $W$ (N), $\rho$ (kg/m³), $g$ (m/s²)
  - **Quando usar**: hidrostática e manometria (colunas de fluido).

### Viscosidade (cinemática)

- **Viscosidade cinemática**:
  - **Fórmula**: $\nu = \frac{\mu}{\rho}$
  - **Variáveis**: $\nu$ (m²/s), $\mu$ (Pa·s), $\rho$ (kg/m³)
  - **Quando usar**: comparar “fluidez” entre fluidos e em variação com $T$; número de Reynolds (quando aparecer).

## 3) Pressão — definições e variação espacial

### Pressão em um ponto

- **Definição**:
  - **Fórmula**: $p = \frac{F}{A}$
  - **Variáveis**: $p$ (Pa), $F$ (N), $A$ (m²)
  - **Quando usar**: converter força normal distribuída em pressão.

### Resultante de forças de pressão (gradiente de pressão)

Para um elemento diferencial $\delta x\,\delta y\,\delta z$, as resultantes por pressão (slides):

- $\delta F_x = -\frac{\partial p}{\partial x}\,\delta x\,\delta y\,\delta z$
- $\delta F_y = -\frac{\partial p}{\partial y}\,\delta x\,\delta y\,\delta z$
- $\delta F_z = -\frac{\partial p}{\partial z}\,\delta x\,\delta y\,\delta z$

Forma vetorial:

- **Fórmula**: $\delta \vec{F}_s = -\nabla p\;\delta x\,\delta y\,\delta z$
- **Variáveis**: $\nabla p$ (gradiente de pressão, Pa/m)
- **Quando usar**: ligar variação de pressão no espaço a força líquida por unidade de volume.

### Equação hidrostática (pressão vs profundidade)

Para fluido em repouso ($\vec{a}=0$):

- **Forma diferencial**: $\frac{dp}{dz} = -\rho g$
- **Forma integral (geral)**:
  - **Fórmula**: $P_2 - P_1 = -\int_{z_1}^{z_2} \rho g\,dz$
  - **Quando usar**: $\rho$ varia com $z$ (ex.: gases).

Se \(\rho\) é constante:

- **Variação de pressão**:
  - **Fórmula**: $\Delta P = P_2 - P_1 = \rho g\,\Delta z = \gamma\,\Delta z$
  - **Variáveis**: $\Delta z = z_2-z_1$
  - **Quando usar**: líquidos (aprox. incompressíveis) ou pequenos intervalos em gases.

- **Pressão a uma profundidade $h$** (tomando superfície como referência):
  - **Fórmulas**:
    - $P = P_{atm} + \rho g h$
    - $P_{gage} = \rho g h$
  - **Variáveis**: $h$ (m) profundidade; $P_{atm}$ (Pa)
  - **Quando usar**: tanques abertos; pressão manométrica em coluna de líquido.

## 4) Medidas de pressão — Manometria

**Manometria**: medir pressão usando **colunas de líquido** (manômetro).

### Princípio base (regra de ouro)

- Em fluido **em repouso**, ao subir $\Delta z>0$, a pressão **diminui** em $\rho g \Delta z$.
- Ao descer, a pressão **aumenta** em $\rho g|\Delta z|$.

### Tubo inclinado (dos slides)

- **Equação (arranjo com 3 fluidos)**:
  - **Fórmula**: $p_A + \gamma_1 h_1 = p_B + \gamma_2\,\ell_2\sin\theta + \gamma_3 h_3$
  - **Equivalente**: $p_A - p_B = \gamma_2\,\ell_2\sin\theta + \gamma_3 h_3 - \gamma_1 h_1$
  - **Variáveis**: $p_A, p_B$ (Pa), $\gamma_i=\rho_i g$ (N/m³), $h_1,h_3$ (m), $\ell_2$ (m), $\theta$ (rad ou °)
  - **Quando usar**: **pequenas variações de pressão**; reduzindo $\theta$ aumenta-se a sensibilidade (pois $\sin\theta$ pequeno para ângulos pequenos).

### Exercício (slides) — barômetro e incerteza de altura

- **Relação usada**: $L = \frac{\Delta P}{\rho g}$
- **Quando usar**: converter incerteza/variação de pressão em variação de altura (ar aproximado com $\rho$ constante no intervalo).

## 5) Trabalho (Work) — definição e formas comuns

### Trabalho de fronteira (pressão–volume)

Para processo **quase-estático** (quase em equilíbrio):

- **Elemento diferencial**: $\delta W = P\,dV$
- **Trabalho 1→2**:
  - **Fórmula**: $W_{1\to2} = \int_{V_1}^{V_2} P\,dV$
  - **Variáveis**: $W$ (J), $P$ (Pa), $V$ (m³)
- **Quando usar**: pistão/cilindro e outros sistemas com fronteira móvel, desde que $P$ do sistema esteja bem definido (quase-estático).

Se **pressão constante**:

- **Fórmula**: $W = P\Delta V = P\,(V_2 - V_1)$
- **Quando usar**: expansões/compressões a \(P\) constante (ou \(P_{ext}\) constante em não-equilíbrio, como no slide).

Para processo de **não-equilíbrio** com pressão externa constante \(P_0\) (slide):

- **Fórmula**: $W_{1\to2} = \int_1^2 P\,dV = P_0\,(V_2 - V_1)$
- **Quando usar**: quando a pressão interna oscila/varia, mas o trabalho “útil” é contra \(P_{ext}=P_0\).

### Trabalho em uma mola (linear)

- **Lei da mola**: $F = k(x-x_0)$
- **Elemento diferencial**: $\delta W = F\,dx$
- **Trabalho 1→2**:
  - **Fórmula**: $W_{1\to2} = \int_{x_1}^{x_2} k(x-x_0)\,dx$
  - **Resultado do slide**:
    
$$
W_{1\to2} = k\left[\frac{x_2^2-x_1^2}{2}-x_0(x_2-x_1)\right]
$$
  - **Variáveis**: \(k\) (N/m), \(x\) (m), \(x_0\) (m)
  - **Quando usar**: pistões com mola, sistemas massa–mola.

### Trabalho por tensão superficial (filme de líquido)

- **Tensão superficial**: $\sigma$ (N/m)
- **Trabalho (forma geral)**:
  - **Fórmula**: $W = -\int_1^2 \sigma\,dA$
  - **No arranjo do slide**: $W = -\int_1^2 \sigma\,2b\,dx$
  - **Variáveis**: \(A\) (m²), \(b\) (m), \(x\) (m)
  - **Quando usar**: criação/alongamento de área de interface (bolhas, películas).

### Trabalho por alongamento de um fio

- **Fórmula**: $W = -\int_1^2 F\,dL$
- **Variáveis**: \(F\) (N), \(L\) (m)
- **Quando usar**: tração em fios/barras quando o “deslocamento” é alongamento.

### Trabalho elétrico (potência)

- **Potência elétrica**:
  - **Fórmula**: $\dot{W} = E\,i$
  - **Variáveis**: $E$ (V), $i$ (A), $\dot{W}$ (W)
  - **Quando usar**: baterias/resistores/motores sob tensão e corrente conhecidas.

- **Trabalho em intervalo $\Delta t$** (se potência constante):
  - **Fórmula**: $W = \int \text{potência}\;dt = \text{potência}\cdot \Delta t$
  - **Quando usar**: carga/descarga com \(E\) e \(i\) constantes.

## 6) Energia potencial gravitacional

- **Variação de energia potencial**:
  - **Fórmula**: $\Delta EP = EP_2 - EP_1 = mg(z_2-z_1)$
  - **Variáveis**: $m$ (kg), $g$ (m/s²), $z$ (m)
  - **Quando usar**: variação de altura em problemas com gravidade (subidas/descidas).

## 7) Gás ideal (aparece nos exercícios)

- **Equação de estado**:
  - **Fórmula**: $PV = mRT$
  - **Variáveis**: $P$ (Pa), $V$ (m³), $m$ (kg), $R$ (J/(kg·K)), $T$ (K)
  - **Quando usar**: gases em condições moderadas (depende da espécie/pressão/temperatura).

## 8) Exercícios dos slides (com “receita” de solução)

### 4.35 — Cilindro–pistão, processo a pressão constante

- **Dados (slide)**: ar a $P=600\,\text{kPa}$, $T_1=290\,K$, $V_1=0{,}01\,m^3$, trabalho retirado $W=54\,kJ$, $P$ constante.
- **Fórmulas que entram**:
  - $W = P\Delta V$
  - $PV = mRT$ (para obter $T_2$ via razão $T_2/T_1 = (P_2V_2)/(P_1V_1)$; com $P_2=P_1\Rightarrow T_2/T_1 = V_2/V_1$)
- **Quando usar**: todo problema “pistão + \(P\) constante + trabalho informado”.

### 4.78 — Bolha/filme de sabão (tensão superficial)

- **Fórmulas que entram**:
  - $W = \int S\,dA \approx S\,\Delta A$ (no slide aparece a forma com $W = \int S\,dA$)
  - Áreas usadas no slide:
    - $A_1=\frac{\pi}{4}D^2$ (círculo)
    - $A_2=\frac{1}{2}\pi D^2$ (semiesfera: área curva $=2\pi r^2=\frac{1}{2}\pi D^2$)
  - Fator 2 (duas superfícies do filme): $W \approx 2\sigma\,\Delta A$
- **Quando usar**: quando o enunciado fala em “filme” (duas interfaces ar–líquido).

### 4.97 — Bateria bem isolada (trabalho elétrico)

- **Fórmulas que entram**:
  - $\dot{W} = E\,i$
  - $W = \dot{W}\,\Delta t$ (se constante)
- **Quando usar**: tensão e corrente constantes por um tempo.

### 4.119 / 4.126 / 4.128 / 4.61 — exercícios adicionais listados

- **Ferramentas típicas (conforme tema dos slides)**:
  - Trabalho de fronteira: $W=\int P\,dV$ (isotérmico: $P\propto 1/V$ se gás ideal)
  - Pressão hidrostática/manometria: $P_2-P_1=\rho g\Delta z$
  - Gás ideal: $PV=mRT$
- **Quando usar**: sempre que o enunciado for “cilindro–pistão”, “compressão/expansão”, “tanque com gás acima do líquido”, “pressão vs altura”.

