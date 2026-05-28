# Introdução e conceitos

- Alguns conceitos fundamentais
- Dimensões e sistema de unidades
- Algumas propriedades da matéria de interesse nas ciências térmicas

## O Sistema nas ciências térmicas

**O que é um sistema (ou sistema fechado)?**

- É uma quantidade de matéria, com massa e identidades fixas.
  - Tudo que é externo ao sistema é denominado ambiente ou vizinhança.
    - O sistema é separado do ambiente pela fronteira.

**O que é um volume de controle (ou sistema aberto)?**

- Um volume que envolve um equipamento ou uma série de equipamentos, ou um pedaço ou uma série de pedaços de um equipamento.
  - O entorno do volume de controle é chamado de superfície de controle.
  - Massa, calor e trabalho podem atravessar a superfície de controle.

## Fase, propriedades da matéria e estado

- Uma fase é uma quantidade de materia que é fisicamente homogênea
- As três fases básicas da matéria são o sólido, líquido e gasoso
  - Os líquidos e gases são *fluidos* e fluem quando estão sujeitos à tensão de cisalhamento
  - Um *sólido* não flui ou expande para tomar forma ou volume no recipiente
  - Um *líquido* flui para tomar a forma do recipiente, mas não se expande para preencher todo o volume disponível
  - Um *gás* toma forma e expande-se para preencher todo o volume do recipiente

- *Propriedades* são certas características da materia como pressão, temperatura, volume específico, etc, que podem ser medidas direta ou indiretamente.
  - *Propriedades extensivas*, como volume e peso, dependem da massa do sistema.
  - *Propriedades intensivas*, como temperatura e pressão, não dependem da massa do sistema.

![Propriedades extensivas e intensivas](Slide%201/5.png)

- Um *estado de um sistema* é definido por um conjunto de valores para as propriedades de determinada substância.
  - **Estado 1:** p = 400 kPa, T = 300 K, v = 0,3861 m³/kg , fase gasosa
  - **Estado 2:** p = 800 kPa, T = 300 K, v = 0,1917 m³/kg , fase gasosa
- Uma fase tem infinitos estado
- Para uma substância pura em uma única fase, são necessárias duas propriedades independentes para especificar um estado.

- O diferencial de uma propriedade é exato

$$\int_{f_1}^{f_2} df = f_2 - f_1$$

- As funções trabalho e de quantidade de calor não têm um valor em determinado estado, sendo dependentes do processo de mudança de um estado a outro.
- O diferencial de uma função que depende do processo ou da trajetória é inexato

$$\int_{estado1}^{estado2} \delta W = W_{1-2}$$

## Dimensões e Unidades

- As dimensões descrevem uma quantidade (ex. propriedade)
- As unidades são magnitudes destas dimensões
- As dimensões primárias são massa, comprimento, tempo, a intensidade de luz, a corrente elétrica, a temperatura e a quantidade de matéria.
- As dimensões derivadas são uma combinação de dimensões primárias
  - A velocidade é o comprimento dividido pelo tempo
  - A aceleração é o comprimento dividido pelo tempo ao quadrado
  - A força e energia também são dimensões derivadas

## Dimensões e sistemas de unidades

Todas as equações teóricas são dimensionalmente homogêneas, ou seja, as dimensões dos lados esquerdo e direito da equação são iguais e todos os termos aditivos separáveis que compõe a equação precisam apresentar a mesma dimensão. Nós aceitamos como premissa fundamental que todas as equações que descrevem os fenômenos físicos são dimensionalmente homogêneas. Se isto não for verdadeiro, nós estaremos igualando quantidades físicas diversas e isto não faz sentido. Por exemplo, a equação para a velocidade de um corpo uniformemente acelerado é

$$V = V_0 + at \quad (1.1)$$

onde $V_0$ é a velocidade inicial, $a$ é a aceleração e $t$ é o intervalo de tempo. Em termos dimensionais, a forma desta equação é

$$LT^{-1} \doteq LT^{-1} + LT^{-1}$$

### Tabela 1.1 Dimensões Associadas a Algumas Quantidades Físicas Usuais

