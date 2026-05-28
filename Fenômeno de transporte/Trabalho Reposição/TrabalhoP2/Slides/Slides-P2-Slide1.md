# Conservação de energia (1ª lei da termodinâmica)

## Observações (correções)

No slide 26 considere

$$t_f = \frac{M(u_l - u_s)\,L}{6W^2 k\,(T_1 - T_f)}$$

sendo $u_l$ e $u_s$ retiradas das tabelas do apêndice B (B.1.2 e B.1.5).

No slide 29 considere $T_{\text{ar}} = 25\,^{\circ}\text{C}$ ao invés de $T_s = 25\,^{\circ}\text{C}$.

---

## CONSERVAÇÃO DE ENERGIA (1ª LEI DA TERMODINÂMICA)

- Uma ferramenta importante na análise de problemas de transferência de calor, geralmente possibilitando a determinação da **temperatura** do sistema.
- Formas de utilizá-la em relação ao
  - **tempo**
    - Em um instante
    - ou
    - Em um intervalo de tempo
  - **local da análise**
    - Sistema
    - Volume de controle
    - Superfície de controle (caso especial de volume de controle)

## 1ª LEI

**Em um instante**

- $\dot{E}_e$, $\dot{E}_s$: Taxa de energia (térmica ou mecânica), que atravessa a superfície de controle através de transferência de calor, e ou trabalho e ou de escoamento de massa (apenas para V.C.)
- $\dot{E}_{\text{ar}}$: Taxa com que a energia é armazenada no sistema.

$$\dot{E}_e - \dot{E}_s = \frac{dE_{\text{ar}}}{dt} = \dot{E}_{\text{ar}}$$

Cada termo tem uma unidade de J/s or W.

**Em um Intervalo de tempo**

$$E_e - E_s = \Delta E_{\text{ar}}$$

Cada termo tem a unidade de J.

**Fig. 1.7** Conservação de energia para um volume de controle. Aplicação em um determinado instante.

![1ª lei — volume de controle](Slide%201/2.png)

## Outras de descrever a conservação de energia

**(i) Em um processo transiente para um sistema fechado de massa (M),**

transferência de calor para o sistema é energia entrando

e trabalho feito pelo sistema é energia saindo

- $Q$ (entrada), $W$ (saída), $\Delta U$ no sistema

**Em um intervalo tempo**

$$Q - W = \Delta E$$

**Em um certo instante**

$$\frac{dE}{dt} = \frac{dU}{dt} + \frac{dEC}{dt} + \frac{dEP}{dt} = \frac{\delta Q}{dt} - \frac{\delta W}{dt}$$

$$\frac{dU}{dt} + \frac{dEC}{dt} + \frac{dEP}{dt} = \dot{Q} - \dot{W}$$

**Para variações de energia cinética e potencial desprezíveis**

$$Q - W = \Delta U$$

**Em um certo instante**

$$\dot{Q} - \dot{W} = \frac{dU}{dt}$$

![Conservação de energia — sistema fechado](Slide%201/3.png)

## A equivalência entre transferência de trabalho e de calor em um sistema durante um processo cíclico

Diagrama $P$-$v$: estados 1 e 2; caminhos A, B, C.

$$De\ 1 \xrightarrow{A} 2 \xrightarrow{B} 1 \Rightarrow \int_1^2 \delta Q_A + \int_2^1 \delta Q_B = \int_1^2 \delta W_A + \int_2^1 \delta W_B$$

$$De\ 1 \xrightarrow{C} 2 \xrightarrow{B} 1 \Rightarrow \int_1^2 \delta Q_C + \int_2^1 \delta Q_B = \int_1^2 \delta W_C + \int_2^1 \delta W_B$$

$$Subtraindo:\ \int_1^2 \delta Q_A - \int_1^2 \delta Q_C = \int_1^2 \delta W_A - \int_1^2 \delta W_C$$

$$ou:\ \int_1^2 \delta Q_A - \int_1^2 \delta W_A = \int_1^2 \delta Q_C - \int_1^2 \delta W_C \Rightarrow \int_1^2 (\delta Q - \delta W)_A = \int_1^2 (\delta Q - \delta W)_C$$

