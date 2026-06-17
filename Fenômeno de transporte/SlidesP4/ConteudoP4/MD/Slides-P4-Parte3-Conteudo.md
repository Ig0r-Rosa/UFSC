# Escoamentos viscosos e não viscosos

## Slide 1

* Equações de Euler
* Equação de Bernoulli
* Escoamento viscoso em tubulações

![](3/1.png)

## Slide 2

### Equações Diferencial Geral do Movimento do Fluido

Superfície arbitrária com área $\delta A$ e força resultante $\delta \mathbf{F}_s$ decomposta em componentes normal $\delta F_n$ e tangenciais $\delta F_1$, $\delta F_2$.

$$\sigma_n = \lim_{\delta A \to 0} \frac{\delta F_n}{\delta A}$$

$$\tau_1 = \lim_{\delta A \to 0} \frac{\delta F_1}{\delta A}$$

$$\tau_2 = \lim_{\delta A \to 0} \frac{\delta F_2}{\delta A}$$

![](3/2.png)

## Slide 3

### Equações Diferencial Geral do Movimento do Fluido

Primeira letra subscrita: eixo normal à superfície que a força age

Segunda letra subscrita: eixo paralelo à direção que a força age

Faces normais a $x$: tensões $\sigma_{xx}$, $\tau_{xy}$, $\tau_{xz}$

![](3/3.png)

## Slide 4

### Equações Diferencial Geral do Movimento do Fluido

$$\delta F_x = \delta m \, a_x; \quad \delta F_y = \delta m \, a_y; \quad \delta F_z = \delta m \, a_z$$

**Forças de superfície na direção $x$ agindo em um elemento de fluido**

Elemento com dimensões $\delta x$, $\delta y$, $\delta z$:

* Face esquerda: $\left(\sigma_{xx} - \frac{\partial \sigma_{xx}}{\partial x} \frac{\delta x}{2}\right) \delta y \delta z$
* Face direita: $\left(\sigma_{xx} + \frac{\partial \sigma_{xx}}{\partial x} \frac{\delta x}{2}\right) \delta y \delta z$
* Face superior: $\left(\tau_{yx} + \frac{\partial \tau_{yx}}{\partial y} \frac{\delta y}{2}\right) \delta x \delta z$
* Face inferior: $\left(\tau_{yx} - \frac{\partial \tau_{yx}}{\partial y} \frac{\delta y}{2}\right) \delta x \delta z$
* Face frontal: $\left(\tau_{zx} + \frac{\partial \tau_{zx}}{\partial z} \frac{\delta z}{2}\right) \delta x \delta y$
* Face traseira: $\left(\tau_{zx} - \frac{\partial \tau_{zx}}{\partial z} \frac{\delta z}{2}\right) \delta x \delta y$

![](3/4.png)

## Slide 5

### Equações Diferencial Geral do Movimento do Fluido

Aplicável em qualquer meio contínuo (sólido e fluido), em movimento ou repouso (**Efeitos viscosos incluídos**)

Mais incógnitas que equações (tensões e velocidades)

$$\rho g_x + \frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \tau_{yx}}{\partial y} + \frac{\partial \tau_{zx}}{\partial z} = \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right)$$

$$\rho g_y + \frac{\partial \tau_{xy}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} + \frac{\partial \tau_{zy}}{\partial z} = \rho \left( \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right)$$

$$\rho g_z + \frac{\partial \tau_{xz}}{\partial x} + \frac{\partial \tau_{yz}}{\partial y} + \frac{\partial \sigma_{zz}}{\partial z} = \rho \left( \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} \right)$$

![](3/5.png)

## Slide 6

### Equações de Euler

Quando não há viscosidade, não há tensão de cisalhamento, e as tensões normais têm a mesma magnitude da pressão

$$\rho g_x - \frac{\partial p}{\partial x} = \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right)$$

$$\rho g_y - \frac{\partial p}{\partial y} = \rho \left( \frac{\partial v}{\partial t} + u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} + w \frac{\partial v}{\partial z} \right)$$

$$\rho g_z - \frac{\partial p}{\partial z} = \rho \left( \frac{\partial w}{\partial t} + u \frac{\partial w}{\partial x} + v \frac{\partial w}{\partial y} + w \frac{\partial w}{\partial z} \right)$$

![](3/6.png)

## Slide 7

### Análise das equações de Euler ao longo e normal a uma linha de corrente

* Linhas tangentes ao vetor velocidade em um campo de escoamento
* No escoamento estacionário, as linhas não se cruzam (partículas poderiam seguir em mais de uma direção e o escoamento não seria estacionário)

**Figura 3.1** (a) Escoamento no plano $x$-$z$. (b) Descrição do escoamento utilizando as coordenadas da linha de corrente ($s$, $n$; raio de curvatura $\mathcal{R} = \mathcal{R}(s)$).

![](3/7.png)

## Slide 8

### Linhas de corrente

Em um escoamento estacionário, todas as partículas que passam por um ponto $Q_0$ em cima de uma linha de corrente, passarão pelos outros pontos desta linha de corrente

**Figura 3.1** (a) Escoamento no plano $x$-$z$. (b) Descrição do escoamento utilizando as coordenadas da linha de corrente.

![](3/8.png)

## Slide 9

### Forças agindo ao longo de uma linha de corrente

* Assuma uma partícula de fluido movendo-se em uma linha de corrente
    * Coordenada baseada na linha de corrente
* O movimento do fluido é governado apenas por forças de pressão e da gravidade.

![](3/9.png)

## Slide 10

Diagrama de forças em um elemento de fluido ao longo de uma linha de corrente:

* Dimensões: $\delta s$ (ao longo da linha), $\delta n$ (normal), $\delta y$ (espessura = $\delta y$)
* Vetores unitários: $\hat{s}$, $\hat{n}$; raio de curvatura $\mathcal{R}$
* Forças de pressão em $s$: $(p - \delta p_s)\delta n \delta y$ e $(p + \delta p_s)\delta n \delta y$
* Forças de pressão em $n$: $(p - \delta p_n)\delta s \delta y$ e $(p + \delta p_n)\delta s \delta y$
* Peso: $\delta \mathcal{W}$ com componentes $\delta \mathcal{W}_s$ e $\delta \mathcal{W}_n$
* Tensão de cisalhamento: $\tau \delta s \delta y = 0$
* Geometria: $\sin \theta = \delta z / \delta s$; $\cos \theta = \delta z / \delta n$

![](3/10.png)

## Slide 11

### A Segunda Lei de Newton ao longo da linha de corrente

$$\sum \delta F_s = \delta m \, a_s = \delta m \, V \frac{\partial V}{\partial s} = \rho \delta \forall \, V \frac{\partial V}{\partial s}$$

