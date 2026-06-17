# Forças hidrostáticas em uma superfície plana

## Slide 1

A determinação dessas forças é importante no projeto de tanques, barragens, navios e outras estruturas hidráulicas

*Assume se que não há tensões de cisalhamento no fluido*

![](2/1.png)

## Slide 2 — Antes de continuar...

**Centroide:** Ponto que pode ser considerado como o centro geométrico de uma figura. A soma da distância entre todos pontos e o centroide é zero.

![](2/2.png)

## Slide 3

Considere forças agindo em um plano inclinado de forma arbitrária

O sistema de coordenada x-y é definido para que **0** seja a origem e **y** seja na direção ao longo da superfície

Em qualquer profundidade

$$dF = \gamma h \, dA$$

E a magnitude da força resultante é

$$F_R = \int_A \gamma h \, dA = \int_A \gamma y \sin\theta \, dA$$

![](2/3.png)

## Slide 4

Sendo $\gamma$ e $\theta$ constantes

$$F_R = \gamma \sin\theta \int_A y \, dA$$

Esta integral é conhecida como **primeiro momento de área** em relação ao eixo X e

$$\int_A y \, dA = y_c A$$

Onde $y_c$ é a coordenada y do centroide, medida a partir do eixo x

![](2/4.png)

## Slide 5

E a **magnitude** da força resultante é

$$F_R = \gamma A y_c \sin\theta = \gamma h_c A$$

A direção é perpendicular a superfície.

Onde ela age (**posição $X_R$ e $Y_R$**)?

![](2/5.png)

## Slide 6 — Na coordenada y...

O momento da força resultante tem que ser igual ao momento da força distribuida.

$$F_R y_R = \int_A y \, dF = \int_A \gamma \sin\theta \, y^2 \, dA$$

então

$$y_R = \frac{\int_A y^2 \, dA}{y_c A}$$

A integral do numerado é chamada de **momento de segunda ordem da área $I_x$ ou momento de inércia**

![](2/6.png)

## Slide 7

Ou reescrevendo como

$$y_R = \frac{I_x}{y_c A}$$

Aplicando o Teorema do Eixo Paralelo

$$I_x = I_{xc} + A y_c^2$$

Onde $I_{xc}$ é o **momento de inércia** em relação a um eixo que passa pelo centroide e é paralelo ao eixo x

![](2/7.png)

## Slide 8

Então...

$$y_R = \frac{I_{xc}}{y_c A} + y_c$$

A posição da força resultante na coordenada **x** pode ser determinada de maneira semelhante

$$x_R = \frac{I_{xyc}}{y_c A} + x_c$$

![](2/8.png)

## Slide 9

$$F_R x_R = \int_A x \, dF = \int_A \gamma \sin\theta \, x y \, dA \Rightarrow x_R = \frac{\gamma \sin\theta \int_A x y \, dA}{\gamma \sin\theta \, y_C A} = \frac{\int_A x y \, dA}{y_C A} = \frac{I_{xy}}{y_C A}$$

$$I_{xy} = I_{xyc} + x_C y_C A$$

$$x_R = \frac{I_{xyc}}{y_C A} + x_C$$

Onde $I_{xyc}$ é o produto de inércia em relação ao sistema de coordenada ortogonal que passa pelo centroide e criado pela translação dos eixos x e y.

Em mecânica clássica, o produto de inércia mede a anti-simetria da distribuição de massa de um corpo em relação a um par de eixos e em relação ao seu baricentro.

![](2/9.png)

## Slide 10 — Propriedades geometricas de algumas formas

**(a) Retângulo** — $A = ba$; $I_{xc} = \frac{1}{12} b a^3$; $I_{yc} = \frac{1}{12} a b^3$; $I_{xyc} = 0$

**(b) Círculo** — $A = \pi R^2$; $I_{xc} = I_{yc} = \frac{\pi R^4}{4}$; $I_{xyc} = 0$

**(c) Semicírculo** — $A = \frac{\pi R^2}{2}$; $I_{xc} = 0{,}1098 \, R^4$; $I_{yc} = 0{,}3927 \, R^4$; $I_{xyc} = 0$