| Quantidade Física | Sistema FLT | Sistema MLT |
| :--- | :--- | :--- |
| Aceleração | $LT^{-2}$ | $LT^{-2}$ |
| Aceleração angular | $T^{-2}$ | $T^{-2}$ |
| Ângulo | $F^0 L^0 T^0$ | $M^0 L^0 T^0$ |
| Área | $L^2$ | $L^2$ |
| Calor | $FL$ | $ML^2 T^{-2}$ |
| Calor específico | $L^2 T^{-2} \Theta^{-1}$ | $L^2 T^{-2} \Theta^{-1}$ |
| Comprimento | $L$ | $L$ |
| Deformação (relativa) | $F^0 L^0 T^0$ | $M^0 L^0 T^0$ |
| Energia | $FL$ | $ML^2 T^{-2}$ |
| Força | $F$ | $MLT^{-2}$ |
| Freqüência | $T^{-1}$ | $T^{-1}$ |
| Massa | $FL^{-1} T^2$ | $M$ |
| Massa específica | $FL^{-4} T^2$ | $ML^{-3}$ |
| Módulo de elasticidade | $FL^{-2}$ | $ML^{-1} T^{-2}$ |
| Momento de inércia (área) | $L^4$ | $L^4$ |
| Momento de inércia (massa) | $FLT^2$ | $ML^2$ |
| Momento de uma força | $FL$ | $ML^2 T^{-2}$ |
| Peso específico | $FL^{-3}$ | $ML^{-2} T^{-2}$ |
| Potência | $FLT^{-1}$ | $ML^2 T^{-3}$ |
| Pressão | $FL^{-2}$ | $ML^{-1} T^{-2}$ |
| Quantidade de movimento | $FT$ | $MLT^{-1}$ |
| Temperatura | $\Theta$ | $\Theta$ |
| Tempo | $T$ | $T$ |
| Tensão | $FL^{-2}$ | $ML^{-1} T^{-2}$ |
| Tensão superficial | $FL^{-1}$ | $MT^{-2}$ |
| Torque | $FL$ | $ML^2 T^{-2}$ |
| Trabalho | $FL$ | $ML^2 T^{-2}$ |
| Velocidade | $LT^{-1}$ | $LT^{-1}$ |
| Velocidade angular | $T^{-1}$ | $T^{-1}$ |
| Viscosidade cinemática | $L^2 T^{-1}$ | $L^2 T^{-1}$ |
| Viscosidade dinâmica | $FL^{-2} T$ | $ML^{-1} T^{-1}$ |
| Volume | $L^3$ | $L^3$ |

## Dimensões e Unidades

- Existem dois sistemas principais de unidades
  - O Sistema Britânico (gravitacional ou de engenharia) utilizado nos Estados Unidos e Reino Unido.
  - O SI (sistema métrico internacional) é utilizado pela maioria dos outros países

## Sistema SI

- As unidades primárias para o SI são:
  - Metro (m) para o comprimento
  - Segundo (s) para o tempo
  - Quilograma (kg) para a massa
  - Grau Celsius (°C) ou Kelvin (K) para a temperatura
  - Ampere (A) para corrente elétrica
  - Candela (cd) para a intensidade de luz
  - O mol para a quantidade de materia
- A unidade de força, o newton (N), é a força necessária para acelerar uma massa de um quilograma em um metro por segundo ao quadrado.

$$1 \text{ N} = 1 \text{ kg} \cdot \text{m/s}^2$$

## Sistemas de unidades

### Tabela 1.2 Prefixos Utilizados no SI

| Fator de Multiplicação da Unidade | Prefixo | Símbolo |
| :--- | :--- | :--- |
| $10^{12}$ | tera | T |
| $10^9$ | giga | G |
| $10^6$ | mega | M |
| $10^3$ | kilo | k |
| $10^2$ | hecto | h |
| 10 | deca | de |
| $10^{-1}$ | deci | d |
| $10^{-2}$ | centi | c |
| $10^{-3}$ | mili | m |
| $10^{-6}$ | micro | $\mu$ |
| $10^{-9}$ | nano | n |
| $10^{-12}$ | pico | p |
| $10^{-15}$ | fento | f |
| $10^{-18}$ | ato | a |

## O Sistema Britânico (ou Inglês)

- As unidades primárias para o Sistema Britânico são:
  - Pé (ft) para o comprimento
  - Segundo (s) para o tempo
  - Slug (BG) ou libra (lbm) (EE) para a massa
  - Grau fahrenheit (ºF) ou grau Rankine (ºR) para a temperatura
  - Ampere (A) para corrente elétrica
  - A Candela (cd) para a intensidade de luz
  - O mol para a quantidade de materia
- Uma constante proporcional é definida entre a libra-massa e o slug

$$1 \text{ slug} = 32{,}2 \text{ lbm}$$