onde $\delta \forall = \delta s \delta n \delta y$ é o volume da partícula

$$a_s = \frac{dV}{dt} = \frac{\partial V}{\partial s} \frac{ds}{dt} = \frac{\partial V}{\partial s} V$$

A força da gravidade é:

$$\delta W_s = -\delta W \sin \theta = -\gamma \delta \forall \sin \theta$$

![](3/11.png)

## Slide 12

Como a partícula de fluido é pequena, podemos aproximar

$$\delta p_s \approx \frac{\partial p}{\partial s} \frac{\delta s}{2}$$

Desta forma, a força de pressão resultante

$$\delta F_{ps} = (p - \delta p_s)\delta n \delta y - (p + \delta p_s)\delta n \delta y = -2\delta p_s \delta n \delta y$$

$$= -\frac{\partial p}{\partial s} \delta s \delta n \delta y = -\frac{\partial p}{\partial s} \delta \forall$$

![](3/12.png)

## Slide 13

E a força resultante agindo ao longo da linha de corrente é:

$$\sum \delta F_s = \delta W_s + \delta F_{ps} = \left( -\gamma \sin \theta - \frac{\partial p}{\partial s} \right) \delta \forall$$

Combinado as equações anteriores, obtemos a equação do movimento na direção de uma linha de corrente:

$$-\gamma \sin \theta - \frac{\partial p}{\partial s} = \rho V \frac{\partial V}{\partial s}$$

![](3/13.png)

## Slide 14

Ao longo da linha de corrente $\sin \theta = dz / ds$

E pode-se escrever

$$V \frac{dV}{ds} = \frac{1}{2} \frac{d(V^2)}{ds}; \quad \frac{\partial p}{\partial s} = \frac{dp}{ds}$$

A equação anterior pode ser escrita da seguinte maneira (ao longo da linha de corrente)

$$-\gamma \frac{dz}{ds} - \frac{dp}{ds} = \frac{1}{2} \rho \frac{d(V^2)}{ds}$$

![](3/14.png)

## Slide 15

E simplificando (ao longo da linha de corrente)

$$dp + \frac{1}{2} \rho \, d(V^2) + \gamma \, dz = 0$$

Para fluido incompressível, pode-se integrar (ao longo da linha de corrente)

$$p + \frac{1}{2} \rho V^2 + \gamma z = C$$

------Equação de **Bernoulli**

![](3/15.png)

## Slide 16

### Forças normal a uma linha de corrente

Considerando a mesma partícula de fluido descrita anteriormente...

A segunda lei de Newton na direção normal é:

$$\sum \delta F_n = \frac{\delta m \, V^2}{\mathcal{R}} = \frac{\rho \delta \forall \, V^2}{\mathcal{R}}$$

![](3/16.png)

## Slide 17

De maneira similar, a força resultante agindo na direção normal é:

$$\sum \delta F_n = \delta W_n + \delta F_{pn} = \left( -\gamma \cos \theta - \frac{\partial p}{\partial n} \right) \delta \forall$$

E a equação do movimento ao longo da direção normal é:

$$-\gamma \frac{dz}{dn} - \frac{dp}{dn} = \frac{\rho V^2}{\mathcal{R}}$$

ou

$$p + \gamma z + \int \frac{\rho V^2}{\mathcal{R}} \, dn = C$$

Com $\cos \theta = dz / dn$

![](3/17.png)

## Slide 18

### Interpretação física da Eq. de Bernoulli

Se cada termo da Eq. de Bernoulli for dividido pelo peso específico do fluido

$$\frac{p}{\gamma} + \frac{V^2}{2g} + z = C$$

Cada termo tem uma dimensão de energia por peso ou de comprimento, e representa um tipo de carga

![](3/18.png)

## Slide 19

Termo de elevação ($z$, carga de elevação)
*Relacionado à energia potencial da partícula*

Termo de pressão ($p/\gamma$, carga de pressão)
*Altura de uma coluna de líquido que produz uma pressão $p$*

Termo de velocidade ($V^2/2g$, carga de velocidade)
*Distância vertical para que um fluido em queda livre acelere do repouso até a velocidade $V$, desprezando o atrito.*

De acordo com a Eq. de Bernoulli, a soma de todas as cargas (ou a energia total do sistema) é constante ao longo de uma linha de corrente

*A Eq. de Bernoulli é um tipo de equação de conservação de energia*

![](3/19.png)

## Slide 20

### Pressão estática, dinâmica e total

Na Eq. de Bernoulli

$p$ ----- *pressão estática*,

$\gamma z$ ---- *pressão hidrostática*,

$\rho V^2 / 2$ ----- *pressão dinâmica*.

Estático, i.e., se movendo junto do fluido e sendo estático em relação ao fluido em movimento

![](3/20.png)

## Slide 21

### Pressão estática

O fluido entre (3) e (4) está estacionário e entre (1) e (3) se move com a mesma velocidade (sem tensões de cisalhamento)

$$p_1 = p_3 + \gamma h_{3-1}$$

$$p_3 = p_0 + \gamma h_{4-3}$$

$$p_1 = p_0 + \gamma h$$

![](3/21.png)

## Slide 22

No ponto 2, $V_2 = 0$ ---- *ponto de estagnação*

Aplicando a Eq. de Bernoulli,

$$p_2 = p_1 + \frac{1}{2} \rho V_1^2$$

**Pressão de estagnação**

![](3/22.png)

## Slide 23

### Pressão hidrostática

* Não é realmente uma pressão, mas uma possível variação de pressão devido a variação da energia potencial do fluido (variação de altura)

![](3/23.png)

## Slide 24

A soma das pressões estática, dinâmica e hidrostática é a *pressão total*

E de acordo com a Eq. de Bernoulli, a pressão total se mantém constante ao longo de uma linha de corrente

$$p + \frac{1}{2} \rho V^2 + \gamma z = p_T = C$$

![](3/24.png)

## Slide 26

### 3) Restrições ao uso da Eq. de Bernoulli

A Eq. de Bernoulli se aplica nas seguintes situações:

a) Fluidos incompressíveis

b) Fluxo estacionários

c) Fluidos não viscosos

d) Sem perdas de cargas e bombas

![](3/26.png)

## Slide 27

### Restrições ao uso da Eq. de Bernoulli

* Fluido incompressível: Gás pode ser considerado incompressível, exceto quando a pressão dinâmica é relativamente grande.
    * Gás considerado como incompressível se
    * $Ma < 0{,}3 \Rightarrow Ma = V/c \Rightarrow$

$$c = \sqrt{kRT} = 332 \text{ m/s} \Rightarrow V = 1195 \text{ km/h}$$

$$T = 15°\text{C}$$

![](3/27.png)

## Slide 28

### Restrições ao uso da Eq. de Bernoulli

