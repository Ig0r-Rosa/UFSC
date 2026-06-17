# Equações Básicas na Forma Integral para um Volume de Controle

## Slide 1

* Teorema do transporte de Reynolds: Análise de volumes de controles para situações originalmente baseadas em sistemas.
* Analise do comportamento do conteúdo de uma região finita do espaço (**volume de controle**)
    * Ex. A forças necessárias para fixar uma turbina eólica
* Para isso, consideraremos:
    * Equação da continuidade (Conservação de massa)
    * 2ª Lei de Newton (Equação do momento linear)
    * 1ª Lei da termodinâmica (Conservação de energia)

![](4/1.png)

## Slide 2

### Volume de controle (VC) e sistema (Sis)

**VC:** Volume no espaço pelo qual a matéria pode fluir.

**Sis:** Conjunto de materia de identidade fixa.

**Atenção:** Todas as leis que governam o movimento dos fluidos, em suas formas básicas, consideram a análise de um sistema.

![](4/2.png)

## Slide 3

### Tipos de volume de controle

a) VC fixo

b) VC fixo ou em movimento

c) VC deformável

**Legenda:**
* Linha tracejada azul: Control volume surface
* Cinza claro: System at time $t_1$
* Cinza escuro: System at time $t_2 > t_1$

(a) Pipe — VC fixo; (b) Jet engine — VC fixo ou em movimento; (c) Balloon — VC deformável.

![](4/3.png)

## Slide 4

### Teorema do transporte de Reynolds

Sistema $\ll$----->> volume de controle

**B:** qualquer propriedade do fluido

**b:** quantidade da propriedade por unidade de massa

$$B = mb$$

$$B_{sis} = \lim_{\delta \forall \to 0} \sum_{i} b_i (\rho_i \delta \forall_i) = \int_{sis} \rho b \, d\forall$$

![](4/4.png)

## Slide 5

### Derivação do TTR

Em um tempo $t$, Sis = VC,

And at time $t + \delta t$, Sis = VC - I + II

**Legenda do diagrama:**
* Fixed control surface and system boundary at time $t$
* System boundary at time $t + \delta t$
* Inflow (Região I)
* Outflow (Região II)
* CV - I

![](4/5.png)

## Slide 6

**Legenda do diagrama:**
* Fixed control surface and system boundary at time $t$
* System boundary at time $t + \delta t$
* Inflow
* Outflow
* CV - I

$$(1) \quad B_{Sis}(t) = B_{VC}(t)$$

$$(2) \quad B_{Sis}(t + \delta t) = B_{VC}(t + \delta t) - B_I(t + \delta t) + B_{II}(t + \delta t)$$

$$(3) \quad \frac{\delta B_{Sis}}{\delta t} = \frac{B_{Sis}(t + \delta t) - B_{Sis}(t)}{\delta t} = \frac{B_{VC}(t + \delta t) - B_{VC}(t)}{\delta t} - \frac{B_I(t + \delta t)}{\delta t} + \frac{B_{II}(t + \delta t)}{\delta t}$$

![](4/6.png)

## Slide 7

No limite, $\delta t \rightarrow 0$

$$(4) \quad \lim_{\delta t \rightarrow 0} \frac{B_{VC}(t + \delta t) - B_{VC}(t)}{\delta t} = \frac{\partial B_{VC}}{\partial t} = \frac{\partial \left( \int_{VC} \rho b \, d\forall \right)}{\partial t}$$

$$(5) \quad \dot{B}_S = \lim_{\delta t \rightarrow 0} \frac{B_{II}(t + \delta t)}{\delta t}$$

$$(6) \quad \dot{B}_E = \lim_{\delta t \rightarrow 0} \frac{B_I(t + \delta t)}{\delta t}$$

finalmente,

$$\frac{DB_{Sis}}{Dt} = \frac{\partial B_{VC}}{\partial t} + \dot{B}_S - \dot{B}_E$$

![](4/7.png)

## Slide 8

(a) Outflow portion of control surface $CS_{out}$ — $\delta A$, $\hat{n}$, $\vec{V}$, $\theta$

(b) $\delta \ell = V \delta t$; $\delta \ell_n = \delta \ell \cos \theta$; $\delta \forall = \delta \ell_n \delta A$

(c) $\delta \ell_n = \delta \ell \cos \theta$

E a taxa de descarga $\dot{B}$ é

$$\delta B = b \rho \delta \forall = b \rho (V \cos \theta \delta t) \delta A,$$

$$\delta \dot{B}_s = \lim_{\delta t \to 0} \frac{\rho b \delta \forall}{\delta t} = \lim_{\delta t \to 0} \frac{b \rho (V \cos \theta \delta t) \delta A}{\delta t} = \rho b V \cos \theta \delta A,$$

$$\dot{B}_s = \int_{SC_s} d \dot{B}_s = \int_{SC_s} \rho b V \cos \theta \, dA = \int_{SC_s} \rho b \vec{V} \cdot \vec{n} \, dA$$

![](4/8.png)

## Slide 9

(a) Inflow portion of control surface $CS_{in}$ — $\delta A$, $\hat{n}$, $\vec{v}$, $\theta$

(b) $\delta \forall = \delta \ell_n \delta A$; $\delta \ell = V \delta t$