- A força no Sistema Britânico é normalmente indicada por libra-força (lbf).
- A pressão no Sistema Britânico é normalmente indicada em libra-força por polegada ao quadrado (lbf/in² ou psi) ou libra-força por pé quadrado (lbf/ft² ou psf), sendo que as pressões manométricas recebem um g ao final da unidade ficando psig e psfg
- A energia no Sistema Britânico é normalmente indicada como lbf.ft quando está relacionada a trabalho e como BTU quando está relacionada a calor ou com propriedades termodinâmicas.

## Sistemas de unidades

*Sistema Britânico gravitacional (BG)*

$$ft,\ slug\ (lbm,\ \text{no sistema Inglês de engenharia}),\ s,\ lbf,\ ^\circ R$$

$1\ slug = 32{,}174\ lbm$

*Sistema International (SI)*

$$m,\ kg,\ s,\ N,\ K$$

![Conversões e definições de unidades](Slide%201/18.png)

### Exercícios 1.19–1.21

**1.19** Deduza os seguintes fatores de conversão:

- (a) Converta uma viscosidade de $1\ \text{m}^2/\text{s}$ para $\text{ft}^2/\text{s}$.
- (b) Converta uma potência de $100\ \text{W}$ para horsepower.
- (c) Converta uma energia específica de $1\ \text{kJ}/\text{kg}$ para $\text{Btu}/\text{kg}$.

**1.20** Deduza os seguintes fatores de conversão:

- (a) Converta uma pressão de $1\ \text{psi}$ para $\text{kPa}$.
- (b) Converta um volume de $1\ \text{litro}$ para galões.
- (c) Converta uma viscosidade de $1\ \text{lbf}\cdot\text{s}/\text{ft}^2$ para $\text{N}\cdot\text{s}/\text{m}^2$.

**1.21** Deduza os seguintes fatores de conversão:

- (a) Converta um calor específico de $4{,}18\ \text{kJ}/\text{kg}\cdot\text{K}$ para $\text{Btu}/\text{lbm}\cdot^\circ\text{R}$.
- (b) Converta uma velocidade de $30\ \text{m}/\text{s}$ para $\text{mph}$.
- (c) Converta um volume de $5{,}0\ \text{L}$ para $\text{in}^3$.

**Horsepower (HP):** $1\ \text{hp} = 745{,}7\ \text{watts}$ — $\Delta t = 1\ \text{s}$, $\Delta h = 1\ \text{ft}$, $m = 550\ \text{lb}$.

**The metric horsepower (CV):** $1\ \text{hp} = 735{,}5\ \text{watts}$ — $\Delta t = 1\ \text{s}$, $\Delta h = 1\ \text{m}$, $m = 75\ \text{kg}$.

BTU é a energia necessária para elevar a temperatura de uma libra de água de um grau Fahrenheit, $C_p=4{,}189\ \text{kJ}/\text{kg}\cdot\text{K} @ 15\ ^\circ\text{C}$

O galão líquido americano é definido como $231\ \text{in}^3$.

A primeira vez que o termo milha foi usado para denotar distância foi na Roma Antiga, onde valia $1\ 000$ passos (do latim, mille passus) dados pelo Centurião, ou $5\ 000$ pés romanos ($5\ 280$ pés desde XIII).

Litro corresponde à quantidade de líquido que cabe exatamente dentro de um cubo com $1\ \text{dm}$ de aresta, de modo que o cubo fique completamente cheio.

### Exercícios 1.34, 1.35, 1.39

**1.34** O livre caminho médio $\lambda$ de uma molécula de gás é a distância média que ela percorre antes de colidir com outra molécula. Ele é dado por

$$\lambda = C \frac{m}{\rho d^2}$$

em que $m$ e $d$ são a massa da molécula e o diâmetro, respectivamente, e $\rho$ é a massa específica do gás. Qual são as dimensões da constante $C$ para uma equação dimensionalmente correta?

**1.35** No Capítulo 9, estudaremos a aerodinâmica e aprenderemos que a força de arrasto $F_D$ sobre um corpo é dada por

$$F_D = \frac{1}{2} \rho V^2 A C_D$$

Assim, o arrasto depende da velocidade $V$, da massa específica $\rho$ do fluido e do tamanho do corpo (indicado pela área frontal $A$) e sua forma (indicado pelo coeficiente de arrasto $C_D$). Qual são as dimensões de $C_D$?

**1.39** Uma determinada bomba tem sua equação característica de desempenho, relacionando a altura manométrica $H$ com a vazão $Q$, dada por:

$$H\ (\text{ft}) = 1{,}5 - 4{,}5 \times 10^{-5}\ [Q\ (\text{gpm})]^2$$

Quais são as unidades dos coeficientes $1{,}5$ e $4{,}5 \times 10^{-5}$? Deduza uma versão SI dessa equação.