* Fluxo estacionário $\Rightarrow V = f(s)$;
* Fluxo transiente $\Rightarrow V = f(s,t)$

$$a_s = V \frac{\partial V}{\partial s}$$

$$a_s = V \frac{\partial V}{\partial s} + \frac{\partial V}{\partial t}$$

![](3/28.png)

## Slide 29

### Restrições ao uso da Eq. de Bernoulli

* Fluido não viscoso, e sem perdas de carga ou bombas:
    * Nenhum termo relativo a força viscosa, a perda de carga ou a adição de energia foi incluído na equação geral do movimento do fluido (apenas forças relativas a pressão e a gravidade)

![](3/29.png)

## Slide 30

### Exemplos da utilização da Eq. de Bernoulli

Para dois pontos ao longo de uma linha de corrente:

$$p_1 + \frac{1}{2}\rho V_1^2 + \gamma z_1 = p_2 + \frac{1}{2}\rho V_2^2 + \gamma z_2$$

![](3/30.png)

## Slide 31

### 1) Jatos livre

Uma vez que o fluxo sai como um jato livre, a pressão no ponto 2 é a pressão atmosférica

Pontos: **(1)** superfície livre; **(2)** centro do orifício de saída; **(3)** fundo do tanque; **(4)** borda do orifício; **(5)** no jato livre abaixo da saída.

Dimensões: $h$ (profundidade da superfície livre até a saída), $l$ (espessura do fundo), $d$ (diâmetro do orifício), $H$ (distância vertical da saída ao ponto 5).

$$p_1 + \frac{1}{2} \rho V_1^2 + \gamma z_1 = p_2 + \frac{1}{2} \rho V_2^2 + \gamma z_2$$

$$\gamma h = \frac{1}{2} \rho V_2^2 \Rightarrow V_2 = \sqrt{2gh}$$

![](3/31.png)

## Slide 33

**Sol:**

$$p_0 + \frac{\rho V_0^2}{2} + \rho g z_0 = p_1 + \frac{\rho V_1^2}{2} + \rho g z_1; \quad p_0 + \frac{\rho V_0^2}{2} + \rho g z_0 = p_2 + \frac{\rho V_2^2}{2} + \rho g z_2$$

$$V_1 = \sqrt{2g(h_2 - h_1)}; \quad V_2 = \sqrt{2gh_2}$$

$$V = \frac{L}{t}; \quad t = \frac{L}{\sqrt{2g(h_2 - h_1)}}; \quad t = \frac{L}{\sqrt{2gh_2}}$$

$$s = s_0 + V_0 t + \frac{a}{2} t^2$$

$$s_1 = h_1 - \frac{g}{2} \frac{L^2}{2g(h_2 - h_1)}; \quad s_2 = 0 - \frac{g}{2} \frac{L^2}{2gh_2}$$

$$h_1 - \frac{L^2}{4(h_2 - h_1)} = -\frac{L^2}{4h_2} \Rightarrow h_1 = \frac{L^2}{4} \left( \frac{1}{(h_2 - h_1)} - \frac{1}{h_2} \right)$$

$$L = 2 \sqrt{h_2(h_2 - h_1)}$$

![](3/33.png)

## Slide 34

### 2) Escoamentos confinados

* O fluido está fisicamente confinado, a pressão ou a velocidade em alguns pontos é desconhecida
* Usa-se a equação da continuidade (conservação de massa) para relacionar $V_1$ e $V_2$ na Eq. de Bernoulli

**Legenda do diagrama:**
* Caixa cinza sólida: Fluid parcel at $t=0$
* Caixa tracejada: Same fluid parcel at $t = \delta t$

Seção **(1):** comprimento do parcela $V_1 \delta t$; Volume $= V_1 \delta t A_1$

Seção **(2):** comprimento do parcela $V_2 \delta t$; Volume $= V_2 \delta t A_2$

$$\dot{m} = \rho \dot{Q} = \rho A V \implies \rho_1 A_1 V_1 = \rho_2 A_2 V_2$$

ou para fluidos incompressíveis $\implies A_1 V_1 = A_2 V_2$

![](3/34.png)

## Slide 37

**Cavitação:** Ocorre quando a pressão do fluido é reduzida para a pressão de saturação (ocorre ebulição)

* Quando o fluido se move em uma curva:
    * Pressão reduzida devido a aceleração centrífuga

A equação do movimento ao longo da direção normal é:

$$p + \gamma z + \int \frac{\rho V^2}{\mathcal{R}} \, dn = C$$

* Quando a área do escoamento diminui:
    * Aumento da velocidade e redução da pressão

![](3/37.png)

## Slide 39

### Medição de vazão e velocidade

As eqs. de Bernoulli e da continuidade podem ser aplicadas para medição de vazão e de velocidade

Equipamentos com restrições locais:

Orifício, bocal (nozzle), venturi

$$P_1 + \frac{1}{2} \rho V_1^2 = P_2 + \frac{1}{2} \rho V_2^2,$$

$$Q = A_1 V_1 = A_2 V_2,$$

Então

$$Q = A_2 \sqrt{\frac{2(P_1 - P_2)}{\rho[1 - (A_2 / A_1)^2]}}$$

![](3/39.png)

## Slide 41

