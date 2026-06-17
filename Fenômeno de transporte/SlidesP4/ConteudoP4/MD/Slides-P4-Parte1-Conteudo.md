# Introdução e conceitos

## Slide 1

* Definição de fluido, formas de análise e descrição
* Certas propriedades dos fluidos
    * Viscosidade
    * Módulo de compressibilidade (elasticidade volumétrica)
    * Velocidade do som
    * Tensão superficial

![](1/1.png)

## Slide 2 — O que é um fluido?

* Uma substância que deforma continuamente quando submetida a uma tensão de cisalhamento (newtonianos fluem com qualquer magnitude da tensão de cisalhamento).

**Fig. 1.1** Diferença em comportamento de um sólido e um líquido devido à força de cisalhamento.

(a) Sólido ou fluido — (b) Sólido ou fluido — (c) Somente fluido — (d) Somente fluido

* Materiais como pastas, piche, etc, não estão incluídos na mecânica dos fluidos clássica (fluidos newtonianos) pois eles podem se comportar como sólido se a tensão de cisalhamento for pequena, e apenas começar a fluir se a tensão de cisalhamento ultrapassar um certo valor.

![](1/2.png)

## Slide 3 — Por que estudar mecânica dos fluidos?

A mecânica dos fluidos é a parte da mecânica aplicada que se dedica à análise do comportamento dos líquidos e gases tanto em equilíbrio quanto em movimento. Obviamente, o escopo da mecânica dos fluidos abrange um vasto conjunto de problemas. Por exemplo, estes podem variar do estudo do escoamento de sangue nos capilares (que apresentam diâmetro da ordem de poucos mícrons) até o escoamento de petróleo através de uma oleoduto (o do Alaska apresenta diâmetro igual a 1,2 m e comprimento aproximado de 1300 km). Os princípios da mecânica dos fluidos são necessários para explicar porque o vôo dos aviões com formato aerodinâmico e com superfícies lisas é mais eficiente e também porque a superfície das bolas de golfe deve ser rugosa. Muitas questões interessantes podem ser respondidas se utilizarmos modelos simples da mecânica dos fluidos. Por exemplo:

* Como um foguete gera empuxo no espaço exterior (na ausência de ar para empurrá-lo)?
* Por que você não escuta o ruído de um avião supersônico até que ele passe por cima de você?
* Por que um rio escoa com uma velocidade significativa apesar do declive da superfície ser pequeno (o desnível não é detectado com um nível comum)?
* Como as informações obtidas num modelo de avião podem ser utilizadas no projeto de um avião real?
* Por que a superfície externa do escoamento de água numa torneira as vezes parece ser lisa e em outras vezes parece ser rugosa?
* Qual é a economia de combustível que pode ser obtida melhorando-se o projeto aerodinâmico dos automóveis e caminhões?

![](1/3.png)

## Slide 4 — Formulação Diferencial vs Formulação Integral

* As leis básicas aplicadas ao estudo da mecânica dos fluidos podem ser formuladas em termos de sistemas ou de volumes de controle infinitesimais ou finitos.
* Sistema é uma entidade com quantidade de massa definida
* Volume de controle é uma região no espaço por onde a massa pode entrar, sair e permanecer.

![](1/4.png)

## Slide 5 — Formulação Diferencial vs Formulação Integral

Solução das equações diferenciais fornece uma maneira de determinar o comportamento detalhado do escoamento (ex. distribuição de pressão sobre a superfície).

Porém quando o interesse está no comportamento de um dispositivo como um todo, é mais apropriado empregar a formulação integral das leis básicas (ex. a sustentação total que uma asa produz).

![](1/5.png)

## Slide 6 — Propriedades dos fluidos

Na mecânica dos fluidos, assume-se que as características e propriedades dos fluidos (pressão, velocidade, etc) variam continuamente através do fluido (**hipótese do meio contínuo**).

Hipótese deixa de ser válida em gases rarefeitos (i.e. quando a trajetória média livre das moléculas torna-se da mesma ordem de grandeza da menor dimensão característica significativa do problema).

![](1/6.png)