Uma vez que A e C são processos arbitrários entre os estados 1 e 2, a quantidade $\delta Q - \delta W$ depende apenas dos estados iniciais e finais. Essa expressão é uma diferencial exata, e portanto, pode ser uma diferencial de uma propriedade do sistema.

![Processo cíclico — equivalência calor e trabalho](Slide%201/4.png)

## Energia do sistema ($E$)

Esta propriedade é chamada de energia do sistema (**E**).

A energia do sistema é uma propriedade termodinâmica porque o valor de ‘E’ é independente do caminho, e pode ser idenficada por a partir de outras propriedades termodinâmicas independentes.

Diagrama $P$-$V$: caminhos A, B, C entre estados 1 e 2.

$$dE = \delta Q - \delta W$$

ou integrada entre 1 e 2:

$$E_2 - E_1 = {}_1Q_2 - {}_1W_2$$

![Energia do sistema](Slide%201/5.png)

## Propriedade E

Propriedade **E** é toda a energia de um sistema, em um certo estado.

Há vários tipos de energia tais como a energia associada ao movimento e posição das partículas, aquela armazenada nas ligações químicas, etc.

$$E = \text{Energia Interna} + \text{Energia cinética} + \text{Energia potêncial}$$

- e.g. relacionada à temperatura / velocidade / elevação

$$E = U + EC + EP$$

Uma vez que todos os termos de E são diferenciais exatas, podemos escrever:

$$dE = dU + d(EC) + d(EP) = \delta Q - \delta W \quad \text{($1^a$ Lei da Termodinâmica)}$$

![Propriedade E](Slide%201/6.png)

## Forma diferenciada e integrada

$$dE = dU + d(EC) + d(EP) = \delta Q - \delta W$$

**Na forma diferenciada:**

$$dE = dU + d\left(\frac{mV^2}{2}\right) + d(mgZ) = \delta Q - \delta W$$

**ou na forma integrada:**

$$E_2 - E_1 = U_2 - U_1 + \frac{m(V_2^2 - V_1^2)}{2} + mg(Z_2 - Z_1) = {}_1Q_2 - {}_1W_2$$

Esta é simplesmente uma constatação da conservação de energia. **MUDANÇAS** na EC, EP & U podem ser causadas **por Q & W**

![Conservação de energia — formas](Slide%201/7.png)

## Como calcular $U$ ou $E$ em um sistema com inúmeros subsistemas?

$$E = E_1 + E_2 + E_3 + \dots$$

$$U = U_1 + U_2 + U_3 + \dots$$

$$mu = m_1 u_1 + m_2 u_2 + m_3 u_3 + \dots$$

Similar com a EC e EP

## Balanço de massa para análise de um volume de controle

- Energia pode atravessar as fronteiras de um volume de controle na forma de trabalho, calor, ou junto com vazões mássicas.
- A massa é uma propriedade que se conserva, assim como a energia.
- A equação (1) abaixo indica que a taxa com que a massa varia dentro do volume de controle depende da taxa (vazão) com que a massa entra e sai desse volume de controle.
- A vazão mássica pode ser escrita como o produto da massa específica pela vazão volumétrica (eq. 2)
- A vazão volumétrica pode ser escrita como o produto da velocidade média pela área transversal ao escoamento

$$\frac{dm_{VC}}{dt} = \dot{m}_E - \dot{m}_S \quad \text{(1)}$$

$$= \rho_E \dot{V}_E - \rho_S \dot{V}_S \quad \text{(2)}$$

$$= \rho_E A_E V_E - \rho_S A_S V_S \quad \text{(3)}$$

**Figura 6.2** — Diagrama esquemático de um volume de controle para a análise da equação da continuidade.

![Balanço de massa — Figura 6.2](Slide%201/9.png)

## Balanço de massa

Se houver mais de uma corrente de entrada e de saída

**Conservação de massa**

$$\frac{dm_{VC}}{dt} = \sum \dot{m}_E - \sum \dot{m}_S$$

![Balanço de massa — múltiplas correntes](Slide%201/10.png)

## 1ª Lei da termodinâmica para um sistema

**1ª Lei entre dois estados:**

$$E_2 - E_1 = {}_1Q_2 - {}_1W_2$$

**1ª Lei para a taxa de variação de energia:**