**3.21** A Fig. P3.21 mostra um dispositivo que pode ser utilizado para medir a vazão de um jato descarregado de um tubo num ambiente aberto. Observe que a gravidade provoca uma curvatura no jato descarregado do tubo (veja os $\odot$'s 3.5 e 4.3) e que a deflexão da superfície do jato pode ser avaliada a partir dos comprimentos $L$ e $x$ indicados na figura. Mostre que a vazão em volume do escoamento é dada por $Q = \pi D^2 L g^{1/2} / (2^{5/2} x^{1/2})$, onde $D$ é o diâmetro interno do tubo.

**Sol:**

$$\dot{Q} = VA \Rightarrow V = \frac{L}{t}; \quad A = \frac{\pi D^2}{4}$$

$$Q = \frac{L}{t} \frac{\pi D^2}{4}$$

$$x = x_0 + V_0 t + \frac{gt^2}{2}$$

$$x = \frac{gt^2}{2} \Rightarrow t = \sqrt{\frac{2x}{g}}$$

$$Q = L \pi D^2 \sqrt{\frac{g}{2^5 x}}$$

![](3/41.png)

## Slide 43

**Figura 3.6 — Tubo de Pitot estático**

Pontos: **(1)** pressão estática na parede lateral; **(2)** estagnação na ponta; **(3)** saída da linha de estagnação; **(4)** saída da linha estática.

Escoamento com velocidade $V$ e densidade $\rho$.

$$p_3 = p + \frac{1}{2} \rho V^2$$

$$p_4 = p_1 = p$$

$$p_3 - p_4 = \frac{1}{2} \rho V^2$$

$$V = \sqrt{\frac{2(p_3 - p_4)}{\rho}}$$

![](3/43.png)

## Slide 44

**3.43** Uma mangueira de plástico, com 10 m de comprimento e diâmetro interno igual a 15 mm, é utilizada para drenar uma piscina do modo mostrado na Fig. P3.43. Qual é a vazão em volume do escoamento na mangueira? Admita que os efeitos viscosos são desprezíveis.

Fig. P3.43 — Profundidade da água na piscina $0{,}2$ m; diferença de cota entre o fundo da piscina e a saída da mangueira $0{,}23$ m.

$$p_0 + \frac{\rho V_0^2}{2} + \rho g z_0 = p_1 + \frac{\rho V_1^2}{2} + \rho g z_1;$$

$$V_1 = \sqrt{2g(z_0 - z_1)};$$

$$\dot{Q} = V_1 A$$

![](3/44.png)

## Slide 46

$$P_0 + \frac{\rho V_0^2}{2} + \rho g z_0 = P_1 + \frac{\rho V_1^2}{2} + \rho g z_1 = P_2 + \frac{\rho V_2^2}{2} + \rho g z_2$$

$$V_0 = 0; \quad V_1 A_1 = V_2 A_2 \Rightarrow V_1 D_1^2 = V_2 D_2^2$$

$$z_1 = z_2 = 0; \quad z_0 = h$$

$$P_2 = P_0$$

$$P_0 + \rho g h = P_1 + \frac{\rho V_1^2}{2} = P_0 + \frac{\rho V_2^2}{2}$$

$$V_2 = \sqrt{2gh} \Rightarrow V_1 = \frac{D_2^2}{D_1^2} \sqrt{2gh}$$

$$P_0 + \rho g h = P_1 + \rho \frac{D_2^4}{D_1^4} g h \Rightarrow h = \frac{P_0 - P_1}{\gamma} \left( \frac{D_1^4}{D_2^4 - D_1^4} \right)$$

$$P_1 + \frac{\rho V_1^2}{2} = \text{Constante.}$$

Para evitar cavitação, aumentar $P_1$, e consequentemente, reduzir $V_1$

$V_1 D_1^2 = V_2 D_2^2$ e para $h$ fixo, diminuir $D_2$ ou aumentar $D_1$

![](3/46.png)

## Slide 48

$$P_1 = P_x$$

$$P_x = \rho g h_1 + P_y$$

$$P_y = \rho_w g \sin \theta \, L + P_z$$

$$P_z = \rho g h_2 + P_2$$

$$P_1 = \rho g h_1 + \rho_w g \sin \theta \, L + \rho g h_2 + P_2$$

$$P_1 + \frac{\rho V_1^2}{2} = P_2 + \frac{\rho V_2^2}{2} + \rho g (h_1 + \sin \theta \, L + h_2)$$

$$\rho g h_1 + \rho_w g \sin \theta \, L + \rho g h_2 + P_2 + \frac{\rho V_1^2}{2} = P_2 + \frac{\rho V_2^2}{2} + \rho g (h_1 + \sin \theta \, L + h_2)$$

$$\left( \frac{\rho_w}{\rho} - 1 \right) 2 g \sin \theta \, L = V_2^2 - V_1^2$$

$$\frac{16 \dot{Q}^2}{\pi^2} \left( \frac{1}{D_2^4} - \frac{1}{D_1^4} \right) = \left( \frac{\rho_w}{\rho} - 1 \right) 2 g \sin \theta \, L$$

$$\dot{Q} = \frac{D_2^2 D_1^2}{2} \sqrt{\left( \frac{\rho_w}{\rho} - 1 \right) \frac{\pi^2 g \sin \theta \, L}{2(D_1^4 - D_2^4)}}$$

![](3/48.png)

## Slide 49

**3.76** A Fig. P3.76 mostra um antigo dispositivo utilizado para medir o tempo. O formato do vaso axissimétrico é tal que o nível da água cai com velocidade constante. Determine o formato do vaso, $R(z)$, sabendo que a velocidade da superfície livre da água e o diâmetro do orifício posicionado no fundo do dispositivo são iguais a $0{,}10$ m/h e $5{,}0$ mm. Admita que o dispositivo opera 12 horas sem recarga.

**Sol:**

$$R^2 u_1 = \frac{d^2}{4} u_2$$

$$\frac{u_1^2}{2} + gz = \frac{u_2^2}{2}$$

$$u_2 = \sqrt{2gz + u_1^2}$$

$$R^2 u_1 = \frac{d^2}{4} \sqrt{2gz + u_1^2}$$

$$\frac{4u_1}{d^2} R^2 = \sqrt{2gz + u_1^2}$$

$$\frac{16u_1^2}{d^4} R^4 = 2gz + u_1^2$$

$$R^4 = \frac{d^4 (2gz + u_1^2)}{16u_1^2}$$

$$R = \frac{d}{2} \sqrt[4]{\frac{2gz}{u_1^2} + 1}$$

![](3/49.png)

## Slide 50

**3.88** A Fig. P3.88 mostra o esboço de um veículo suportado por um colchão de ar. O ar escapa através da fresta formada pela saia do veículo e pela superfície da água (ou chão). Admita que a massa do veículo é igual a 4530 kg e que seu formato é retangular (9,1 m $\times$ 19,8 m). O volume da câmara é grande o suficiente para que a energia cinética do ar na câmara seja desprezível. Determine a vazão em volume, $Q$, necessária para suportar o veículo sabendo que a espessura da fresta é igual a 76 mm. Se a espessura da fresta for reduzida para 51 mm, qual é a vazão necessária para suportar o veículo? Se a massa do veículo for reduzida para 2265 kg e a espessura da fresta for mantida igual a 76 mm, qual é a vazão de ar necessária para suportar o veículo?

**Sol:**

$$\sum F_{up} = \sum F_{down}$$

$$P_i A_i = P_e A_e + mg; \quad A_i \approx A_e = a \times b$$

$$P_i = P_e + \frac{mg}{a \times b}$$

$$P_i + \frac{\rho V_i^2}{2} + \rho g z_i = P_e + \frac{\rho V_e^2}{2} + \rho g z_e$$

$$z_i = z_e; \quad V_i \approx 0$$

$$P_i = P_e + \frac{\rho V_e^2}{2}$$

$$\frac{\rho V_e^2}{2} = \frac{mg}{a \times b}; \quad \dot{Q} = V_e A_f = 2V_e(a+b)\varepsilon$$

$$\left( \frac{\dot{Q}}{2(a+b)\varepsilon} \right)^2 = \frac{2mg}{\rho(a \times b)}$$

$$\dot{Q} = 2(a+b)\varepsilon \sqrt{\frac{2mg}{\rho(a \times b)}}$$

![](3/50.png)

## Slide 51

E qual a mínima potência do ventilador para que isso aconteça? Utiliza-se a Eq. de Bernoulli extendida.

$$\frac{p_e}{\gamma} + \frac{V_e^2}{2g} + z_e + h_{eixo} = \frac{p_i}{\gamma} + \frac{V_i^2}{2g} + z_i + h_L$$

$$\frac{p_e}{\gamma} + h_{eixo} = \frac{p_i}{\gamma}$$

$$h_{eixo} = \frac{p_i - p_e}{\gamma}$$

$$h_{eixo} = \frac{\dot{W}}{\dot{m}g} = \frac{\dot{W}}{\dot{Q}\gamma}$$

$$\dot{W} = \dot{Q}(p_i - p_e)$$

$$\dot{W} = \frac{(a+b)\varepsilon}{\rho^{\frac{1}{2}}} \left[ \frac{2mg}{(a \times b)} \right]^{\frac{3}{2}}$$

$$\dot{W} \equiv \frac{m \cdot m \cdot m^{\frac{3}{2}}}{kg^{\frac{1}{2}}} \cdot \frac{kg^{\frac{3}{2}}}{m^{\frac{3}{2}} s^3} = \frac{m \cdot m \cdot kg}{s^3} = \frac{N \cdot m}{s} = \frac{J}{s} = W$$

![](3/51.png)

## Slide 52

Água escoa através de uma curva, com uma vazão mássica de 1000 lbm/s. A pressão a montante da curva é 90 psi, e a queda de pressão nesta curva é 5 psi. Os diâmetros de entrada e saída da curva são 12 e 24 pol. Determine a perda de energia por unidade de massa que ocorre neste escoamento. Assuma que o escoamento ocorre na horizontal.

Volume de controle: entrada com diâmetro $12$ in.; saída com diâmetro $24$ in.; $\rho_{\text{Água}} = 1{,}94$ slug/ft$^3$.

$$\frac{p_s}{\rho} + \frac{V_s^2}{2} + gz_s = \frac{p_e}{\rho} + \frac{V_e^2}{2} + gz_e + w_{\text{liq.eixo}} - \text{perda}$$

$$\text{perda} = \frac{p_e}{\rho} + \frac{V_e^2}{2} - \frac{p_s}{\rho} - \frac{V_s^2}{2}$$

$$\dot{m} = \rho A V \Rightarrow V = \frac{\dot{m}}{\rho A}$$

$$\text{perda} = \frac{p_e}{\rho} + \frac{1}{2}\left(\frac{4\dot{m}}{\rho \pi D_e^2}\right)^2 - \frac{p_s}{\rho} - \frac{1}{2}\left(\frac{4\dot{m}}{\rho \pi D_s^2}\right)^2$$

$$\text{perda} = \frac{1}{\rho}\left[(p_e - p_s) + \left(\frac{8}{\rho}\right)\left(\frac{\dot{m}}{\pi}\right)^2 \left(\frac{1}{D_e^4} - \frac{1}{D_s^4}\right)\right]$$

![](3/52.png)

## Slide 53

## Capítulo 8. Escoamento em tubulações

* Exemplos de componentes de uma tubulação

**Componentes ilustrados:** Inlet, Elbow, Pump, Tee, Valve, Pipe, Outlet.

![](3/53.png)

## Slide 54

### Escoamentos laminares e turbulentos

* Osborne Reynolds fez experimentos com vários escoamentos

**(a)** Tubo com entrada suave (*Smooth, well-rounded entrance*); injeção de corante (*Dye streak*) a partir de reservatório de corante (*Dye*); diâmetro interno $D$; $Q = VA$.

**(b)** Regimes de escoamento observados no corante:
* **Laminar** — linha reta e estável
* **Transitional** — oscilações
* **Turbulent** — dispersão caótica

![](3/54.png)

## Slide 55

O número de Reynolds,

$$\text{Re} = \frac{\rho V D}{\mu}$$

Para um escoamento em um tubo circular,

* Escoamento Laminar: $\text{Re} < 2100$
* Escoamento de Transição: $2100 < \text{Re} < 4000$
* Escoamento turbulento: $\text{Re} > 4000$

![](3/55.png)

## Slide 56

### Região de entrada e escoamento desenvolvido

**Entrance region flow** (entre os pontos (1) e (2), comprimento $l_e$):
* Perfil de velocidade uniforme na entrada (ponto **(1)**)
* Crescimento da **Boundary layer**
* Núcleo central **Inviscid core**

**Fully developed flow** (a partir do ponto **(2)** até **(3)**):
* Perfil parabólico plenamente desenvolvido
* Diâmetro $D$; coordenadas $r$ e $x$

Após curva de 180°:
* Ponto **(4)** — perfil distorcido
* **Developing flow** entre (4) e (5), comprimento $x_5 - x_4$
* **Fully developed flow** entre (5) e (6), comprimento $x_6 - x_5$
* Ponto **(6)** — perfil simétrico restabelecido

![](3/56.png)

## Slide 57

O comprimento típico da região de entrada em tubos circulares é

$$\frac{l_e}{D} = 0{,}06 \text{ Re} \quad \text{para escoamento laminar}$$

e

$$\frac{l_e}{D} = 4{,}4 \text{ Re}^{1/6} \quad \text{para escoamento turbulento}$$

![](3/57.png)

## Slide 58

### Escoamento laminar plenamente desenvolvido

* De acordo com a 2ª Lei de Newton

$$(p_1)\pi r^2 - (p_1 - \Delta p)\pi r^2 - (\tau)2\pi r \ell = 0$$

$$\frac{\Delta p}{\ell} = \frac{2\tau}{r}$$

**FIGURE 8.7** — Motion of a cylindrical fluid element within a pipe.

Perfil de velocidade $V = u(r)\hat{i}$; elemento cilíndrico de raio $r$ e comprimento $\ell$; *Fluid element at time $t$* (posição **(1)**); *Element at time $t + \delta t$* (posição **(2)**); diâmetro $D$; eixo $x$.

**FIGURE 8.8** — Free-body diagram of a cylinder of fluid.

Forças: $p_1 \pi r^2$ (face esquerda); $(p_1 - \Delta p) \pi r^2$ (face direita); $\tau 2\pi r \ell$ (superfície lateral).

![](3/58.png)

## Slide 59

### Escoamento laminar plenamente desenvolvido

* De acordo com a 2ª Lei de Newton

$$(p_1)\pi r^2 - (p_1 - \Delta p)\pi r^2 - (\tau)2\pi r \ell = 0$$

$$\frac{\Delta p}{\ell} = \frac{2\tau}{r}$$

**FIGURE 8.7** — Motion of a cylindrical fluid element within a pipe.

Perfil de velocidade $V = u(r)\hat{i}$; elemento cilíndrico de raio $r$ e comprimento $\ell$; *Fluid element at time $t$* (posição **(1)**); *Element at time $t + \delta t$* (posição **(2)**); diâmetro $D$; eixo $x$.

**FIGURE 8.8** — Free-body diagram of a cylinder of fluid.

Forças: $p_1 \pi r^2$ (face esquerda); $(p_1 - \Delta p) \pi r^2$ (face direita); $\tau 2\pi r \ell$ (superfície lateral).

![](3/59.png)

## Slide 60

### Escoamento laminar plenamente desenvolvido

* E sabendo-se que $\tau = 0$ no centro e igual a $\tau = \tau_W$ na parede, tem-se

$$\tau = \frac{2\tau_W r}{D}$$

Desta forma

$$\frac{\Delta p}{l} = \frac{2\tau}{r} \Rightarrow \frac{\Delta p}{l} = \frac{2\left(\frac{2\tau_W r}{D}\right)}{r} \Rightarrow \Delta p = \frac{4l\tau_W}{D}$$

Para fluidos Newtonianos

$$\tau = -\mu \frac{du}{dr}$$

$$\frac{du}{dr} = -\left(\frac{\Delta p}{2\mu l}\right)r \Rightarrow u = -\left(\frac{\Delta p}{4\mu l}\right)r^2 + C_1$$

![](3/60.png)

## Slide 61

### Escoamento laminar plenamente desenvolvido

* E sabendo-se que $\tau = 0$ no centro e igual a $\tau = \tau_W$ na parede, tem-se

$$\tau = \frac{2\tau_W r}{D}$$

Desta forma

$$\frac{\Delta p}{l} = \frac{2\tau}{r} \Rightarrow \frac{\Delta p}{l} = \frac{2\left(\frac{2\tau_W r}{D}\right)}{r} \Rightarrow \Delta p = \frac{4l\tau_W}{D}$$

Para fluidos Newtonianos

$$\tau = -\mu \frac{du}{dr}$$

$$\frac{du}{dr} = -\left(\frac{\Delta p}{2\mu l}\right)r \Rightarrow u = -\left(\frac{\Delta p}{4\mu l}\right)r^2 + C_1$$

![](3/61.png)

## Slide 62

* A vazão $Q$ é obtida por integração do perfil de velocidade ao longo da seção transversal do tubo
* Escoamento de Hagen-Poiseuille (laminar)

$$u = \left( \frac{\Delta p D^2}{16 \mu l} \right) \left[ 1 - \left( \frac{2r}{D} \right)^2 \right] = V_C \left[ 1 - \left( \frac{2r}{D} \right)^2 \right]$$

$$Q = \int u \, dA = \frac{\pi R^2 V_C}{2} = \frac{\pi \Delta p D^4}{128 \mu l}$$

$$\bar{V} = \frac{Q}{A} = \frac{V_C}{2} = \frac{\Delta p D^2}{32 \mu l}$$

![](3/62.png)

## Slide 63

Tubulação inclinada com ângulo $\theta$; cilindro de fluido de comprimento $l$ e raio $r$.

Forças: $(p + \Delta p)\pi r^2$ (montante); $p\pi r^2$ (jusante); $\tau 2\pi r l$ (cisalhamento); $W\sin\theta = \gamma \pi r^2 l \sin\theta$ (peso).

$$\bar{V} = \frac{(\Delta p - \gamma l \sin \theta)R^2}{8\mu l}$$

$$Q = \frac{\pi (\Delta p - \gamma l \sin \theta)R^4}{8\mu l}$$

![](3/63.png)

## Slide 64

### Escoamento turbulento plenamente desenvolvido

* Escoamento complexo e o menos compreendido na área de mecânica dos fluidos
* Escoamento importante pois é o mais comum

* Transição: $2100 < \text{Re} < 4000$
* Turbulento: $\text{Re} > 4000$

Velocidade instantânea $u(t)$ e valor médio temporal $\bar{u}$:

$$\bar{u} = \frac{1}{T} \int_{t_0}^{t_0+T} u(x, y, z, t) \, dt$$

![](3/64.png)

## Slide 65

### Perfil de velocidade no escoamento turbulento

* Não há nenhuma equação que descreva exatamente qual é o perfil de velocidade
* Perfil turbulento é mais "uniforme" que o perfil laminar
* Equação empírica para o perfil de velocidade

$$\frac{\bar{u}}{V_c} = \left( 1 - \frac{r}{R} \right)^{1/n}$$

O valor de $n$ depende de $\text{Re}$

$R = D/2$; $\delta_s$ — subcamada viscosa; rugosidade $\epsilon$ (parede rugosa vs. lisa).

![](3/65.png)

## Slide 66

### Perfis de velocidade em escoamento laminar e turbulento

$$\frac{\bar{u}}{V_c} = \left( 1 - \frac{r}{R} \right)^{1/n}$$

$$Q = A \bar{V} = \int_{r=0}^{r=R} V_c \left( 1 - \frac{r}{R} \right)^{1/n} 2\pi r \, dr$$

$$Q = 2\pi R^2 V_c \frac{n^2}{(n+1)(2n+1)} = A_R V_c \frac{2n^2}{(n+1)(2n+1)}$$

$$\bar{V} = V_c \frac{2n^2}{(n+1)(2n+1)}$$

$p/n = 6 \Rightarrow Q = 0{,}79 A_R V_c$

$p/n = 10 \Rightarrow Q = 0{,}87 A_R V_c$

![](3/66.png)

## Slide 67

### Perda de carga em uma tubulação

* Experimentalmente, pode-se verificar que a perda de pressão em uma tubulação é função das seguintes variáveis

$$\Delta p = f(V, D, l, \varepsilon, \mu, \rho)$$

* Também é possível confirmar que a função tem a seguinte forma (**para escoamento horizontal**)

$$\Delta p = f_{atrito} \frac{l}{D} \frac{\rho V^2}{2}$$

$$f_{atrito} = \text{Fator de atrito}$$

![](3/67.png)

## Slide 68

* Para escoamento laminar

$$f_{atrito} = \frac{64}{\text{Re}}$$

* Para $\text{Re}$ grandes

$$f_{atrito} = f\left(\frac{\varepsilon}{D}\right)$$

* Para valores moderados de $\text{Re}$

$$f_{atrito} = f\left(\text{Re}, \frac{\varepsilon}{D}\right)$$

![](3/68.png)

## Slide 69

### Equação de Colebrook

$$\frac{1}{\sqrt{f_{atrito}}} = -2{,}0 \log \left( \frac{\varepsilon / D}{3{,}7} + \frac{2{,}51}{\text{Re} \sqrt{f_{atrito}}} \right)$$

* Válida para toda região não laminar
* Implícita ---> solução por iteração
* Representada graficamente pelo diagrama de Moody

![](3/69.png)

## Slide 70

### Diagrama de Moody

$$\text{Re} = \frac{\rho V D}{\mu}$$

**Rugosidade equivalente, $\varepsilon$ (mm):**

| Tubo | $\varepsilon$ (mm) |
|------|-------------------|
| Aço rebitado | 0,9 - 9,0 |
| Concreto | 0,3 - 3,0 |
| Madeira aparelhada | 0,18 - 0,9 |
| Ferro fundido | 0,26 |
| Ferro galvanizado | 0,15 |
| Aço comercial ou estrudado | 0,045 |
| Tubo estirado | 0,0015 |
| Plástico, vidro | 0,0 (liso) |

Regiões: laminar ($\text{Re} < 2000$); transição; turbulento; *smooth*; *wholly turbulent*.

![](3/70.png)

## Slide 71

### Como usar o $f_{atrito}$?

* **A equação de energia mecânica**

$$\frac{p_1}{\gamma} + \frac{V_1^2}{2g} + z_1 + h_{eixo} = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L$$

* **Para $V$ constante e mesma cota $z$:** $\Delta p = \gamma h_L$

$$\Delta p = f_{atrito} \frac{l}{D} \frac{\rho V^2}{2}$$

$$h_L = f_{atrito} \frac{l}{D} \frac{V^2}{2g}$$

* **Quando se tem variação da cota, acha-se a perda de pressão por**

$$p_1 - p_2 = \gamma(z_2 - z_1) + \gamma h_L$$

![](3/71.png)

## Slide 72

### Perdas de carga

* As perdas devido ao atrito no tubo são as maiores
* Mas outros componentes da tubulação, tais como (válvulas, curvas, bifurcações, etc) também causam perdas de carga
* Coeficiente de perda,

$$K_L = \frac{h_L}{(V^2 / 2g)} = \frac{\Delta p}{\frac{1}{2} \rho V^2}$$

$$\Delta p = K_L \frac{1}{2} \rho V^2 \quad \text{ou} \quad h_L = K_L \frac{V^2}{2g}$$

![](3/72.png)

## Slide 73

### Alguns valores para o coeficiente de perda

* (a) Entrada reentrante: $K_L^{(a)} = 0{,}8$
* (b) Entrada de aresta viva: $K_L^{(b)} = 0{,}5$
* (c) Entrada ligeiramente arredondada: $K_L = 0{,}2$
* (d) Entrada bem arredondada: $K_L = 0{,}04$

![](3/73.png)

## Slide 74

### Coeficiente de perda para uma contração súbita

$$h_L = K_L \frac{V_2^2}{2g}$$

$K_L$ em função de $A_2/A_1$: $K_L \approx 0{,}5$ quando $A_2/A_1 \to 0$; $K_L = 0$ quando $A_2/A_1 = 1{,}0$.

![](3/74.png)

## Slide 75

### Coeficiente de perda para uma expansão súbita

$$h_L = K_L \frac{V_1^2}{2g}$$

$K_L$ em função de $A_1/A_2$: $K_L \approx 1{,}0$ quando $A_1/A_2 \to 0$; $K_L = 0$ quando $A_1/A_2 = 1{,}0$.

![](3/75.png)

## Slide 76

### Tubos não-circulares

Defini-se o diâmetro hidráulico

$$D_h = \frac{4A}{P}$$

$A$ — área da seção transversal; $P$ — perímetro molhado; $V = u(y,z)$.

![](3/76.png)

## Slide 77

* E utiliza-se o diâmetro hidráulico para se calcular a perda de carga e $\text{Re}$

$$h_L = f_{atrito} \frac{l}{D_h} \frac{V^2}{2g}$$

$$\text{Re}_h = \frac{\rho V D_h}{\mu}$$

* E a rugosidade relativa $\varepsilon / D_h$.

![](3/77.png)

## Slide 78

### Equivalência entre coeficiente de perda e comprimento de tubulação que fornece a mesma perda de carga

$$h_L = f_{atrito} \frac{l}{D} \frac{V^2}{2g}$$

$$h_L = K_L \frac{V^2}{2g}$$

$$f_{atrito} \frac{l}{D} \equiv K_L$$

![](3/78.png)

## Slide 79

### Exemplos de tipo de problema com tubulações

a) Tipo 1: $Q$ ou $V$ é conhecido $\rightarrow$ achar $\Delta P$