(c) $\delta \ell_n$, $\delta \ell$, $\theta$

De maneira similar, a taxa de alimentação:

$$\dot{B}_E = \int_{SC_E} d\dot{B}_E = \int_{SC_E} \rho b V \cos \theta \, dA = - \int_{SC_E} \rho b \vec{V} \cdot \vec{n} \, dA$$

e,

$$\dot{B}_S - \dot{B}_E = \int_{SC_S} \rho b \vec{V} \cdot \vec{n} \, dA - \left( - \int_{SC_E} \rho b \vec{V} \cdot \vec{n} \, dA \right) = \int_{SC} \rho b \vec{V} \cdot \vec{n} \, dA$$

![](4/9.png)

## Slide 10

E finalmente:

$$\frac{DB_{sys}}{Dt} = \frac{\partial B_{cv}}{\partial t} + \int_{cs} \rho b \vec{V} \cdot \vec{n} \, dA$$

A forma geral para o TTR para volumes de controle fixo e não deformáveis

$$\frac{DB_{Sis}}{Dt} = \frac{\partial}{\partial t} \int_{VC} \rho b \, d\forall + \int_{SC} \rho b \vec{V} \cdot \vec{n} \, dA$$

![](4/10.png)

## Slide 11

### Interpretação física

A taxa de variação temporal de qualquer propriedade extensiva $B$ em um sistema $\equiv$ A taxa de variação temporal desta propriedade extensiva $B$ dentro do volume de controle + o fluxo mássico líquido através da superfície do volume de controle

$$\frac{DB_{sis}}{Dt} = \frac{\partial}{\partial t} \int_{VC} \rho b \, d\forall + \int_{SC} \rho b \vec{V} \cdot \vec{n} \, dA$$

![](4/11.png)

## Slide 12

### Seleção do volume de controle

Qualquer volume no espaço pode ser considerado um volume de controle

Nenhum está errado, mas alguns são mais convenientes para se analisar, que outros

**FIGURE 4.12** Various control volumes for flow through a pipe.

(a) Control surface passando por (1); (b) ponto (1) fora do volume de controle; (c) superfícies não perpendiculares ao escoamento.

Para se saber o valor de uma propriedade em $(1)$, (a) é mais conveniente que (b) e que (c).

![](4/12.png)

## Slide 14

Fig. P4.56 — Seção (1): $V_1 = 2$ m/s, $0{,}5$ m; Seção (2): $V_2 = 1$ m/s, $0{,}6$ m; Seção (3): $V_3 = 2{,}5$ m/s, $0{,}8$ m; --- Volume de controle.

$\Delta t = 0{,}2$ s:

* Seção (1): flow into control vol. — $0{,}4$ m ($V_1 \Delta t$)
* Seção (2): flow into control vol. — $0{,}2$ m ($V_2 \Delta t$)
* Seção (3): flow out of control vol. — $0{,}5$ m ($V_3 \Delta t$)

Legenda: --- control volume; ... system at $t = 20{,}2$ s

![](4/14.png)

## Slide 15

### Equação da continuidade

#### Derivação da Eq. da Continuidade

Um sistema é definido como um conjunto de conteúdo fixo

Desta forma,

$$\frac{DM_{sis}}{Dt} = 0$$

e

$$M_{sis} = \int_{sis} \rho \, d\forall$$

![](4/15.png)

## Slide 16

Do TTR, obtém-se a seguinte equação para um VC fixo e indeformável:

$$\frac{D}{Dt} \int_{sis} \rho \, d\forall = \frac{\partial}{\partial t} \int_{VC} \rho \, d\forall + \int_{SC} \rho \vec{V} \cdot \vec{n} \, dA$$

Então....

$$\frac{\partial}{\partial t} \int_{cv} \rho \, d\forall + \int_{cs} \rho \vec{V} \cdot \vec{n} \, dA = 0 \Rightarrow \text{Eq. da Continuida de}$$

![](4/16.png)

## Slide 17

A vazão mássica pode ser escrita como

$$\dot{m} = \rho \dot{Q} = \rho A \overline{V}$$

E a velocidade média é definida como:

$$\overline{V} = \frac{\int_{A} \rho \vec{V} \cdot \vec{n} \, dA}{\rho A} \Rightarrow \frac{\int_{A} \vec{V} \cdot \vec{n} \, dA}{A} \text{ (cte } \rho)$$

![](4/17.png)

## Slide 19

$$\frac{DB_{Sis}}{Dt} = \frac{\partial B_{VC}}{\partial t} + \dot{B}_S - \dot{B}_E$$

$$\frac{DM_{Sis}}{Dt} = \frac{\partial M_{VC}}{\partial t} + \dot{M}_S - \dot{M}_E = 0$$

$$\frac{\partial M_{VC}}{\partial t} = \dot{M}_E - \dot{M}_S = \rho_E \dot{Q}_E - \rho_S A_S V_S$$

$$\frac{\partial \rho \forall_{VC}}{\partial t} = \rho_E \dot{Q}_E - \rho_S A_S V_S$$

$$\frac{\partial \rho}{\partial t} = \frac{\rho_E \dot{Q}_E - \rho_S A_S V_S}{\forall_{VC}}$$

A ISA (Atmosfera Padrão Internacional), considera que ao nível do mar (101,3 kPa) e a 15 °C o ar tem uma massa específica de cerca de 1,225 kg/m$^3$