## Slide 7 — Viscosidade

É uma propriedade que descreve a “fluidez” do fluido

Considere o seguinte experimento hipotético:

A placa inferior é rigida e a placa superior pode se mover livremente.

![](1/7.png)

## Slide 8

A velocidade do fluido (newtoniano) entre as placas varia linearmente,

$$u = \frac{Uy}{b}$$

$$\frac{du}{dy} = \frac{U}{b}$$

**Condição de não escorregamento: O fluido gruda na superfície do sólido**

![](1/8.png)

## Slide 9

Em um intervalo de tempo infinitesimal ($\delta t$), a linha imaginária vertical AB vai rotacionar num ângulo $\beta$

$$\tan \delta\beta \approx \delta\beta = \frac{\delta a}{b}$$

Como $\delta a = U \delta t$, obtém-se

$$\delta\beta = \frac{U \delta t}{b}$$

![](1/9.png)

## Slide 10

Definindo a taxa de deformação por cisalhamento ou

$$\gamma = \lim_{\delta t \to 0} \frac{\delta \beta}{\delta t}$$

$$\gamma = \frac{U}{b} = \frac{du}{dy}$$

Experimentalmente, observou-se que a tensão de cisalhamento é diretamente proporcional a taxa de deformação por cisalhamento

$$\tau \propto \gamma \quad \text{ou} \quad \tau \propto \frac{du}{dy} \quad \text{or} \quad \tau = \mu \cdot \frac{du}{dy}$$

$\mu$ é **viscosidade absoluta**, viscosidade dinâmica ou apenas viscosidade

**Dimensão:** $(F \cdot T \cdot L^{-2})$

**Unidades:** $\text{lbf} \cdot \text{s} \cdot \text{ft}^{-2}$, $\text{N} \cdot \text{s} \cdot \text{m}^{-2}$, $\text{dina} \cdot \text{s} \cdot \text{cm}^{-2}$ (poise)

![](1/10.png)

## Slide 11

Se a viscosidade for combinada com a massa específica, obtém-se a **viscosidade cinemática**

$$\nu = \frac{\mu}{\rho}$$

**Fluidos Newtonianos** são aqueles cuja tensão de cisalhamento varia linearmente com a taxa de deformação angular

![](1/11.png)

## Slide 12

![](1/12.png)

## Slide 13 — Módulo de compressibilidade / Módulo de elasticidade volumétrica

Quão compressível é um fluido?

Propriedade relacionada ao Módulo de Compressibilidade

$$E_v = -\frac{dp}{d\overline{V}/\overline{V}}$$

Onde $dp$ é a variação da pressão necessária para criar uma variação de volume relativa

Módulos de compressibilidade grandes indicam substâncias praticamente incompressíveis.

O que tem maior $E_v$: Água ou Ferro? Água ou Nitrogênio gasoso?

Sabendo se $E_v$ de uma substância, é possível ou não determinar a variação de volume quando esta substância muda de um ambiente a 100 kPa para outro a 1000 kPa? E de massa específica?

![](1/13.png)

## Slide 14 — Velocidade do som

Velocidade com que as pertubações se propagam no fluido

$$c = \sqrt{\frac{dp}{d\rho}} = \sqrt{\frac{E_v}{\rho}}$$

Para processos isentropicos (pequenas pertubações, transferência de calor negligível) em gases ideais

$$c = \sqrt{\frac{kp}{\rho}} = \sqrt{kRT}$$

![](1/14.png)

## Slide 15 — Tensão superficial ($\sigma$)

1. É a intensidade da atração molecular por unidade de comprimento ao longo da superfície do líquido
2. Varia com a temperatura (aumenta ou diminui?)
3. Dimensões: $FL^{-1}$ ; unidades: $lb \cdot ft^{-1}$ or $N \cdot m^{-1}$
4. Exemplos da atuação da tensão superficial:
    1. Capilaridade
    2. Inseto andando sobre a água
    3. Bolha de sabão

![](1/15.png)

## Slide 16 — Pressão dentro de uma gota de fluido