b) Tipo 2: $\Delta P$ é conhecido $\rightarrow$ achar $Q$

c) Tipo 3: $h_L$ e $Q$ é conhecido $\rightarrow$ achar $A$

![](3/79.png)

## Slide 81

$$\frac{p_1}{\gamma} + \frac{V_1^2}{2g} + z_1 + h_{eixo} = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L \Rightarrow h_{eixo} = h_L$$

$$\frac{\dot{W}}{\dot{Q}\gamma} = \left( f \frac{L}{D} + \sum K_L \right) \frac{V^2}{2g} \Rightarrow \frac{\dot{W}}{\dot{Q}\rho} = \left( f \frac{L}{D} + \sum K_L \right) \frac{8\dot{Q}^2}{\pi^2 D^4}$$

$$\dot{Q} = \sqrt[3]{\frac{\dot{W} \pi^2 D^4}{8 \left( f \frac{L}{D} + \sum K_L \right) \rho}}; \quad \text{Re} = \frac{\rho V D}{\mu} = \frac{4\dot{Q}}{\pi D \nu}$$

$$\frac{\varepsilon}{D} = 0{,}01, \text{ assumindo } \text{Re} > 1 \times 10^5, f = 0{,}038$$

$$\dot{Q} = \sqrt[3]{\frac{272 \pi^2 (31 \times 10^{-3})^4}{8 \left( 0{,}038 \frac{61}{31 \times 10^{-3}} + 27{,}3 \right) 998}} = \sqrt[3]{\frac{3{,}105 \times 10^{-7}}{(0{,}038 \times 1967{,}7 + 27{,}3)}} = 1{,}45 \times 10^{-3} \text{ m}^3/\text{s}$$