![](4/19.png)

## Slide 21

### Equações de quantidade de movimento

#### 1) Derivação da Equação de Quantidade de Movimento Linear

A quantidade de movimento de uma pequena partícula é:

$$\delta q = \vec{V} \rho \, d\forall$$

E Segunda Lei de Newton pode ser escrita como:

$$\frac{D}{Dt} \int_{sis} \vec{V} \rho \, d\forall = \sum F_{sis}$$

![](4/21.png)

## Slide 22

Se o Sis e o VC coincidem em um determinado instante, então $\sum F_{sis} = \sum F_{VCC}$

#### Forças externas agindo no Sis e no VCC

Diagrama: System; Coincident control volume; forças $\mathbf{F}_A$, $\mathbf{F}_B$, $\mathbf{F}_C$, $\mathbf{F}_D$, $\mathbf{F}_E$, $\mathbf{F}_F$, $\mathbf{F}_G$.

![](4/22.png)

## Slide 23

Se o VCC for fixo e indeformável, pode-se usar o TTR:

$$\frac{D}{Dt} \int_{sis} \vec{V} \rho \, d\forall = \frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA$$

E finalmente, a Eq. da Quantidade de Movimento Linear fica

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

![](4/23.png)

## Slide 24

### Aplicação:

Encontre a força necessária para mobilizar o bocal cônico

**Dados:**
* $\dot{Q} = 0{,}6$ L/s
* $M = 0{,}1$ kg
* $D_1 = 16$ mm
* $D_2 = 5$ mm
* $H = 30$ mm
* $p_1 = 464$ kPa

Bocal cônico vertical: Seção (1) — $D_1$, $w_1$; Seção (2) — $D_2$, $w_2$; $h = 30$ mm; Control volume; eixo $z$ para cima; $g$ para baixo.

![](4/24.png)

## Slide 25

VC: O bocal e a água dentro do bocal

A pressão atmosférica se anula em todas as direções

Na direção z, a equação da quantidade de movimento para um fluxo estacionário é

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

$$\int_{SC} w \rho \vec{V} \cdot \vec{n} \, dA = F_A - W_n - p_1 A_1 - W_w + p_2 A_2$$

**Legenda:**
* $F_A$ = anchoring force that holds nozzle in place
* $W_n$ = weight of nozzle
* $W_w$ = weight of water contained in the nozzle
* $p_1$ = gage pressure at section (1)
* $A_1$ = cross section area at section (1)
* $p_2$ = gage pressure at section (2)
* $A_2$ = cross section area at section (2)
* $w_1$ = z direction velocity at control volume entrance
* $w_2$ = z direction velocity at control volume exit

![](4/25.png)

## Slide 26

Note: A velocidade w é + na direção positiva da coordenada e – caso contrário: Neste exemplo –w

O vetor normal é + quando deixa a superfície de controle, portanto

$$\vec{V} \cdot \vec{n} \, dA = \pm |w| \cos \theta \, dA$$

E...

$$(-w_1)(-\dot{m}_1) + (-w_2)\dot{m}_2 = F_A - W_n - p_1 A_1 - W_w + p_2 A_2$$

Da equação da continuidade temos que $\dot{m}_1 = \dot{m}_2 = \dot{m}$

E a força para manter o bocal estacionário é

$$F_A = \dot{m}(w_1 - w_2) + W_n + p_1 A_1 + W_w - p_2 A_2$$

E neste caso,

$$p_2 = 0$$

![](4/26.png)

## Slide 27

### Comentários

1. Quando a velocidade do escoamento é uniformemente distribuído sobre a seção de escoamento, a integração é uma operação simples.
2. A quantidade de movimento linear é vetorial e pode ter componentes nas três direções ortogonais
3. **A quantidade de movimento e velocidade tem sinais algébricos**
    * **Para a vazão mássica**, vazão de entrada é negativa e vazão de saída é positiva
    * **Para a velocidade**, ela é positiva na direção positiva da coordenada, e negativa na direção negativa da coordenada

![](4/27.png)

## Slide 28

4. Para escoamento estacionário, a taxa de variação da quantidade de movimento no conteúdo do volume de controle indeformável é nula, portanto...

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall = 0$$

5. Quando a vazão na saída for subsônica, a pressão na saída é atmosférica ( jatos livres )

6. Forças devido a pressão atmosférica agindo na superfície de controle devem ser cuidadosamente analisadas

7. Forças externas tem sinal algébrico, que é **+** se a força agir na direção positiva da coordenada, e **-**, caso contrário

![](4/28.png)

## Slide 29

8. Além das forças de campo (forças devido a gravidade), apenas forças externas agindo no conteúdo do VC são consideradas na Eq. da QML. Se apenas o fluido for considerado no VC, as forças de reação entre o fluido e a parede também devem ser consideradas

9. A força necessária para mobilizar um objeto pode ser uma reação a...
    * Mudanças na quantidade de movimento linear (direção ou magnitude)
    * Forças de pressão no fluido
    * Forças de fricção no fluido
    * Peso do fluido

![](4/29.png)

## Slide 30

10. O VC também pode ser: um contendo só o bocal e outro contendo só a água do bocal

Cuidado ao analisar as forças devido a pressão