$$2\pi R\sigma = \Delta p \, \pi R^2$$

$$\Delta p = p_i - p_e = \frac{2\sigma}{R}$$

![](1/16.png)

## Slide 17 — Altura do menisco em um tubo capilar

**Figura 1.8** Efeito da ação capilar em tubos com diâmetro pequeno. (a) Elevação da coluna para um líquido que molha o tubo. (b) Diagrama de corpo livre para o cálculo da altura da coluna. (c) Depressão da coluna para um líquido que não molha a parede do tubo.

$$\gamma \pi R^2 h = 2 \pi R \sigma \cos \theta$$

Assim, a altura da coluna é dada pela relação

$$h = \frac{2 \sigma \cos \theta}{\gamma R}$$

![](1/17.png)

## Slide 18 — Campos de escoamento

**Maneira de representar os parâmetros dos fluidos em função de sua coordenada espacial**

### Campo de velocidade

Os parâmetros dependem das coordenadas espaciais (x,y,z, por exemplo) e do tempo (t).

$$\vec{V} = u \vec{i} + v \vec{j} + w \vec{k}$$

$$u = u(x, y, z, t)$$

E se a velocidade é descrita por um vetor posição,

$$\vec{V} = \frac{d \vec{r}}{dt}$$

![](1/18.png)

## Slide 19

![](1/19.png)

## Slide 20

Temos duas formas de descrever e analisar os escoamentos:

descrição Euleriana e descrição Lagrangiana

**Descrição Euleriana:**

Informação sobre o escoamento em um certo ponto do espaço.

Utiliza o conceito de *campo* de escoamento.

**Descrição Lagrangiana :**

Informação sobre como uma certa partícula se move. Descreve como as propriedades se alteram no espaço e no tempo.

![](1/20.png)

## Slide 21 — Formas de descrever um escoamento

Quando se deseja acompanhar o deslocamento dos elementos que compõem uma massa, pode-se utilizar o método de descrição lagrangiano.

Para se analisar o que ocorre num escoamento em certa região do espaço num determinado tempo, podo-se utilizar o método de descrição euleriano.

![](1/21.png)

## Slide 22 — Escoamentos em 1, 2 ou 3 dimensões

**Classificação de escoamentos**

1. **Escoamento tridimensional:** O vetor velocidade depende de três variáveis espaciais.
2. **Escoamento bidimensional:** O vetor velocidade depende de somente duas variáveis espaciais.
3. **Escoamento unidimensional:** O vetor velocidade depende só de uma variável espacial.

Se um ou mais desse componentes do vetor velocidade é relativamente pequeno em relação aos outros, o escoamento pode ser considerado como bidimensional ou unidimensional

![](1/22.png)

## Slide 23

**4.1.2 Escoamentos Unidimensionais, Bidimensionais e Tridimensionais**

Os escoamentos normalmente são fenômenos tridimensionais, transitórios e complexos, $\mathbf{V} = \mathbf{V}(x, y, z, t)$. Entretanto, em muitos casos, é normal utilizarmos hipóteses simplificadoras para que seja possível analisar o problema (sem sacrificar muito a precisão dos resultados da análise). Uma destas hipóteses é a de considerar o escoamento real como unidimensional ou bidimensional.

O campo de velocidade, na maioria dos casos, apresenta três componentes (por exemplo: $u$, $v$ e $w$) e, em muitas situações, os efeitos do caráter tridimensional do escoamento são importantes. Nestes casos é necessário analisar o escoamento tridimensionalmente pois se desprezarmos um dos componentes do vetor velocidade na análise do escoamento obteremos resultados que apresentam desvios significativos em relação àqueles encontrados no escoamento real.

O escoamento de ar em torno de uma asa de avião é um exemplo de escoamento tridimensional complexo. A Fig. 4.3 mostra o aspecto da estrutura tridimensional deste escoamento. Note que foi utilizada uma técnica de visualização de escoamentos para enfatizar as estruturas do escoamento ao longo de um modelo de asa de avião (Ex. 4.2 - Escoamento em torno de uma asa).