## Algumas propriedades de interesse nas ciências térmicas

- Energia
- Temperatura
- Massa específica e volume específico
- Pressão
- Pressão de vapor

## Algumas propriedades da materia

Nas ciências térmicas clássica, assume-se que as características e propriedades dos fluidos (pressão, temperatura, etc) variam (quando variam) de forma continua através da materia (**hipótese do meio contínuo**).

Hipótese deixa de ser válida em gases rarefeitos (i.e. quando a trajetória livre média das moléculas torna-se da mesma ordem de grandeza da menor dimensão característica significativa do problema).

$O_2$ — $1\ \text{atm},\ 20\ ^\circ\text{C}$ — $3 \times 10^{16}$ moléculas/mm³ — Vazio

## Energia

- A energia é uma propriedade relacionada a capacidade do sistema de causar alterações na sua vizinhança.
- A energia pode ter muitas formas diferentes.
- Nas ciências térmicas o foco está, principalmente, nas energias cinética, potencial e interna.
  - Porém, muitas vezes, as energias cinética e potencial são negligenciáveis, restando apenas a energia interna.
- A ***energia interna*** é a soma de todas as energias associadas com a estrutura interna e com a atividade atômica e molecular do sistema.
  - Energia molecular de translação, rotação e **vibração**
  - Energia química: ligações inter e intra moleculares ou atômicas.
  - Energia atômica: ligação entre as partículas nucleares.

**Figura 2.4** Sistema de coordenadas para uma molécula diatômica.

**Figura 2.5** Os três principais modos de vibração para a molécula de $H_2O$.

![Energia — Figuras 2.4 e 2.5](Slide%201/22.png)

## Algumas considerações sobre a energia interna

**FIGURA 2-5** As diversas formas microscópicas de energia que constituem a energia sensível:

- Translação molecular
- Rotação molecular
- Translação do elétron
- Vibração molecular
- Spin do elétron
- Spin do núcleo

**FIGURA 2-6** A energia interna de um sistema é a soma de todas as formas microscópicas de energia:

- Energias sensível e latente
- Energia química
- Energia nuclear

- **Energia sensível:** a porção da energia interna de um sistema associado às energias cinéticas das moléculas.
- **Energia latente:** energia interna associada à fase de um sistema (ligação entre as moléculas).
- **Energia química:** energia interna associada às ligações atômicas em uma molécula.
- **Energia nuclear:** a tremenda quantidade de energia associada aos fortes laços dentro do núcleo do próprio átomo.

**TÉRMICA = Sensível + Latente**

**INTERNA = Sensível + Latente + Química + Nuclear**

![Considerações sobre energia interna](Slide%201/23.png)

## Temperatura

- A *temperatura* é proporcional à quantidade de energia térmica contida em uma substância
  - Medida indireta da agitação molecular
- A *lei zero da termodinâmica* afirma que se dois corpos (A e B) estão em equilíbrio térmico com um terceiro corpo (C), eles também estão em equilíbrio térmico um com o outro
  - A base para a medição da temperatura
  - **C** é o termômetro, **A** o meio de calibração e **B** o meio onde se deseja conhecer a temperatura

- Sistemas entram em equilíbrio térmico através da transferência de calor (energia)
  - Sistema adiabático não troca calor com outros sistemas
- Sensação de quente e frio está relacionado com temperatura e com taxa de transferência de calor
  - Quando na mesma temperatura
    - Metal parece mais frio que madeira
  - Sentimos mais “frio” dentro da água que no ar
  - É possível que um objeto esteja mais quente que o outro se ambos estiverem a mesma temperatura?

## Escalas de Temperatura

- Escala de temperatura é uma maneira de quantificar e comparar a temperatura de diferentes sistemas
- Escalas absolutas (da temperatura zero até infinito, também chamada de temperatura termodinâmica ou absoluta)
  - Kelvin (K) no SI e Rankine (°R) no BG
- Escalas relativas (a temperatura zero é escolhido arbitrariamente)
  - Celsius (°C) no SI e Fahrenheit (°F) no BG

- Ponto de congelamento da água: 273,15 K, 0 °C, 459,67 °R, 32 °F
- Ponto de ebulição da água a 1 atm: 373,15 K, 100 °C, 639,67 °R, 212 °F
- Conversão entre as escalas:
  - $K = °C + 273{,}15$
  - $°R = °F + 459{,}67$
  - $°F = 32 + (9/5)\ °C$
  - $\Delta T$: $1\ C° = 1\ K = (9/5)\ F° = (9/5)\ R°$

## Medição de Temperatura