$$\frac{dE_{\text{sis}}}{dt} = (\dot{Q} - \dot{W})_{\text{sis}}$$

**1ª Lei para um volume de controle:**

$$\frac{dE_{VC}}{dt} = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} + \dot{W}_{\text{fluido}} + \dot{E}_e - \dot{E}_s$$

$$\dot{Q} = \sum \dot{Q}_e - \sum \dot{Q}_s$$

$$\dot{W}_{\text{eixo}} = \sum \dot{W}_{\text{eixo},e} - \sum \dot{W}_{\text{eixo},s}$$

$$\dot{W}_{\text{fluido}} = \sum \dot{W}_e - \sum \dot{W}_s = \sum \dot{m}_e v_e p_e - \sum \dot{m}_s v_s p_s$$

$$E = e \cdot m$$

$$e = \bar{u} + gz + \frac{V^2}{2} \Rightarrow \text{energia total do sistema}$$

$$\dot{E} = e \cdot \dot{m}$$

VC — $E_{VC}$ — $\dot{E}_e$, $\dot{W}_e$, $\dot{E}_s$, $\dot{W}_s$, $\dot{Q}_{VC}$, $\dot{W}_{\text{Eixo}}$

![1ª lei — sistema e volume de controle](Slide%201/11.png)

## 1ª Lei da termodinâmica para um volume de controle

$$\frac{dE_{VC}}{dt} = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} + \sum_{E} \dot{m}_{E} p_{E} v_{E} - \sum_{S} \dot{m}_{S} p_{S} v_{S} - \sum_{S} \dot{m}_{S} \left(u_{S} + gz_{S} + \frac{V_{S}^2}{2}\right) + \sum_{E} \dot{m}_{E} \left(u_{E} + gz_{E} + \frac{V_{E}^2}{2}\right)$$

$$\frac{dE_{VC}}{dt} = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \sum_{S} \dot{m}_{S} \left(u_{S} + p_{S} v_{S} + gz_{S} + \frac{V_{S}^2}{2}\right) + \sum_{E} \dot{m}_{E} \left(u_{E} + p_{E} v_{E} + gz_{E} + \frac{V_{E}^2}{2}\right)$$

$$\frac{dE_{VC}}{dt} = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \sum_{S} \dot{m}_{S} \left(h_{S} + gz_{S} + \frac{V_{S}^2}{2}\right) + \sum_{E} \dot{m}_{E} \left(h_{E} + gz_{E} + \frac{V_{E}^2}{2}\right)$$

$$\frac{dE_{VC}}{dt} = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \sum_{S} \dot{m}_{S} h_{S,\text{tot}} + \sum_{E} \dot{m}_{E} h_{E,\text{tot}}$$

$$h_{\text{tot}} = h + gz + \frac{V^2}{2}$$

![1ª lei — volume de controle (entalpia)](Slide%201/12.png)

## A propriedade Entalpia ($H$)

É uma combinação das propriedades $U$, $p$ e $V$ ou $u$, $p$ e $v$ e combina os efeitos da energia interna e do trabalho de expansão a pressão constante com a quantidade de calor transferido no processo isobárico.

Para obtê-la, considere uma expansão isobárica, onde a EC e EP são desprezíveis

$$U_2 - U_1 = {}_1Q_2 - {}_1W_2$$

$$\Rightarrow {}_1Q_2 = U_2 - U_1 + {}_1W_2$$

$${}_1W_2 = \int_1^2 P\, dV = P(V_2 - V_1)$$

$${}_1Q_2 = (U_2 + PV_2) - (U_1 + PV_1) \equiv H_2 - H_1$$

$$H = U + PV$$

**Figura 5.7** Processo quase-estático a pressão constante.

A quantidade de calor trocado num processo isobárico sem variação de EC e EP é igual a variação da entalpia

![Entalpia — Figura 5.7](Slide%201/13.png)

## As propriedades calor específico a pressão constante e a volume constante ($C_P$ e $C_V$)

Calor específico $\equiv$ Quantidade de calor necessária para aumentar a temperatura de uma unidade de massa em uma unidade de temperatura (no SI, J/kg.K)

Ou...

$$\delta Q = dU + \delta W = dU + P\, dV$$