Existem muitas situações onde um dos componentes do vetor velocidade é pequeno em relação aos outros dois componentes. Nestas situações, pode ser razoável desprezar este componente do vetor velocidade e admitir que o escoamento é bidimensional, ou seja, $\mathbf{V} = u \hat{i} + v \hat{j}$ onde $u$ e $v$ são funções de $x$, $y$ e, possivelmente, do tempo.

*MUNSON B. R., YOUNG D. F., OKIISHI T. H.; Fundamentos da Mecânica dos Fluidos. Vol II. Ed. Edgard Blucher Ltda., 1997.*

**Escoamentos Uni, Bi e Tridimensionais**

Um escoamento é classificado como uni, bi ou tridimensional de acordo com o número de coordenadas espaciais necessárias para especificar seu campo de velocidade. A Eq. 2.5 indica que o campo de velocidade pode ser uma função de três coordenadas espaciais e do tempo. Tal campo de escoamento é denominado *tridimensional* (ele é também *transiente*), porque a velocidade em qualquer ponto no campo de escoamento depende das três coordenadas requeridas para se localizar o ponto no espaço.

**Fig. 2.2** Exemplos de escoamentos uni e bidimensionais.

*FOX AND MCDONALD, Introdução à Mecânica dos Fluidos. 6ª ed. LTC editora, 2006.*

![](1/23.png)

## Slide 24

Tipos de escoamento em relação ao que acontece no tempo: escoamentos estacionários e transientes

Escoamento estacionário: Velocidade e outras propriedades num certo ponto não variam com o tempo.

$$\frac{\partial \vec{V}}{\partial t} = 0$$

![](1/24.png)

## Slide 25

**Conceitos para ajudar na visualização e análise dos campos de escoamento**

Linhas de corrente, linhas de emissão e trajetória

**Linhas de corrente:**

* Importantes para indicar a direção instantânea de movimento do fluido no escoamento
* Linha contínua e tangente ao vetor velocidade no campo de escoamento
* Abordagem matemática

No escoamento bidimensional:

a inclinação da linha de corrente = tangente do ângulo que o vetor velocidade faz com o eixo $x$

$$\frac{dy}{dx} = \frac{v}{u}$$

![](1/25.png)

## Slide 26

**Linhas de emissão:** Linha composta de todas as partículas em um escoamento, que passaram através de um ponto comum.

**Trajetória:** Linha traçada por uma certa partícula enquanto ela escoa de um ponto à outro. **Descrição Lagrangiana.**

**Ambas são abordagens experimentais**

![](1/26.png)

## Slide 27

* No escoamento permanente, a velocidade em cada ponto do campo permanece constante com o tempo e, por conseguinte, as linhas de corrente não variam de um instante a outro.
* Isso implica que uma partícula localizada em uma determinada linha de corrente permanecerá sobre ela.
* Além disso, partículas consecutivas passando através de um ponto fixo do espaço estarão sobre a mesma linha de corrente e, subsequentemente, permanecerão nela.
* Então, em um escoamento permanente, trajetórias, linhas de emissão e linhas de corrente são idênticas no campo de escoamento.
* No entanto, em escoamentos transientes, elas podem ser diferentes....

![](1/27.png)

## Slide 28 — Diferenças e semelhanças entre linhas de corrente, linhas de emissão e trajetória

1. São as mesmas para escoamento estacionário
2. Podem não ser todas iguais para escoamentos transientes
3. Linhas de corrente e trajetória: linhas tangenta ao campo de velocidade
4. Linhas de emissão: diferentes partículas num mesmo instante
5. Trajetória: mesma partícula em diferentes instantes
6. Essas linhas indicam direção e velocidade, mas não a magnitude.
7. Linhas de corrente estacionarias não se cruzam:
    * Partícula de fluido não pode ter duas velocidades diferentes num mesmo ponto.
8. Linhas de emissão não podem se autocruzar ou cruzar outras linhas de emissão:
    * Duas partículas de fluido não podem estar presente na mesma posição e tempo.