**(d) Triângulo** — $A = \frac{a b}{2}$; $I_{xc} = \frac{b a^3}{36}$; $I_{xyc} = \frac{b a^2}{72}(b - 2d)$

**(e) Quarto de círculo** — $A = \frac{\pi R^2}{4}$; $I_{xc} = I_{yc} = 0{,}05488 \, R^4$; $I_{xyc} = -0{,}01647 \, R^4$

![](2/10.png)

## Slide 11 — Como calcular a localização do centroide?

**Fig. 2.18 ou**

$$C_x = \frac{\int x \, dA}{A} = \frac{\int x y \, dx}{A}$$

$$C_y = \frac{\int y \, dA}{A} = \frac{\int y^2 \, dx}{A}$$

$$A = \int f(x) \, dx$$

**Para geometrias complexas**

$$C_x = \frac{\sum_n A_n C_{xn}}{\sum_n A_n}$$

$$C_y = \frac{\sum_n A_n C_{yn}}{\sum_n A_n}$$

![](2/11.png)

## Slide 12 — Forças hidrostáticas em uma superfície curva

Considera-se o fluido envolto pela superfície curva e suas projeções na direção vertical e horizontal

$F_V$ e $F_H$ são forças do tanque agindo no fluido

No equilíbrio, essas forças estão balanceadas com forças colineares, concorrentes e coplanares.

$$F_V = W + F_1$$

$$F_H = F_2$$

$$F_R = \sqrt{(F_H)^2 + (F_V)^2}$$

![](2/12.png)

## Slide 17 — PRINCÍPIO DE ARQUIMEDES

- Um corpo total ou parcialmente imerso em um fluido é sustentado por uma força (**empuxo**) cuja intensidade é igual ao peso do fluido deslocado pelo corpo
- Quando $\rho_{fl} > \rho_{ob}$
  - Peso deslocado (**empuxo**) > peso do objeto (**flutua**)
- Quando $\rho_{fl} < \rho_{ob}$
  - Peso deslocado (**empuxo**) < peso do objeto (**afunda**)

![](2/17.png)

## Slide 18 — Princípio de Arquimedes

$$F_E = \rho g \mathcal{V}$$

$F_E$ passa pelo centro de gravidade do volume deslocado pelo objeto. Esse ponto é conhecido como centro de sustentação.

![](2/18.png)

## Slide 19

**Empuxo atua no centro de sustentação (centroide)**

**Peso atua no centro de gravidade do objeto**

Objeto imerso ou parcialmente imerso pode estar em **equilíbrio estável** ou **equilíbrio instável**.

![](2/19.png)

## Slide 20 — Objeto submerso

Quando o centro de gravidade está abaixo do centro de sustentação

$\rightarrow$ equilíbrio estável

Figura 2.25 Estabilidade de um corpo submerso - centro de gravidade abaixo do centróide.

**Estável** — Momento de restauração

Quando o centro de gravidade está acima do centro de sustentação

$\rightarrow$ equilíbrio instável

Figura 2.26 Estabilidade de um corpo submerso - centro de gravidade acima do centróide.

**Instável** — Momento de instabilização

![](2/20.png)

## Slide 21 — Equilíbrio estável

Para objetos parcialmente submersos, o centro de sustentação pode mudar, de acordo com o volume submerso

$c =$ centróide do volume original deslocado

$c' =$ centróide do novo volume deslocado

**Momento de restauração**

**Equilíbrio estável**

![](2/21.png)

## Slide 22 — Equilíbrio instável

$c =$ centróide do volume original deslocado

$c' =$ centróide do novo volume deslocado

**Momento de instabilização**

**Equilíbrio instável**

![](2/22.png)

---

## Formulário — Parte 2

### Fórmulas dos slides (organizadas por tópico)

#### Força hidrostática elementar e resultante (superfície plana inclinada)

$$dF = \gamma h \, dA$$

$$h = y \sin\theta$$

$$F_R = \int_A \gamma h \, dA = \int_A \gamma y \sin\theta \, dA$$

$$F_R = \gamma \sin\theta \int_A y \, dA$$

$$F_R = \gamma A y_c \sin\theta = \gamma h_c A$$