$$C_V \equiv \frac{1}{m} \left(\frac{\delta Q}{\partial T}\right)_V = \frac{1}{m} \left(\frac{\partial U}{\partial T}\right)_V = \left(\frac{\partial u}{\partial T}\right)_V \quad (\text{kJ/kg K})$$

$$C_P \equiv \frac{1}{m} \left(\frac{\delta Q}{\partial T}\right)_P = \frac{1}{m} \left(\frac{\partial H}{\partial T}\right)_P = \left(\frac{\partial h}{\partial T}\right)_P \quad (\text{kJ/kg K})$$

**Importante:** $C_p$ e $C_v$ são propriedades termodinâmicas

## Calor específico ($C_P$) e ($C_V$) para sólidos e líquidos

Essas fases são praticamente incompressíveis

$$h = u + pv$$

$$dh = du + p\, dv + v\, dp$$

$$dh \approx du \approx C\, dT$$

$C$ é aproximadamente constante durante um processo (a não ser que o intervalo de temperatura seja muito grande, ou o processo ocorra em temperaturas muito baixas, logo...

$$h_2 - h_1 \cong u_2 - u_1 \cong C(T_2 - T_1)$$

## Energia Interna, Entalpia e Calor específico para gases ideais

A eq. dos gases ideais é $pv = RT$

E como um gás ideal expandindo num sistema isolado no vácuo permanece com temperatura constante, enquanto $p$ e $V$ mudam

$$u = u(T)$$

E pode-se verificar essa afirmação em tabelas termodinâmicas, na região dos gases ideais

Além disso, pode se escrever a entalpia como $h = u + RT$

E $h = h(T)$

## Relação entre $u$ e $T$ para os gases ideais

$$C_v = \left(\frac{\partial u}{\partial T}\right)_v \xrightarrow{\text{Gás Ideal}} C_{v0} = \frac{\partial u}{\partial T}$$

$$du = C_{v0}\, dT \Rightarrow dU = m C_{v0}\, dT$$

## Relação entre $h$ e $T$ para os gases ideais

$$C_p = \left(\frac{\partial h}{\partial T}\right)_p \xrightarrow{\text{Gás Ideal}} C_{p0} = \frac{\partial h}{\partial T}$$

$$dh = C_{p0}\, dT \Rightarrow dH = m C_{p0}\, dT$$

## Outras relações importantes

$$h = u + Pv$$

$$Pv = RT \Rightarrow h = u + RT$$

$$\frac{dh}{dT} = \frac{du}{dT} + R \Rightarrow C_{p0} - C_{v0} = R$$

## Quando é possível utilizar o $C_v$ e o $C_p$ ao invés de $u$ e $h$?

- Quando houver apenas uma fase!
- NÃO utilizar em processos com mudança de fase, ou bifásicos

Para gases, use calor específico constante para um curto intervalo de temperatura (cálculo baseado na temperatura média)

Para sólidos e líquidos, o calor específico é aproximadamente constante, mesmo numa faixa relativamente grande de temperatura.

## Cálculo de $\Delta h$ e $\Delta u$

$$h_2 - h_1 \cong u_2 - u_1 \cong C(T_2 - T_1)$$

Sólidos e líquidos comprimidos e $C$ obtido na tabela A3 ou A4 (disponível no Moodle)

$$u_2 - u_1 = C_{v0}(T_2 - T_1)$$

$$h_2 - h_1 = C_{p0}(T_2 - T_1)$$

Gases ideais $C_{v0}$ e $C_{p0}$ obtidos na tabela A5 (disponível no Moodle)

$$\Delta h = h_2 - h_1 \quad ; \quad \Delta u = u_2 - u_1$$

Gases não ideais, líquidos saturados ou comprimidos, mistura de líquido e vapor saturado, Propriedades nas tabelas do apêndice B ou em http://laine.com.br

Sendo que 1 e 2 podem ser dois estados distintos ou duas posições distintas como a entrada e a saída de um volume de controle

## Simplificações

### 1. Estado estacionário

$$\frac{dE_{VC}}{dt} = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \sum_{S} \dot{m}_S \left(h_S + gz_S + \frac{V_S^2}{2}\right) + \sum_{E} \dot{m}_E \left(h_E + gz_E + \frac{V_E^2}{2}\right)$$

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \sum_{S} \dot{m}_S \left(h_S + gz_S + \frac{V_S^2}{2}\right) + \sum_{E} \dot{m}_E \left(h_E + gz_E + \frac{V_E^2}{2}\right)$$

$$\sum_{S} \dot{m}_S = \sum_{E} \dot{m}_E$$

### 2. Se há apenas uma vazão de entrada e de saída

$$\dot{m}_S = \dot{m}_E = \dot{m}$$

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \dot{m} \left(h_S + gz_S + \frac{V_S^2}{2}\right) + \dot{m} \left(h_E + gz_E + \frac{V_E^2}{2}\right)$$

$$w_{\text{eixo,VC}} + h_S + gz_S + \frac{V_S^2}{2} = q_{VC} + h_E + gz_E + \frac{V_E^2}{2}$$

## EXEMPLO 1.3

Uma barra longa, de material condutor, com diâmetro $D$ e resistência elétrica por unidade de comprimento $R'_e$, encontra-se inicialmente em equilíbrio térmico com o ar ambiente e sua vizinhança. Esse equilíbrio é perturbado quando uma corrente elétrica $I$ passa através da barra. Desenvolva uma equação que possa ser utilizada para calcular a variação da temperatura da barra durante a passagem da corrente.

**Esquema:** $I$, $D$, $L$, $T$, Ar ($T_\infty$, $h$), $T_{\text{viz}}$, $\dot{E}_{\text{ar}}$, $\dot{E}_s$

![Exemplo 1.3 — enunciado e esquema](Slide%201/22.png)

$$\dot{E}_e - \dot{E}_s = \frac{dE_{\text{ar}}}{dt} \quad ; \quad \dot{Q} - \dot{W} = \frac{dU}{dt}$$

$$\dot{E}_e = -\dot{W} = I^2 R'_e L$$

$$\dot{E}_s = \dot{Q} = h(\pi DL)(T - T_\infty) + \epsilon \sigma (\pi DL)(T^4 - T_{\text{viz}}^4)$$

$$\dot{E}_{\text{ar}} = \frac{dU}{dt} = \frac{d}{dt}(\rho V c T)$$

$$I^2 R'_e L - h(\pi DL)(T - T_\infty) - \epsilon \sigma (\pi DL)(T^4 - T_{\text{viz}}^4) = \rho c \left(\frac{\pi D^2}{4}\right) L \frac{dT}{dt}$$

$$\frac{dT}{dt} = \frac{I^2 R'_e - \pi D h (T - T_\infty) - \pi D \epsilon \sigma (T^4 - T_{\text{viz}}^4)}{\rho c (\pi D^2 / 4)}$$

![Exemplo 1.3 — derivação](Slide%201/23.png)

## No estado estacionário

$$\pi D h (T - T_\infty) + \pi D \epsilon \sigma (T^4 - T_{\text{viz}}^4) = I^2 R'_e$$

Gráfico $T$ ($^{\circ}\text{C}$) vs $I$ (ampères): em $I = 5{,}2$ A, $T = 60\,^{\circ}\text{C}$.

![Estado estacionário — exemplo 1.3](Slide%201/24.png)

## EXEMPLO 1.4

Uma massa de gelo $M$ na temperatura de fusão ($T_f = 0\,^{\circ}\text{C}$) encontra-se no interior de uma cavidade cúbica de aresta $W$. A parede da cavidade possui espessura $L$ e condutividade térmica $k$. Se a temperatura $T_1$, da superfície externa da parede, é maior do que $T_f$ ($T_1 > T_f$), obtenha uma expressão para o tempo necessário para que a fusão do gelo seja completa.

**Esquema:** cavidade $W$, Mistura de água-gelo ($T_f$), Seção A-A, $L$, $k$, $T_1$, $E_e$, $\Delta E_{\text{ar}}$

![Exemplo 1.4 — enunciado e esquema](Slide%201/25.png)

$$E_e = \Delta E_{\text{ar}} = \Delta U_{\text{lat}}$$

$$q_{\text{cond}} = k(6W^2) \frac{T_1 - T_f}{L}$$

$$E_e = \left[k(6W^2) \frac{T_1 - T_f}{L}\right] t_f$$

$$t_f = \frac{M h_s L}{6W^2 k (T_1 - T_f)}$$

Considere uma cavidade de aresta $W = 200\ \text{mm}$, espessura da parede $L = 10\ \text{mm}$ e condutividade térmica $k = 0{,}05\ \text{W/m}\cdot\text{K}$.

$$M = \rho_s (W - 2L)^3 = 917\ \text{kg/m}^3 \times (0{,}2\ \text{m} - 0{,}02\ \text{m})^3 = 5{,}35\ \text{kg}$$

Se a temperatura da superfície externa for $T_1 = 20\,^{\circ}\text{C}$, o tempo necessário para a fusão do gelo é

$$t_f = \frac{5{,}35\ \text{kg} \times 333420\ \text{J/kg} \times 0{,}01\ \text{m}}{6 \times (0{,}2\ \text{m})^2 \times 0{,}05\ \text{W/m}\cdot\text{K} \times (20 - 0)\,^{\circ}\text{C}} = 74325\ \text{s} = 20\ \text{h e } 39\ \text{min.}$$

![Exemplo 1.4 — solução](Slide%201/26.png)

## Conservação de energia na superfície

Um caso particular onde não há massa ou volume dentro da superfície de controle

**Conservação de Energia (em um instante):**

$$\dot{E}_e - \dot{E}_s = 0$$

Como não há massa ou volume, não pode haver acúmulo ou decréscimo de energia, mesmo que isso ocorra ao redor da superfície de controle

Considere a superfície da parede com transferência de calor por condução, convecção e radiação

**Fig. 1.9** Balanço de energia para conservação de energia na superfície de um meio.

![Conservação de energia na superfície](Slide%201/27.png)

## 1.6 — Janela de vidro

Uma janela de vidro de $1\ \text{m}$ de largura e $2\ \text{m}$ de altura apresenta $5\ \text{mm}$ de espessura e condutividade térmica $k_v = 1{,}4\ \text{W/m}\cdot\text{K}$. Se as temperaturas interna e externa do vidro são $15\,^{\circ}\text{C}$ e $-20\,^{\circ}\text{C}$, respectivamente, em um dia de inverno, qual a taxa de perda de calor através do vidro? Para reduzir as perdas de calor através das janelas, costumam-se utilizar construções com painel duplo em que as duas placas de vidro são separadas por ar. Se o espaçamento entre elas for de $10\ \text{mm}$ e as superfícies em contato com o ar tiverem temperaturas de $10\,^{\circ}\text{C}$ e $-15\,^{\circ}\text{C}$, qual a taxa de perda de calor de uma janela $1\ \text{m} \times 2\ \text{m}$? A condutividade térmica do ar é $k_a = 0{,}024\ \text{W/m}\cdot\text{K}$.

![Exercício 1.6](Slide%201/28.png)

## 1.17 — Anemômetro de fio incandescente

Um procedimento comum para medir a velocidade de uma corrente de ar envolve a inserção de um aquecedor elétrico em forma de fio (denominado *anemômetro de fio incandescente*) em uma corrente de ar, com o eixo do fio orientado perpendicularmente em direção do escoamento. A energia elétrica dissipada no fio é considerada como sendo transferida para o ar por convecção forçada. Assim sendo, para uma potência elétrica prescrita, a temperatura do fio depende do coeficiente de convecção, que, por sua vez, depende da velocidade do ar. Considere o fio com comprimento $L = 20\ \text{mm}$ e diâmetro $D = 0{,}5\ \text{mm}$, cuja calibração da forma, $V = 6{,}25 \times 10^{-5} h^2$, foi determinada. A velocidade $V$ e o coeficiente de convecção $h$ têm unidades de m/s e W/m²·K, respectivamente. Em uma aplicação com o ar a uma temperatura $T_{\text{ar}} = 25\,^{\circ}\text{C}$, a temperatura da superfície do anemômetro é mantida a $T_s = 75\,^{\circ}\text{C}$ com uma queda de tensão de $5\ \text{V}$ e uma corrente elétrica de $0{,}1\ \text{A}$. Qual a velocidade do ar?

![Exercício 1.17](Slide%201/29.png)