- Os termômetros à expansão de líquido dependem da expansão de um líquido à medida que a temperatura muda (o coeficiente da expansão térmica)
- As lâminas bimetálicas, que dobram à medida que a temperatura muda, são frequentemente utilizadas em termostatos
- Os termopares e os termistores podem ser utilizados para relacionar valores de temperatura com valores de sinais elétricos

## Massa especifica, volume específico, peso específico e densidade

a) Massa específica ($\rho$) é massa por unidade de volume.

b) Volume específico ($v$) é o recíproco da $\rho$.

$$v = \frac{1}{\rho}$$

c) Peso específico ($\gamma$) é o peso por unidade de volume.

$$\gamma = \rho g$$

d) Densidade é a razão entre a massa específica de um fluido e a massa específica de outro fluido em uma temperatura específica (normalmente água a 4 °C ou a 39,2°F).

$$SG = \frac{\rho}{\rho_{H_2O@4^\circ C}}$$

![Massa específica, volume específico, peso específico e densidade](Slide%201/30.png)

## PRESSÃO

- Força normal por unidade de área
- Força é uma grandeza vetorial, pressão é uma grandeza escalar
- Pressão que um fluido exerce sobre uma superfície de contato é resultado da colisão de partículas deste fluido
- Pressão pode ser manométrica ou absoluta
  - Pressão manométrica pode ser negativa
  - Pressão absoluta é sempre positiva

**Pressure**

- $1\ \text{Pa} = 1\ \text{N/m}^2$
- $1\ \text{bar} = 10^5\ \text{Pa} = 0{,}1\ \text{MPa}$
- $1\ \text{atm} = 101{,}325\ \text{Pa} = 101{,}3\ \text{kPa}$

**Gage versus Absolute Pressure**

Vácuo Absoluto — Pressão Atmosférica — Pressão Absoluta — Pressão Relativa — Vácuo

$P_{abs} = 0$ — $P_{atm} = 101{,}3\ \text{kPa}$

$P_{abs,1} = 200\ \text{kPa}$ — $P_{gage,1} = P_{abs,1} - P_{atm} = 98{,}7\ \text{kPa}$

$P_{abs,2} = 30\ \text{kPa}$ — $P_{gage,2} = P_{abs,2} - P_{atm} = -71{,}3\ \text{kPa}$

![Pressão — unidades e manométrica vs absoluta](Slide%201/32.png)

## Pressão vapor ou de saturação

- Um líquido evapora porque algumas moléculas na superfície do líquido tem quantidade de movimento suficiente para superar as forças intermoleculares coesivas.
- Pressão na qual coexistem a fase líquida e gasosa de uma substância.
- A pressão de saturação está relacionada com atividade molecular, e portanto, com temperatura.
- Quando há coexistência dessas de duas ou mais fases, diz-se que a substância está saturada.
- Quando uma susbstância encontra-se saturada e com temperatura constante em um reservatório fechado, a quantidade de moleculas entrando e saíndo da fase líquida é aproximadamente a mesma.
- A pressão de vapor é uma medida da tendência de evaporação de um líquido.
  - Quanto maior for a sua pressão de vapor, mais volátil será o líquido, e menor será sua temperatura de ebulição relativamente a outros líquidos com menor pressão de vapor à mesma temperatura de referência.

Além das propriedades encontradas quando uma substância encontra-se em uma única fase, na condição de saturação, defini-se uma outra propriedade que relaciona a quantidade de matéria na fase gasosa com a quantidade de materia total

- Na saturação, pressão e temperatura não são independentes
- Defini-se o título ($x$) para auxiliar na especificação de um estado
- O título as vezes é denominado qualidade ou *quality* em textos em Inglês
- O título pode ser apresentado como uma fração com valor entre 0 (líquido saturado) e 1 (vapor saturado) ou como um percentual entre 0 e 100 %

$$V = V_{liq} + V_{vap} = m_{liq}v_f + m_{vap}v_g$$

$$v = \frac{V}{m} = \frac{m_{liq}}{m}v_f + \frac{m_{vap}}{m}v_g = (1 - x)v_f + xv_g$$

$$x = m_{vap}/m \qquad v_{fg} = v_g - v_f \qquad v = v_f + xv_{fg} \qquad x = (v - v_f)/v_{fg}$$

## O Gás Ideal

A lei do gás ideal relaciona a pressão, a temperatura e o volume específico dos gases

$$Pv = RT$$

$R$ depende do gás e é igual a $R_u \div M$

Em que $R_u$ é a constante universal do gás ($8{,}314\ \text{J/mol·K}$) e $M$ é a massa molar do gás