(c) Bocal — $F_A$, $W_n$, $R_z$, $P_{atm}$

(d) Água — $(p_1 + p_{atm})A_1$, $w_1$, $W_w$, $R_z$, $(p_2 + p_{atm})A_2$, $w_2$, seção (2)

$$R_z \equiv \text{Interação entre o bocal e a água}$$

![](4/30.png)

## Slide 31

Jato horizontal: $A_1 = 0{,}06$ m$^2$, $V_1 = 4$ m/s; deflexão $\theta = 30°$; $F_x = ?$

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum \vec{F}_{VCC}$$

$$0 + \int_{SC} u \rho \vec{V} \cdot \vec{n} \, dA = F_x$$

$$u \rho (-u) A + u \rho (u \cos 30°) A = -F_x$$

$$F_x = 0{,}06 \times 4^2 \times 1000 \times (1 - \cos 30°) = 128{,}6 \text{ N}$$

![](4/31.png)

## Slide 33

$$\sum M_O = 0 \quad \implies \quad R_x l_{R_x} = W l_W$$

$$R_x = \frac{W l_W}{l_{R_x}} = \frac{6\text{N} \left( \frac{0{,}015}{2} \text{ m} \right)}{0{,}050\text{m}} = 0{,}90 \text{ N}$$

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

$$0 + \int_{SC} u \rho \vec{V} \cdot \vec{n} \, dA = F_x$$

$$u \rho (-u) A = -R_x$$

$$u = \sqrt{\frac{R_x}{A \rho}}$$

$$V_1 = \sqrt{\frac{0{,}9 \text{ N}}{\left(999 \frac{\text{kg}}{\text{m}^3}\right) \frac{\pi}{4} (0{,}01\text{m})^2}} = 3{,}39 \frac{\text{m}}{\text{s}}$$

$$Q = A_1 V_1 = \frac{\pi}{4} (0{,}01\text{m})^2 \left(3{,}39 \frac{\text{m}}{\text{s}}\right) = \underline{\underline{2{,}66 \times 10^{-4} \frac{\text{m}^3}{\text{s}}}}$$

Superfície de controle: seção (1) $V_1$; seções (2) $V_2$ e (3) $V_3 \approx 0$; $p_1 = p_3 = 0$. Bloco: $R_x$, $W$, $O_x$, $O_y$ em $O$; $l_{R_x}$, $l_W$.

![](4/33.png)

## Slide 34

A propulsão dos "jet ski" é realizada por um jato d'água descarregado a alta velocidade (veja o $\odot$ 9.7). Considere as condições operacionais indicadas na Fig. P5.36 e admita que os escoamentos nas seções de alimentação e descarga do "jet ski" se comportem como jatos livres. Nestas condições, determine a vazão de água bombeada para que o empuxo no "jet ski" seja igual a 1335 N.

Fig. P5.36 — jato de descarga diâmetro = 89 mm; Seção de alimentação Área = 0,016 m$^2$; ângulo $30°$.

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

$$u_e \rho (-u_e \cos 30°) A_e + u_s \rho (u_s) A_s = F_x$$

$$\rho \dot{Q}^2 \left( \frac{1}{A_s} - \frac{\cos 30°}{A_e} \right) = F_x$$

$$\dot{Q} = \sqrt{\frac{A_s A_e F_x}{\rho (A_e - A_s \cos 30°)}}$$

![](4/34.png)

## Slide 36

**Direção x:**

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum \vec{F}_{VCC}$$

$$0 + \int_{SC} u \rho \vec{V} \cdot \vec{n} \, dA = F_{RH} - F_x$$

$$u \rho (-u) A_1 + u \rho (u \text{ sen } 20°) A_2 = \rho g h_c A_1 - F_x$$

$$-9 \times 998 \times 1{,}22b + 9 \times \left( \frac{1{,}22}{0{,}3} \right)^2 \times 998 (\text{sen } 20°) 0{,}3b = 998 \times 9{,}81 \times \frac{1{,}22}{2} \times 1{,}22b - F_x$$

$$F_x' = 10958 + 7286 - 15241 = 3003 \text{ N/m}$$

**Direção y:**

$$0 + \int_{SC} v \rho \vec{V} \cdot \vec{n} \, dA = -F_y - W$$

$$-v \rho (v \cos 20°) A_2 = -F_y - W$$

$$-9 \times \left( \frac{1{,}22}{0{,}3} \right)^2 \times 998 (\cos 20°) 0{,}3b = -F_y - 0$$

$$F_y' = 41875 \text{ N/m}$$

$$F' = \sqrt{3003^2 + 41875^2} = 41983 \text{ N/m}$$

![](4/36.png)

## Slide 37

**5.56** A Fig. P5.56 mostra um tanque sendo carregado com um escoamento vertical. O nível do líquido no tanque é constante e o tanque está apoiado num plano horizontal e que não propicia atrito. Determine o módulo da força horizontal necessária para manter o tanque imóvel. Despreze todas as perdas.

Fig. P5.56 — Superfície sem atrito; $F$; Nível constante; jato esquerdo: Área = 1250 mm$^2$, $1$ m abaixo do nível; jato direito: Área = 625 mm$^2$, $2$ m abaixo do nível.

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

$$0 + \int_{SC} u \rho \vec{V} \cdot \vec{n} \, dA = F_x$$