$$\text{Re} = \frac{4 \times 1{,}45 \times 10^{-3}}{\pi \times 31 \times 10^{-3} \times 1{,}01 \times 10^{-6}} = 5{,}9 \times 10^4 \text{ e } f \approx 0{,}038, \text{ então } \dot{Q} \approx 1{,}45 \times 10^{-3} \text{ m}^3/\text{s}$$

![](3/81.png)

## Slide 82

Diagrama de Moody — exemplo: $\text{Re} = 10^5$, $\varepsilon/D \approx 0{,}01 \Rightarrow f \approx 0{,}038$.

![](3/82.png)

## Formulário — Parte 3

### Fórmulas dos slides (organizadas por tópico)

#### Equações diferenciais do movimento (Cauchy e Euler)

$$\sigma_n = \lim_{\delta A \to 0} \frac{\delta F_n}{\delta A}; \quad \tau_i = \lim_{\delta A \to 0} \frac{\delta F_i}{\delta A}$$

$$\rho g_x + \frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \tau_{yx}}{\partial y} + \frac{\partial \tau_{zx}}{\partial z} = \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right)$$

(análogas para $y$ e $z$)

$$\rho g_x - \frac{\partial p}{\partial x} = \rho \left( \frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} + w \frac{\partial u}{\partial z} \right)$$