## Formas Alternativas da Lei do Gás Ideal e quando considerar um gás como ideal

A lei do gás ideal também pode ser representada como

$$PV = mRT$$

$$PV = NR_uT$$

$$P = \rho RT$$

$N$ é o número de mols do gás

Se o estado da substância não é próximo do estado de saturação, pode-se considerá-la como um gas ideal

**Como definir se estado é próximo ou não da saturação?**

- Quando a massa especifica for baixa, i.e., quando a pressão for baixa e a temperatura for alta.

**E como definir quando a pressão é baixa e quando a temperatura é alta?**

![Figura 3.21 Diagrama temperatura–volume específico para a água](Slide%201/37.png)

**Atenção:** Quando a $P \downarrow$, o erro $\downarrow$ mesmo em temperaturas muito próximas da saturação.

**Se a $P$ for constante, o erro $\downarrow$ quando $T \uparrow$.**

Para evitar ambiguidade, define-se o fator de compressibilidade:

$$Z = \frac{Pv}{RT}$$

**Quanto é Z para um gás ideal?**

$Pv = ZRT$ — $Pv = 1RT$

![Figura 3.22 Compressibilidade do nitrogênio](Slide%201/38.png)

Na falta de uma tabela de compressibilidade específica para uma determinada substância, usa se uma tabela geral, baseada nas propriedades reduzidas.

![Figura D.1 — Fator de compressibilidade para o fluido de Lee-Kesler simples](Slide%201/39.png)

$$P_r = \frac{P}{P_c} \qquad T_r = \frac{T}{T_c}$$

## Método de Resolução de Problemas

- Um procedimento sistemático geral pode ser utilizado para resolver os problemas termodinâmicos
  - Leia o enunciado e identifique as informações
  - Esboce uma figura do sistema ou do volume de controle
  - Liste as informações dadas para todos os estados
  - Verifique os processos especiais
  - Estabeleça as hipóteses utilizadas
  - Determine os estados e/ou as propriedades necessários
  - Aplique as equações apropriadas
  - Verifique sua resposta

## Alguns exercícios

**1.4** Se $P$ é uma força e $x$ um comprimento, quais serão as dimensões (no sistema $FLT$) de (a) $dP/dx$, (b) $d^3P/dx^3$, e (c) $\int P\,dx$ ?

**1.5** Se $p$ é uma pressão, $V$ uma velocidade e $\rho$ a massa específica de um fluido, quais serão as dimensões (no sistema $MLT$) de (a) $p/\rho$, (b) $pV\rho$, e (c) $p/(\rho V^2)$.

**1.12** Uma equação que é utilizada para estimar a vazão em volume, $Q$, do escoamento no vertedor de uma barragem é

$$Q = C \sqrt{2g}\ B\ \left(H + \frac{V^2}{2g}\right)^{3/2}$$

onde $C$ é uma constante, $g$ é a aceleração da gravidade, $B$ é a largura do vertedor, $H$ é a espessura da lâmina de água que escoa sobre o vertedor e $V$ é a velocidade do escoamento de água a montante do vertedor.

Esta equação é válida em qualquer sistema de unidades? Justifique sua resposta.

**1.19** Verifique as relações de conversão para (a) aceleração, (b) massa específica, (c) pressão e (d) vazão em volume da Tab. 1.4. Utilize as seguintes relações básicas de conversão: $1\ \text{m} = 3{,}2808\ \text{ft}$; $1\ \text{N} = 0{,}22481\ \text{lb}$ e $1\ \text{kg} = 0{,}068521\ \text{slug}$.

**1.26** Um tanque cilíndrico, rígido e aberto para a atmosfera contém $4\ \text{ft}^3$ de água. Inicialmente, a temperatura da água é igual a $40\ ^\circ\text{F}$. Transfere-se calor à água até que sua temperatura atinja $90\ ^\circ\text{F}$. Determine a variação do volume da água contida no tanque neste processo. Utilize as propriedades da água indicadas no Apen. B para resolver o problema. Admitindo que o diâmetro do tanque é igual a $2\ \text{ft}$, determine a variação do nível da água detectada no processo descrito.

**1.36** Uma câmara de pneu, com volume interno igual a $0{,}085\ \text{m}^3$, contém ar a $26\ \text{psi}$ (relativa) e $21\ ^\circ\text{C}$. Determine a massa específica e o peso do ar contido na câmara.