$$-u_1 \rho (u_1) A_1 + u_2 \rho (u_2) A_2 = F_x$$

$$u_1 = \sqrt{2gh_1}$$

$$u_2 = \sqrt{2gh_2}$$

![](4/37.png)

## Slide 38

Determine quais dispositivos se deslocarão para a direita, e quais para a esquerda, quando os vínculos que imobilizam os dispositivos forem retirados. Justifique suas respostas.

(a) Tubo em C; (b) recipiente que expande; (c) tubo em L; (d) recipiente que contrai.

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

(a) $u_e \rho (-u_e) A_e - u_s \rho (u_s) A_s = F_x$

(b) $u_e \rho (-u_e) A_e + u_s \rho (u_s) A_s = F_x$

(c) $u_e \rho (-u_e) A_e = F_x$

(d) $u_e \rho (-u_e) A_e + u_s \rho (u_s) A_s = F_x$

Para (b) e (d):

$$\rho \dot{Q}^2 \left( \frac{A_e - A_s}{A_s A_e} \right) = F_x$$

![](4/38.png)

## Slide 39

### Equação da Energia

#### 1) Derivação

A Primeira Lei da Termodinâmica para um sistema

$$\frac{D}{Dt} \int_{sis} e \rho \, d\forall = (\dot{Q}_{liq.e} + \dot{W}_{liq.e})_{sis}$$

$$\dot{Q}_{liq.e} = \sum \dot{Q}_e - \sum \dot{Q}_s$$

$$\dot{W}_{liq.e} = \sum \dot{W}_e - \sum \dot{W}_s$$

$$e = \bar{u} + gz + \frac{V^2}{2} \implies \text{energia total do sistema}$$

![](4/39.png)

## Slide 40

Do TTR, para um VC fixo e não deformável

$$\frac{\partial}{\partial t} \int_{VC} e \rho \, d\forall + \int_{SC} e \rho \vec{V} \cdot \vec{n} \, dA = (\dot{Q}_{liq.e} + \dot{W}_{liq.e})_{VC}$$

**Taxa de transferência de calor** para dentro do VC é considerada positiva, e para fora é considerada negativa

**Potência de trabalho** é positiva quando trabalho é feito pelo ambiente no conteúdo do VC, e negativo quando o conteúdo do volume de controle realiza trabalho no ambiente

![](4/40.png)

## Slide 41

### Considere o trabalho em um eixo móvel

$$\dot{W}_{eixo} = T_{eixo} \omega,$$

e para mais de um eixo:

$$\dot{W}_{eixo, liq.} = \sum \dot{W}_{eixo, e} - \sum \dot{W}_{eixo, s}$$

Potência também pode ser transferida por forças de tensão normal

$$\delta \dot{W}_{tensão normal} = \delta \vec{F}_{tensão normal} \cdot \vec{V}$$

$$\Rightarrow \delta \dot{W}_{tensão normal} = \sigma \vec{n} \delta A \cdot \vec{V}$$

$$\dot{W}_{tensão normal} = \int_{SC} \sigma \vec{V} \cdot \vec{n} \, dA = \int_{SC} -p \vec{V} \cdot \vec{n} \, dA$$

$\sigma = -p$ para que tensão de compressão forneça um valor positivo para $p$.

Pipe — Section (1), Section (2), Control volume, $u_{max}$, $R$, $r$.

![](4/41.png)

## Slide 42

Desta forma:

$$\frac{\partial}{\partial t} \int_{VC} e\rho \, d\forall + \int_{SC} e\rho \vec{V} \cdot \vec{n} \, dA = \dot{Q}_{liq,e} + \dot{W}_{liq,e} - \int_{SC} p \vec{V} \cdot \vec{n} \, dA$$

Ou

$$\frac{\partial}{\partial t} \int_{VC} e\rho \, d\forall + \int_{SC} \left( \bar{u} + \frac{p}{\rho} + \frac{V^2}{2} + gz \right) \rho \vec{V} \cdot \vec{n} \, dA = \dot{Q}_{liq,e} + \dot{W}_{liq,e}$$

![](4/42.png)

## Slide 43

Para simplificar, a equação de energia será utilizada nos seguintes casos:

* Escoamentos estacionário
* Apenas uma corrente entrando e saindo do VC
* Todas as propriedades estão uniformementes distribuidas ao longo da superfície de controle

$$\int_{SC} \left( \bar{u} + \frac{p}{\rho} + \frac{V^2}{2} + gz \right) \rho \vec{V} \cdot \vec{n} \, dA = \left( \bar{u} + \frac{p}{\rho} + \frac{V^2}{2} + gz \right)_s \dot{m}_s - \left( \bar{u} + \frac{p}{\rho} + \frac{V^2}{2} + gz \right)_e \dot{m}_e$$

e $\quad \sum \dot{m}_s - \sum \dot{m}_e = 0$

$$\dot{m} \left[ \bar{u}_s - \bar{u}_e + \left( \frac{p}{\rho} \right)_s - \left( \frac{p}{\rho} \right)_e + \frac{V_s^2 - V_e^2}{2} + g(z_s - z_e) \right] = \dot{Q}_{liq,e} + \dot{W}_{liq,e}$$

![](4/43.png)

## Slide 44