#### Primeiro momento de área e centroide

$$\int_A y \, dA = y_c A$$

$$C_x = \frac{\int x \, dA}{A} = \frac{\int x y \, dx}{A}$$

$$C_y = \frac{\int y \, dA}{A} = \frac{\int y^2 \, dx}{A}$$

$$A = \int f(x) \, dx$$

$$C_x = \frac{\sum_n A_n C_{xn}}{\sum_n A_n}, \quad C_y = \frac{\sum_n A_n C_{yn}}{\sum_n A_n}$$

#### Centro de pressão (superfície plana)

$$F_R y_R = \int_A y \, dF$$

$$y_R = \frac{\int_A y^2 \, dA}{y_c A} = \frac{I_x}{y_c A}$$

$$y_R = \frac{I_{xc}}{y_c A} + y_c$$

$$x_R = \frac{\int_A x y \, dA}{y_c A} = \frac{I_{xy}}{y_c A}$$

$$x_R = \frac{I_{xyc}}{y_c A} + x_c$$

#### Teorema dos eixos paralelos

$$I_x = I_{xc} + A y_c^2$$

$$I_{xy} = I_{xyc} + x_c y_c A$$

#### Propriedades geométricas (referência)

Retângulo: $A = ba$; $I_{xc} = \frac{1}{12} b a^3$; $I_{yc} = \frac{1}{12} a b^3$; $I_{xyc} = 0$

Círculo: $A = \pi R^2$; $I_{xc} = I_{yc} = \frac{\pi R^4}{4}$; $I_{xyc} = 0$

Semicírculo: $A = \frac{\pi R^2}{2}$; $I_{xc} = 0{,}1098 R^4$; $I_{yc} = 0{,}3927 R^4$; $I_{xyc} = 0$

Triângulo: $A = \frac{a b}{2}$; $I_{xc} = \frac{b a^3}{36}$; $I_{xyc} = \frac{b a^2}{72}(b - 2d)$

Quarto de círculo: $A = \frac{\pi R^2}{4}$; $I_{xc} = I_{yc} = 0{,}05488 R^4$; $I_{xyc} = -0{,}01647 R^4$

#### Forças em superfície curva

$$F_V = W + F_1$$

$$F_H = F_2$$

$$F_R = \sqrt{F_H^2 + F_V^2}$$

#### Princípio de Arquimedes e flutuabilidade

$$F_E = \rho g \mathcal{V} = \gamma \mathcal{V}$$

$$\rho_{fl} > \rho_{ob} \Rightarrow \text{flutua}$$

$$\rho_{fl} < \rho_{ob} \Rightarrow \text{afunda}$$

### Fórmulas relacionadas (usadas nas questões)

#### Pressão e peso específico

$$p = \gamma h$$

$$\gamma = \rho g$$

#### Força hidrostática em comportas e anteparos planos

$$F_R = \gamma h_c A$$

$$M = F_R \cdot d$$

#### Superfície curva — componentes e momento

$$F_H = \gamma h_{cg} A_{proj,\,vertical}$$

$$F_V = \gamma \mathcal{V}_{fluido\,acima\,da\,superficie}$$

#### Empuxo, peso aparente e densidade relativa

$$E = \rho g \mathcal{V}_{deslocado}$$

$$W_{liquido} = W_{ar} - E$$

$$SG = \frac{\rho}{\rho_{ref}} = \frac{W_{ar}}{W_{ar} - W_{agua}}$$

$$\rho_{coroa} = \frac{W_a}{W_a - W_w} \cdot \rho_{agua}$$

#### Equilíbrio de corpos flutuantes

$$E = W$$

$$\sum F = ma \Rightarrow E - W = m_{total} \cdot a$$

#### Ar quente em balão (gás ideal, pressão padrão)

$$\rho = \frac{p M}{R T}$$

$$E = \rho_{ar\,externo} \cdot g \cdot \mathcal{V}_{balao}$$

$$W_{total} = E$$

#### Mistura água-ar (afundamento)

$$\rho_{mistura} < \rho_{agua} \Rightarrow E_{reduzido} < W \Rightarrow \text{afunda}$$