(análogas para $y$ e $z$ — equações de Euler)

#### Bernoulli (ao longo de linha de corrente)

$$-\gamma \sin \theta - \frac{\partial p}{\partial s} = \rho V \frac{\partial V}{\partial s}$$

$$dp + \frac{1}{2} \rho \, d(V^2) + \gamma \, dz = 0$$

$$p + \frac{1}{2} \rho V^2 + \gamma z = C$$

$$\frac{p}{\gamma} + \frac{V^2}{2g} + z = C$$

$$p_1 + \frac{1}{2}\rho V_1^2 + \gamma z_1 = p_2 + \frac{1}{2}\rho V_2^2 + \gamma z_2$$

$$p + \frac{1}{2} \rho V^2 + \gamma z = p_T = C$$

#### Equação do movimento normal à linha de corrente

$$-\gamma \frac{dz}{dn} - \frac{dp}{dn} = \frac{\rho V^2}{\mathcal{R}}$$

$$p + \gamma z + \int \frac{\rho V^2}{\mathcal{R}} \, dn = C$$

#### Pressão estática, dinâmica e de estagnação

$$p_1 = p_0 + \gamma h$$

$$p_2 = p_1 + \frac{1}{2} \rho V_1^2$$

$$p_3 = p + \frac{1}{2} \rho V^2; \quad p_4 = p$$