Desta forma, a equação de energia para escoamento estacionário e unidimensional (compressível ou incompressível) é

$$\dot{m} \left[ \bar{u}_s - \bar{u}_e + \left( \frac{p}{\rho} \right)_s - \left( \frac{p}{\rho} \right)_e + \frac{V_s^2 - V_e^2}{2} + g(z_s - z_e) \right] = \dot{Q}_{liq,e} + \dot{W}_{liq,e}$$

Como a entalpia e definida como $\bar{h} = \bar{u} + \frac{p}{\rho}$

Pode se reescrever a equação acima como

$$\dot{m} \left[ \bar{h}_s - \bar{h}_e + \frac{V_s^2 - V_e^2}{2} + g(z_s - z_e) \right] = \dot{Q}_{liq,e} + \dot{W}_{liq,e}$$

![](4/44.png)

## Slide 45

### A Equação de Bernoulli

Para um escoamento estacionário incompressível e sem trabalho de eixo, a equação da energia por unidade de vazão mássica é

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e - (\bar{u}_s - \bar{u}_e - q_{liq,e})$$

Quando o efeito da viscosidade é desprezado **(sem atrito)**

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e$$

![](4/45.png)

## Slide 46

Comparando as duas equações anteriores, pode-se concluir que para um escoamento sem atrito

$$\bar{u}_s - \bar{u}_e - q_{liq,e} = 0$$

E para um escoamento com atrito

$$\bar{u}_s - \bar{u}_e - q_{liq,e} > 0$$

![](4/46.png)

## Slide 47

Nós sabemos que $\frac{p}{\rho} + \frac{V^2}{2} + gz$ é a energia por unidade de massa, disponível num escoamento

Desta forma

$$\bar{u}_s - \bar{u}_e - q_{liq,e} = \text{perda}$$

A perda da energia útil ou disponível devido ao atrito

Então

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e - \text{perda}$$

![](4/47.png)

## Slide 48

Se a potência de eixo também for incluída na equação, pode-se reescrever a equação como a seguir, se o processo for estacionário

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e + w_{liq,e} - \text{perda}$$

Essa equação é conhecida como

**Equação da energia mecânica**

ou

**Equação de Bernoulli estendida**

![](4/48.png)

## Slide 49

Se a Eq. de Bernoulli extendida for dividida pela aceleração da gravidade, $g$, obtém-se

$$\frac{p_{out}}{\gamma} + \frac{V_{out}^2}{2g} + z_{out} = \frac{p_{in}}{\gamma} + \frac{V_{in}^2}{2g} + z_{in} + h_{eixo} - h_L$$

onde,

$$h_{eixo} = w_{liq,e} / g = \frac{\dot{W}_{liq,e}}{\dot{m}g} = \frac{\dot{W}_{liq,e}}{\gamma Q}, \text{ carga de eixo}$$

Se for o eixo de uma bomba, $h_b = h_{eixo}$

Se for o eixo de uma turbina, $h_T = -h_{eixo}$

$$h_L = \text{perda} / g, \text{ perda de carga}$$

![](4/49.png)

## Slide 51

**Sol:**

Equação de Bernoulli entre 0 e 1

$$\frac{p_0}{\rho g} + \frac{V_0^2}{2g} + z_0 = \frac{p_1}{\rho g} + \frac{V_1^2}{2g} + z_1 \Rightarrow V_1 = V_0$$

Equação de Bernoulli entre 0 e 2

$$\frac{p_0}{\gamma} + \frac{V_0^2}{2g} + z_0 = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 \Rightarrow V_2 = V_0$$

Equação da continuidade

$$V_0 A_0 = V_1 A_1 + V_2 A_2$$

$$\frac{\partial}{\partial t} \int_{cv} \vec{V} \rho \, d\forall + \int_{cs} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{\substack{contents \\ ccv}}$$

$$\begin{cases} (\rho A_1 V_1^2 \cos \alpha - \rho A_2 V_2^2 \cos \alpha) - \rho A_0 V_0^2 = -N \sin \alpha \\ (\rho A_1 V_1^2 \sin \alpha - \rho A_2 V_2^2 \sin \alpha) - 0 = N \cos \alpha \end{cases}$$

![](4/51.png)

## Slide 52

$$\begin{cases}
(\rho A_1 V_1^2 \cos \alpha - \rho A_2 V_2^2 \cos \alpha) - \rho A_0 V_0^2 = -N \sin \alpha \\
(\rho A_1 V_1^2 \sin \alpha - \rho A_2 V_2^2 \sin \alpha) - 0 = N \cos \alpha \\
V_0 A_0 = V_1 A_1 + V_2 A_2
\end{cases}$$

$$\begin{cases}
(10^3 \times 5^2 \times \text{ctg } 40° A_1 - 10^3 \times 5^2 \times \text{ctg } 40° A_2) - \frac{10^3 \times 5^2 \times 0{,}008}{\sin 40°} = -N \\
10^3 \times 5^2 \times \text{tg } 40° A_1 - 10^3 \times 5^2 \times \text{tg } 40° A_2 = N \\
0{,}008 = A_1 + A_2
\end{cases}$$

$$\begin{cases}
29794 A_1 - 29794 A_2 - 311{,}1 = -N \\
20977 A_1 - 20977 A_2 = N \\
0{,}008 = A_1 + A_2
\end{cases}$$