9. Trajetórias podem se autocruzar ou cruzar outras trajetórias:
10. Linhas de corrente e linhas de emissão são como fotos do campo de escoamento, e trajetórias são uma descrição temporal do escoamento.

![](1/28.png)

## Slide 29 — Aplicação destes conceitos

1. Desenvolvimento de equações descrevendo mudanças ao longo da linha de corrente: Equação de Bernoulli.
2. Engenheiros e cientistas podem utilizar tintas na água ou fumaça no ar para ver linhas de emissão, e usar estas informações no desenvolvimento e projeto de estruturas ou objetos, para, por exemplo, reduzir (ou aumentar) a força de arrasto ou de sustentação.

![](1/29.png)

## Slide 32 — Campo de tensão

$$\sigma_n = \lim_{\delta A \to 0} \frac{\delta F_n}{\delta A}$$

$$\tau_1 = \lim_{\delta A \to 0} \frac{\delta F_1}{\delta A}$$

$$\tau_2 = \lim_{\delta A \to 0} \frac{\delta F_2}{\delta A}$$

![](1/32.png)

## Slide 33 — Campo de tensão

Primeira letra subscrita: eixo normal a superfície que a força age

Segunda letra subscrita: eixo paralelo a direção que a força age

![](1/33.png)

## Slide 34

A tensão em um ponto é especificada então pelas nove componentes

$$
\begin{bmatrix}
\sigma_{xx} & \tau_{xy} & \tau_{xz} \\
\tau_{yx} & \sigma_{yy} & \tau_{yz} \\
\tau_{zx} & \tau_{zy} & \sigma_{zz}
\end{bmatrix}
$$

![](1/34.png)

## Formulário — Parte 1

### Fórmulas dos slides (organizadas por tópico)

#### Viscosidade (escoamento entre placas paralelas)

$$u = \frac{Uy}{b}$$

$$\frac{du}{dy} = \frac{U}{b}$$

$$\tan \delta\beta \approx \delta\beta = \frac{\delta a}{b}$$

$$\delta\beta = \frac{U \delta t}{b}$$

$$\gamma = \lim_{\delta t \to 0} \frac{\delta \beta}{\delta t} = \frac{U}{b} = \frac{du}{dy}$$

$$\tau = \mu \frac{du}{dy}$$

$$\nu = \frac{\mu}{\rho}$$

#### Módulo de compressibilidade (elasticidade volumétrica)

$$E_v = -\frac{dp}{d\overline{V}/\overline{V}}$$

#### Velocidade do som

$$c = \sqrt{\frac{dp}{d\rho}} = \sqrt{\frac{E_v}{\rho}}$$

$$c = \sqrt{\frac{kp}{\rho}} = \sqrt{kRT}$$

#### Tensão superficial

$$\Delta p = p_i - p_e = \frac{2\sigma}{R}$$

$$2\pi R\sigma = \Delta p \, \pi R^2$$

$$\gamma \pi R^2 h = 2 \pi R \sigma \cos \theta$$

$$h = \frac{2 \sigma \cos \theta}{\gamma R}$$

#### Campo de velocidade

$$\vec{V} = u \vec{i} + v \vec{j} + w \vec{k}$$

$$u = u(x, y, z, t)$$

$$\vec{V} = \frac{d \vec{r}}{dt}$$

#### Escoamento estacionário

$$\frac{\partial \vec{V}}{\partial t} = 0$$

#### Linhas de corrente (escoamento bidimensional)

$$\frac{dy}{dx} = \frac{v}{u}$$

#### Campo de tensão

$$\sigma_n = \lim_{\delta A \to 0} \frac{\delta F_n}{\delta A}$$

$$\tau_1 = \lim_{\delta A \to 0} \frac{\delta F_1}{\delta A}, \quad \tau_2 = \lim_{\delta A \to 0} \frac{\delta F_2}{\delta A}$$

$$
\begin{bmatrix}
\sigma_{xx} & \tau_{xy} & \tau_{xz} \\
\tau_{yx} & \sigma_{yy} & \tau_{yz} \\
\tau_{zx} & \tau_{zy} & \sigma_{zz}
\end{bmatrix}
$$