**1.43** O tempo necessário para retirar uma certa quantidade de líquido de um reservatório, $t$, é função de vários parâmetros e a viscosidade cinemática do fluido, $\nu$, é importante nesse processo (veja o $\odot$ 1.1). Nós medimos, num laboratório, o tempo necessário para retirar 100 ml de vários óleos que apresentavam mesma massa específica mas viscosidades diferentes. O volume do béquer utilizado nos experimentos é igual a 150 ml e a inclinação do béquer na operação de esvaziamento foi mantida constante. Os resultados obtidos nos experimentos são bem representados pela equação

$$t = 1 + 9 \times 10^2 \nu + 8 \times 10^3 \nu^2$$

onde $\nu$ está em $\text{m}^2/\text{s}$.

(a) A equação apresentada é do tipo homogênea geral? Justifique sua resposta.

(b) Compare os tempos necessários para retirar 100 ml de óleo SAE 30 a 0 e a 60 °C do béquer de 150 ml. Utilize a Fig. B.2 do Apen. B para determinar o valor da viscosidade do óleo.

![Viscosidade cinemática vs temperatura](Slide%201/44.png)

**1.81** Um tanque fechado contém álcool etílico a 20 °C e não está totalmente cheio. Se o ar acima do álcool é evacuado, qual é a pressão absoluta mínima que se desenvolve no espaço acima do líquido?

**2.31** A aceleração da gravidade na superfície da Lua é aproximadamente igual a 1/6 daquela referente à superfície da Terra. Uma massa de 5 kg é 'pesada' numa balança de braço na superfície da Lua. Qual é a leitura esperada? Se a pesagem fosse efetuada numa balança de mola, calibrada corretamente num ponto em que a aceleração...

Moon gravitation is: $g = g_{earth}/6$

Beam Balance Reading is **5 kg** — This is mass comparison

Spring Balance Reading is in kg units — Force comparison length $\propto$ F $\propto$ g — Reading will be **5/6 kg**

![Balança de braço e de mola na Lua](Slide%201/46.png)

**2.36** Uma central de potência separa $CO_2$ dos gases de exaustão da planta. O $CO_2$ é então comprimido para uma condição em que a massa específica é de $110\ \text{kg/m}^3$ e armazenado em uma jazida de carvão inexplorável, que contém em seus poros um volume de vazios de $100\ 000\ \text{m}^3$. Determine a massa de $CO_2$ que pode ser armazenada.

$$m = \rho V = 110\ \text{kg/m}^3 \times 100\ 000\ \text{m}^3 = 11 \times 10^6\ \text{kg}$$

Just to put this in perspective a power plant that generates $2000\ \text{MW}$ by burning coal would make about $20\ \text{million tons}$ of carbon-dioxide a year. That is $2000$ times the above mass so it is nearly impossible to store all the carbon-dioxide being produced.

**2.48** Um reservatório de $1\ \text{m}^3$ tem $400\ \text{kg}$ de granito, $200\ \text{kg}$ de areia, $0{,}2\ \text{m}^3$ de água a $20\ ^\circ\text{C}$. Qual é a massa específica no interior do reservatório?

Dados:

- massa específica do granito = $2630\ \text{kg/m}^3$
- massa específica da areia = $1515\ \text{kg/m}^3$
- massa específica do ar = $1{,}21\ \text{kg/m}^3$ (a $20\ ^\circ\text{C}$)

![Reservatório com granito, areia e água](Slide%201/48.png)

**2.40** Um recipiente fechado e com volume de $5\ \text{m}^3$ contém $900\ \text{kg}$ de granito e ar (massas específicas respectivamente iguais a $2400$ e $1{,}15\ \text{kg/m}^3$). Determine a massa de ar contida no recipiente e o volume específico médio do arranjo.

**2.40** A $5\ \text{m}^3$ container is filled with $900\ \text{kg}$ of granite (density $2400\ \text{kg/m}^3$) and the rest of the volume is air with density $1{,}15\ \text{kg/m}^3$. Find the mass of air and the overall (average) specific volume.

$$m_{air} = \rho V = \rho_{air}\left(V_{tot} - \frac{m_{granite}}{\rho}\right) = 1{,}15\left[5 - \frac{900}{2400}\right] = 1{,}15 \times 4{,}625 = \mathbf{5{,}32\ \text{kg}}$$

$$v = \frac{V}{m} = \frac{5}{900 + 5{,}32} = \mathbf{0{,}005\ 52\ \text{m}^3/\text{kg}}$$

Because the air and the granite are not mixed or evenly distributed in the container the overall specific volume or density does not have much meaning.

**Atenção:** a pergunta em inglês é explícita ao indicar que há $900\ \text{kg}$ de granito. A pergunta em português é dúbia, pois pode se entender que são $900\ \text{kg}$ só de granito ou $900\ \text{kg}$ de uma mistura granito e ar.