$$\begin{cases}
N = 126{,}8 \text{ (N)} \\
A_1 = 0{,}0071 \text{ (m}^2\text{)} \\
A_2 = 0{,}0009 \text{ (m}^2\text{)}
\end{cases}$$

![](4/52.png)

## Slide 54

Figura P5.122 — Óleo; Bomba; diâmetro $305$ mm; diâmetro $152$ mm; manômetro: $914$ mm; $H$; $h$.

$$\frac{p_s}{\gamma} + \frac{V_s^2}{2g} + z_s = \frac{p_e}{\gamma} + \frac{V_e^2}{2g} + z_e + h_{\text{eixo}} - h_L$$

![](4/54.png)

## Slide 55

$$\frac{p_s}{\gamma} + \frac{V_s^2}{2g} + z_s = \frac{p_e}{\gamma} + \frac{V_e^2}{2g} + z_e + h_{eixo} - h_L$$

$$h_{eixo} = \frac{w_{liq.e}}{g} = \frac{\dot{W}_{liq.e}}{\dot{m}g} = \frac{\dot{W}_{liq.e}}{\gamma \dot{Q}}$$

$$\dot{Q} = A \cdot V \Rightarrow V = \frac{\dot{Q}}{A}$$

$$h_L = \frac{\text{perda}}{g} = 0$$

$$h_{eixo} = \frac{\dot{W}_{liq.e}}{\gamma \dot{Q}} = \frac{p_s - p_e}{\gamma} + \frac{8}{g} \left( \frac{\dot{Q}}{\pi} \right)^2 \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right) + z_s - z_e$$

$$\dot{W}_{liq.e} = \dot{Q}(p_s - p_e) + \frac{8\rho\dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right) + \gamma\dot{Q}(z_s - z_e)$$

![](4/55.png)

## Slide 56

Figura P5.122 — $p_x$ na linha de referência do manômetro.

$$\dot{W}_{liq,e} = \dot{Q}(p_s - p_e) + \frac{8\rho\dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right) + \gamma\dot{Q}(z_s - z_e)$$

$$p_x = \gamma_{oleo}(0{,}914 + H + h) + p_s$$

$$p_x = \gamma_{merc} \cdot 0{,}914 + \gamma_{oleo} H + p_e$$

$$p_s - p_e = 0{,}914(\gamma_{merc} - \gamma_{oleo}) - \gamma_{oleo}h$$

$$\dot{W}_{liq,e} = \dot{Q} \cdot 0{,}914 \cdot (\gamma_{merc} - \gamma_{oleo}) - \dot{Q}\gamma_{oleo}h + \frac{8\rho\dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right) + \dot{Q}\gamma_{oleo}h$$

![](4/56.png)

## Slide 57

$$\dot{W}_{liq,e} = \dot{Q} \cdot 0{,}914 \cdot (\gamma_{merc} - \gamma_{oleo}) - \dot{Q} \gamma_{oleo} h + \frac{8 \rho \dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right) + \dot{Q} \gamma_{oleo} h$$

$$\dot{W}_{liq,e} = \dot{Q} \cdot 0{,}914 \cdot (\gamma_{merc} - \gamma_{oleo}) + \frac{8 \rho \dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right)$$

$$[W] = \left[\frac{m^3}{s}\right] \cdot [m] \cdot \left[\frac{N}{m^3}\right] + \left[\frac{kg}{m^3}\right] \left[\frac{m^9}{s^3}\right] \left[\frac{1}{m^4}\right]$$

$$\left[\frac{N \cdot m}{s}\right] = \left[\frac{N \cdot m}{s}\right] + \left[\frac{kg \cdot m^2}{s^3}\right]$$

$$\left[\frac{N \cdot m}{s}\right] = \left[\frac{N \cdot m}{s}\right] + \left[\frac{N \cdot m}{s}\right]$$

![](4/57.png)

## Formulário — Parte 4

### Fórmulas dos slides (organizadas por tópico)

#### Teorema do transporte de Reynolds (TTR)

$$B = mb$$

$$B_{sis} = \int_{sis} \rho b \, d\forall$$

$$\frac{DB_{Sis}}{Dt} = \frac{\partial B_{VC}}{\partial t} + \dot{B}_S - \dot{B}_E$$

$$\frac{DB_{Sis}}{Dt} = \frac{\partial}{\partial t} \int_{VC} \rho b \, d\forall + \int_{SC} \rho b \vec{V} \cdot \vec{n} \, dA$$

$$\dot{B}_s = \int_{SC_s} \rho b \vec{V} \cdot \vec{n} \, dA$$

$$\dot{B}_E = - \int_{SC_E} \rho b \vec{V} \cdot \vec{n} \, dA$$

$$\int_{SC} \rho b \vec{V} \cdot \vec{n} \, dA = \dot{B}_S - \dot{B}_E$$

#### Equação da continuidade

$$\frac{DM_{sis}}{Dt} = 0$$

$$M_{sis} = \int_{sis} \rho \, d\forall$$

$$\frac{\partial}{\partial t} \int_{VC} \rho \, d\forall + \int_{SC} \rho \vec{V} \cdot \vec{n} \, dA = 0$$

$$\dot{m} = \rho \dot{Q} = \rho A \overline{V}$$