$$p_3 - p_4 = \frac{1}{2} \rho V^2; \quad V = \sqrt{\frac{2(p_3 - p_4)}{\rho}}$$

#### Continuidade e medição de vazão

$$A_1 V_1 = A_2 V_2$$

$$Q = A_2 \sqrt{\frac{2(P_1 - P_2)}{\rho[1 - (A_2/A_1)^2]}}$$

$$V_2 = \sqrt{2gh} \quad \text{(jato livre)}$$

$$\dot{Q} = \pi D_0^2 \sqrt{\frac{gh}{8} \left(1 - \frac{\rho_m}{\rho}\right)} \quad \text{(Pitot + manômetro)}$$

#### Restrições de Bernoulli

$$Ma = V/c; \quad c = \sqrt{kRT}; \quad Ma < 0{,}3$$

$$a_s = V \frac{\partial V}{\partial s} \quad \text{(estacionário)}$$

$$a_s = V \frac{\partial V}{\partial s} + \frac{\partial V}{\partial t} \quad \text{(transiente)}$$

#### Reynolds e regiões de escoamento

$$\text{Re} = \frac{\rho V D}{\mu}$$

Laminar: $\text{Re} < 2100$; Transição: $2100 < \text{Re} < 4000$; Turbulento: $\text{Re} > 4000$

$$\frac{l_e}{D} = 0{,}06 \text{ Re} \quad \text{(laminar)}$$

$$\frac{l_e}{D} = 4{,}4 \text{ Re}^{1/6} \quad \text{(turbulento)}$$

#### Escoamento laminar (Hagen-Poiseuille)

$$\frac{\Delta p}{l} = \frac{2\tau}{r}; \quad \tau = \frac{2\tau_W r}{D}$$

$$\tau = -\mu \frac{du}{dr}$$

$$u = \left( \frac{\Delta p D^2}{16 \mu l} \right) \left[ 1 - \left( \frac{2r}{D} \right)^2 \right]$$

$$Q = \frac{\pi \Delta p D^4}{128 \mu l}; \quad \bar{V} = \frac{\Delta p D^2}{32 \mu l}$$

$$\bar{V} = \frac{(\Delta p - \gamma l \sin \theta)R^2}{8\mu l}$$

$$Q = \frac{\pi (\Delta p - \gamma l \sin \theta)R^4}{8\mu l}$$

#### Escoamento turbulento — perfil de potência

$$\bar{u} = \frac{1}{T} \int_{t_0}^{t_0+T} u \, dt$$

$$\frac{\bar{u}}{V_c} = \left( 1 - \frac{r}{R} \right)^{1/n}$$

$$\bar{V} = V_c \frac{2n^2}{(n+1)(2n+1)}$$

#### Darcy-Weisbach e fator de atrito

$$\Delta p = f_{atrito} \frac{l}{D} \frac{\rho V^2}{2}$$

$$h_L = f_{atrito} \frac{l}{D} \frac{V^2}{2g}$$

$$f_{atrito} = \frac{64}{\text{Re}} \quad \text{(laminar)}$$

$$\frac{1}{\sqrt{f_{atrito}}} = -2{,}0 \log \left( \frac{\varepsilon/D}{3{,}7} + \frac{2{,}51}{\text{Re} \sqrt{f_{atrito}}} \right) \quad \text{(Colebrook)}$$

#### Bernoulli estendida e perdas localizadas

$$\frac{p_1}{\gamma} + \frac{V_1^2}{2g} + z_1 + h_{eixo} = \frac{p_2}{\gamma} + \frac{V_2^2}{2g} + z_2 + h_L$$

$$p_1 - p_2 = \gamma(z_2 - z_1) + \gamma h_L$$

$$K_L = \frac{h_L}{V^2/(2g)} = \frac{\Delta p}{\frac{1}{2}\rho V^2}$$

$$h_L = K_L \frac{V^2}{2g}; \quad \Delta p = K_L \frac{1}{2} \rho V^2$$

$$f_{atrito} \frac{l}{D} \equiv K_L$$

#### Tubos não circulares

$$D_h = \frac{4A}{P}$$

$$h_L = f_{atrito} \frac{l}{D_h} \frac{V^2}{2g}; \quad \text{Re}_h = \frac{\rho V D_h}{\mu}$$

#### Circuitos com bomba

$$\frac{\dot{W}}{\dot{Q}\rho} = \left( f \frac{L}{D} + \sum K_L \right) \frac{8\dot{Q}^2}{\pi^2 D^4}$$

$$\dot{Q} = \sqrt[3]{\frac{\dot{W} \pi^2 D^4}{8 \left( f \frac{L}{D} + \sum K_L \right) \rho}}$$

$$\dot{W} = \dot{Q}(p_i - p_e)$$