**2.41** O diâmetro do pistão de um macaco hidráulico é igual a 200 mm. Determine a pressão no cilindro para que o pistão levante uma massa de 740 kg.

Force acting on the mass by the gravitational field

$F\downarrow = ma = mg = 740 \times 9{,}80665 = 7256{,}9\ \text{N} = 7{,}257\ \text{kN}$

Force balance:

$F\uparrow = (P - P_0)A = F\downarrow \implies P = P_0 + F\downarrow / A$

$A = \pi D^2 (1/4) = 0{,}031416\ \text{m}^2$

$P = 101\ \text{kPa} + \frac{7{,}257\ \text{kN}}{0{,}031416\ \text{m}^2} = 332\ \text{kPa}$

![Macaco hidráulico](Slide%201/50.png)

**2.50** Um tornado arrancou o teto horizontal de um galpão. A área e o peso do teto são, respectivamente, iguais a $100\ \text{m}^2$ e $1000\ \text{kg}$. Qual é a pressão mínima necessária (vácuo) para que isso ocorra? Admita que o teto estava simplesmente apoiado.

The net force on the roof is the difference between the forces on the two sides as the pressure times the area

$F = P_{inside} A - P_{outside} A = \Delta P A$

That force must overcome the gravitation $mg$, so the balance is

$\Delta P A = mg$

$$\Delta P = \frac{mg}{A} = \frac{1000\ \text{kg} \times 9{,}807\ \text{m/s}^2}{100\ \text{m}^2} = 98\ \text{Pa} = 0{,}098\ \text{kPa}$$

Remember that kPa is $\text{kN/m}^2$.

![Tornado e galpão](Slide%201/51.png)

**2.68** Um barômetro que apresenta imprecisão de medida igual a 1 mbar (0,001 bar) foi utilizado para medir a pressão atmosférica no nível do chão e na cobertura de um edifício alto. Determine a incerteza no valor da altura do prédio calculada a partir dos valores das pressões atmosféricas medidas.

**2.68** Assume we use a pressure gauge to measure the air pressure at street level and at the roof of a tall building. If the pressure difference can be determined with an accuracy of 1 mbar (0.001 bar) what uncertainty in the height estimate does that corresponds to?

$\rho_{air} = 1{,}169\ \text{kg/m}^3$ from Table A.5

$\Delta P = 0{,}001\ \text{bar} = 100\ \text{Pa}$

$$L = \frac{\Delta P}{\rho g} = \frac{100}{1{,}169 \times 9{,}807} = 8{,}72\ \text{m}$$

**Atenção:** a pergunta em inglês é diferente da pergunta em português. A resposta da pergunta em português é duas vezes a resposta da pergunta em inglês.

![Barômetro](Slide%201/52.png)

**2.89** O diâmetro do pistão mostrado na Figura P2.89 é 100 mm e sua massa é 5 kg. A mola é linear e não atua sobre o pistão enquanto este estiver encostado na superfície inferior do cilindro. No estado mostrado na figura, o volume da câmara é 0,4 L e a pressão é 400 kPa. Quando a válvula de alimentação de ar é aberta, o pistão sobe 20 mm. Admitindo que a pressão atmosférica seja igual a 100 kPa, calcule a pressão no ar nesta nova situação.

![Figura P2.89 — pistão, mola e solução](Slide%201/53.png)

A linear spring has a force linear proportional to displacement. $F = k \cdot x$, so the equilibrium pressure then varies linearly with volume: $P = a + bV$, with an intersect $a$ and a slope $b = dP/dV$. Look at the balancing pressure at zero volume ($V \to 0$) when there is no spring force $F = PA = P_0 A + m_p g$ and the initial state. These two points determine the straight line shown in the P-V diagram.

**Piston area** $= A_p = (\pi/4) \times 0{,}1^2 = 0{,}00785\ \text{m}^2$

$a = P_0 + \frac{m_p \cdot g}{A_p} = 100\ \text{kPa} + \frac{5 \times 9{,}80665}{0{,}00785}\ \text{Pa} = 106{,}2\ \text{kPa}$ (intersect for zero volume).

$V_2 = 0{,}4 + 0{,}00785 \times 20 = 0{,}557\ \text{L}$

$$P_2 = P_1 + \frac{dP}{dV} \Delta V$$

$$P_2 = 400 + \frac{(400 - 106{,}2)}{0{,}4 - 0} \cdot (0{,}557 - 0{,}4)$$

$$P_2 = \mathbf{515{,}3\ \text{kPa}}$$