$$\overline{V} = \frac{\int_{A} \vec{V} \cdot \vec{n} \, dA}{A} \quad \text{(cte } \rho)$$

$$\frac{\partial M_{VC}}{\partial t} = \dot{M}_E - \dot{M}_S = \rho_E \dot{Q}_E - \rho_S A_S V_S$$

$$\frac{\partial \rho}{\partial t} = \frac{\rho_E \dot{Q}_E - \rho_S A_S V_S}{\forall_{VC}}$$

#### Equação da quantidade de movimento linear

$$\frac{D}{Dt} \int_{sis} \vec{V} \rho \, d\forall = \sum F_{sis}$$

$$\sum F_{sis} = \sum F_{VCC}$$

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall + \int_{SC} \vec{V} \rho \vec{V} \cdot \vec{n} \, dA = \sum F_{VCC}$$

$$\frac{\partial}{\partial t} \int_{VC} \vec{V} \rho \, d\forall = 0 \quad \text{(regime permanente)}$$

$$F_A = \dot{m}(w_1 - w_2) + W_n + p_1 A_1 + W_w - p_2 A_2$$

$$F_x = \rho A V^2 (1 - \cos \theta)$$

$$\rho \dot{Q}^2 \left( \frac{1}{A_s} - \frac{\cos \theta}{A_e} \right) = F_x$$

$$\rho \dot{Q}^2 \left( \frac{A_e - A_s}{A_s A_e} \right) = F_x$$

#### Equação da energia

$$\frac{D}{Dt} \int_{sis} e \rho \, d\forall = (\dot{Q}_{liq.e} + \dot{W}_{liq.e})_{sis}$$

$$e = \bar{u} + gz + \frac{V^2}{2}$$

$$\dot{Q}_{liq.e} = \sum \dot{Q}_e - \sum \dot{Q}_s$$

$$\dot{W}_{liq.e} = \sum \dot{W}_e - \sum \dot{W}_s$$

$$\frac{\partial}{\partial t} \int_{VC} e \rho \, d\forall + \int_{SC} e \rho \vec{V} \cdot \vec{n} \, dA = (\dot{Q}_{liq.e} + \dot{W}_{liq.e})_{VC}$$

$$\frac{\partial}{\partial t} \int_{VC} e\rho \, d\forall + \int_{SC} \left( \bar{u} + \frac{p}{\rho} + \frac{V^2}{2} + gz \right) \rho \vec{V} \cdot \vec{n} \, dA = \dot{Q}_{liq,e} + \dot{W}_{liq,e}$$

$$\dot{W}_{eixo} = T_{eixo} \omega$$

$$\dot{W}_{tensão normal} = \int_{SC} -p \vec{V} \cdot \vec{n} \, dA$$

$$\dot{m} \left[ \bar{h}_s - \bar{h}_e + \frac{V_s^2 - V_e^2}{2} + g(z_s - z_e) \right] = \dot{Q}_{liq,e} + \dot{W}_{liq,e}$$

$$\bar{h} = \bar{u} + \frac{p}{\rho}$$

#### Bernoulli e energia mecânica

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e$$

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e + w_{liq,e} - \text{perda}$$

$$\frac{p_{out}}{\gamma} + \frac{V_{out}^2}{2g} + z_{out} = \frac{p_{in}}{\gamma} + \frac{V_{in}^2}{2g} + z_{in} + h_{eixo} - h_L$$

$$h_{eixo} = \frac{\dot{W}_{liq,e}}{\gamma \dot{Q}}$$

$$h_L = \frac{\text{perda}}{g}$$

$$h_b = h_{eixo} \quad \text{(bomba)}$$

$$h_T = -h_{eixo} \quad \text{(turbina)}$$

$$\bar{u}_s - \bar{u}_e - q_{liq,e} = \text{perda}$$

### Fórmulas relacionadas (usadas nas questões)

#### Lei de Torricelli

$$u = \sqrt{2gh}$$

#### Manometria

$$p_s - p_e = \Delta h (\gamma_{merc} - \gamma_{fluido}) - \gamma_{fluido} h$$

#### Potência da bomba

$$\dot{W}_{liq,e} = \dot{Q}(p_s - p_e) + \frac{8\rho\dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right) + \gamma\dot{Q}(z_s - z_e)$$

$$\dot{W}_{liq,e} = \dot{Q} \cdot \Delta h_{man} \cdot (\gamma_{merc} - \gamma_{oleo}) + \frac{8 \rho \dot{Q}^3}{\pi^2} \left( \frac{1}{D_s^4} - \frac{1}{D_e^4} \right)$$

#### Equilíbrio de momentos (tombamento)

$$\sum M_O = 0 \quad \implies \quad R_x = \frac{W l_W}{l_{R_x}}$$

#### Continuidade e Bernoulli (jato em placa)

$$V_1 = V_2 = V_0$$

$$V_0 A_0 = V_1 A_1 + V_2 A_2$$

#### Densidade — condição padrão (ISA)

$$\rho_{ar} \approx 1{,}225 \text{ kg/m}^3 \quad \text{(101,3 kPa, 15 °C)}$$

#### Peso específico

$$\gamma = \rho g$$

#### Vazão volumétrica

$$\dot{Q} = A V = \frac{\pi}{4} D^2 V$$
