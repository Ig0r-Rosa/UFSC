# Explorando outras características da pressão

1. Pressão em um ponto
2. Pressão em diferentes pontos
3. Medidas de pressão

## Pressão

- A *pressão absoluta* é medida em relação à pressão zero absoluta (sempre positiva).
- A *pressão manométrica* é medida em relação à pressão da atmosfera ao redor do instrumento de medição (pode ser negativa ou positiva).
- Nas ciências térmicas, assume-se pressão absoluta a menos que declarada de outra maneira.
  - Pressão arterial de 12/8, o que significa?
  - É manométrica ou absoluta?

**Figura 2.12** Ilustração dos termos utilizados em medidas de pressão.

- $P_{abs,1}$ — $P_{atm}$ — $P_{abs,2}$
- Barômetro lê a pressão atmosférica
- Manômetro comum: $\Delta P = P_{abs,1} - P_{atm}$
- Manômetro de vácuo: $\Delta P = P_{atm} - P_{abs,2}$

![Figura 2.12 — medidas de pressão](Slide%202/2.png)

## Gage versus Absolute Pressure

- $1\ \text{Pa} = 1\ \text{N/m}^2$
- $1\ \text{bar} = 10^5\ \text{Pa} = 0{,}1\ \text{MPa}$
- $1\ \text{atm} = 101{,}325\ \text{Pa} = 101{,}3\ \text{kPa}$

$P_{abs} = 0$ (vacuum) — $P_{atm} = 101{,}3\ \text{kPa}$

$P_{abs,1} = 200\ \text{kPa}$ — $P_{gage,1} = P_{abs,1} - P_{atm} = 98{,}7\ \text{kPa}$

$P_{abs,2} = 30\ \text{kPa}$ — $P_{gage,2} = P_{abs,2} - P_{atm} = -71{,}3\ \text{kPa}$

![Gage versus Absolute Pressure](Slide%202/3.png)

## 1. Pressão em um ponto

Como a pressão ao redor de um ponto varia?

- A pressão ao redor de um ponto é a mesma.
- A pressão é a mesma em todos os pontos em um plano horizontal em um determinado fluido, independentemente da geometria, desde que os pontos estejam interligados pelo mesmo fluido.

$P_A = P_B = P_C = P_D = P_E = P_F = P_G = P_{atm} + \rho gh$

$P_H \neq P_I$

![Pressão em plano horizontal — recipiente irregular](Slide%202/5.png)

Considere um volume de fluido triangular.

As forças atuando são relativas ao peso e a pressão.

**Não há tensão de cisalhamento!!**

1. Fluido em repouso
2. Fluido em movimento, mas volume de fluido se move como um corpo rígido

![Volume de fluido triangular](Slide%202/6.png)

Forças agindo neste volume de controle arbitrário.

![Forças no volume de controle](Slide%202/7.png)

A segunda Lei de Newton nas direções y e z respectivamente,

$$\sum F_y = p_y \delta x \delta z - p_s \delta x \delta s \sin \theta = \rho \frac{\delta x \delta y \delta z}{2} a_y$$

$$\sum F_z = p_z \delta x \delta y - p_s \delta x \delta s \cos \theta - \gamma \frac{\delta x \delta y \delta z}{2} = \rho \frac{\delta x \delta y \delta z}{2} a_z$$

$$e \quad \delta y = \delta s \cos \theta \quad \delta z = \delta s \sin \theta$$

As equações de movimento podem ser reescritas como:

$$p_y - p_s = \rho a_y \frac{\delta y}{2}$$

$$p_z - p_s = (\rho a_z + \gamma) \frac{\delta z}{2}$$

Se $\delta y, \delta z$ tenderem ao limite e se aproximarem de zero:

$$p_y = p_s = p_z$$

O ângulo $\theta$ foi escolhido arbitrariamente, então, pode-se concluir que a pressão em um ponto de um fluido em movimento ou em repouso é independente da direção, se o ponto não receber um tensão de cisalhamento

## 2. Equação básica para um campo de pressão

Como a pressão em um fluido varia entre um ponto e outro, quando não há tensão de cisalhamento ?

## Forças internas e externas agindo em um pequeno elemento de volume

A pressão no centro do elemento é $p$

![Elemento de volume e forças de pressão](Slide%202/12.png)

A resultante da forças externas na direção y:

$$\delta F_y = \left( p - \frac{\partial p}{\partial y} \frac{\delta y}{2} \right) \delta x \delta z - \left( p + \frac{\partial p}{\partial y} \frac{\delta y}{2} \right) \delta x \delta z$$

ou

$$\delta F_y = -\frac{\partial p}{\partial y} \delta x \delta y \delta z$$

Por similaridade, as resultantes das forças nas direções x e z são

$$\delta F_x = -\frac{\partial p}{\partial x} \delta x \delta y \delta z$$

$$\delta F_z = -\frac{\partial p}{\partial z} \delta x \delta y \delta z$$

E a resultante das forças externas agindo no elemento de volume é

$$\delta \hat{F}_s = -\left( \frac{\partial p}{\partial x} \hat{i} + \frac{\partial p}{\partial y} \hat{j} + \frac{\partial p}{\partial z} \hat{k} \right) \delta x \delta y \delta z = -\nabla p \delta x \delta y \delta z$$

O eixo z é vertical, e o peso é

$$-\delta W \hat{k} = -\gamma \delta x \delta y \delta z \hat{k}$$

De acordo com a segunda lei de Newton

$$\sum \delta \hat{F} = \delta \hat{F}_s - \delta W \hat{k} = \delta m \hat{a}$$

ou

$$-\nabla p \delta x \delta y \delta z - \gamma \delta x \delta y \delta z \hat{k} = \rho \delta x \delta y \delta z \hat{a}$$

Ou

$$-\nabla p - \gamma \hat{k} = \rho \hat{a}$$

A equação geral de movimento para um fluido onde não há tensão de cisalhamento.

## 3. Para um fluido em repouso

$$\hat{a} = 0$$

$$\nabla p + \gamma \hat{k} = 0$$

ou

$$\frac{\partial p}{\partial x} = \frac{\partial p}{\partial y} = 0$$

$$\frac{\partial p}{\partial z} = -\gamma$$

### 3.1 Para um fluido homogêneo e incompressível

Integração direta com peso específico constante,

$$\int_{p_1}^{p_2} dp = -\gamma \int_{z_1}^{z_2} dz$$

Se a superfície do fluido for o plano de referência

$$p = \gamma h + p_0$$

### 3.2 Para um fluido compressível

Gases como ar, oxigênio e nitrogênio são compressíveis.

A equação de estado para um gás ideal é

$$p = \rho RT$$

E

$$\frac{dp}{dz} = -\frac{gp}{RT}$$

ou

$$\int_{p_1}^{p_2} \frac{dp}{p} = \ln \frac{p_2}{p_1} = -\frac{g}{R} \int_{z_1}^{z_2} \frac{dz}{T}$$

## Variação da pressão com a profundidade

A pressão cresce linearmente com a profundidade quando a massa específica é constante

$$\Delta P = P_2 - P_1 = \rho g \Delta z = \gamma_s \Delta z$$

$$P = P_{atm} + \rho g h \quad \text{or} \quad P_{gage} = \rho g h$$

$$\Delta P = P_2 - P_1 = -\int_1^2 \rho g \, dz$$

![Variação da pressão com a profundidade](Slide%202/20.png)

## Lei de Pascal

A pressão aplicada em um fluido confinado aumenta a pressão em todo o fluido na mesma quantia.

Levantamento de uma grande massa pela aplicação de uma pequena força

$$P_1 = P_2 \rightarrow \frac{F_1}{A_1} = \frac{F_2}{A_2} \rightarrow \frac{F_2}{F_1} = \frac{A_2}{A_1}$$

$F_1 = P_1 A_1$ — $F_2 = P_2 A_2$

![Lei de Pascal — macaco hidráulico](Slide%202/21.png)

## Manometria

Técnica para medir pressão que envolve o uso de colunas de líquido ----- **manômetro.**

*Tubo Piezométrico, Tube em U e Tubo Inclinado*

## Medição da Pressão (manometria)

- Método simples e razoavelmente preciso para medir a pressão

**Figura 2.13:** Exemplo de medição de pressão com uma coluna de líquido.

Fluido $P$ — $P_{atm} = P_0$ — $H$ — pontos $A$ e $B$ — $g$

(Uma sala com 5 m de altura) — $P_{topo} = 1\ \text{atm}$ — $P_{piso} = 1{,}006\ \text{atm}$

A variação de pressão num gas em repouso (sistema) é desprezível em varios volumes de controle

![Medição da pressão — Figura 2.13](Slide%202/23.png)

**Figura 2.12** Ilustração dos termos utilizados em medidas de pressão.

**Figura 2.14** Barômetro.

$\rho_{Hg} = 13595\ \text{kg/m}^3$

$g = 9{,}807\ \text{m/s}^2$

![Figuras 2.12 e 2.14 — barômetro](Slide%202/24.png)

## Medição da Pressão

- Os barômetros de mercúrio e os manômetros diferenciais medem a pressão através da altura da coluna de um líquido

![Manômetro diferencial e barômetro de mercúrio](Slide%202/25.png)

### Manômetro de Tubo piezométrico

Tubo vertical aberto no topo.

Construção simples

$$p_A = \gamma_1 h_1$$

Relativamente exato e simples, qual o problema na sua utilização?

![Manômetro de tubo piezométrico](Slide%202/26.png)

### 2) Tubo em U

$$p_A = \gamma_2 h_2 - \gamma_1 h_1$$

![Tubo em U](Slide%202/27.png)

Determine uma equação para $p_A - p_B$

$$p_A - \gamma_1 h_1 - \gamma_2 h_2 + \gamma_1 (h_1 + h_2) = p_B$$

$$p_A - p_B = h_2 (\gamma_2 - \gamma_1)$$

![Manômetro diferencial — bocal de fluxo](Slide%202/28.png)

### 3) Tubo Inclinado

$$p_A + \gamma_1 h_1 = p_B + \gamma_2 l_2 \sin \theta + \gamma_3 h_3$$

$$p_A - p_B = \gamma_2 l_2 \sin \theta + \gamma_3 h_3 - \gamma_1 h_1$$

Útil para medir pequena variação de pressão: $\sin \theta \rightarrow 0$ as $\theta \rightarrow 0$

![Tubo inclinado](Slide%202/29.png)

## Transdutor de pressão

- Conversão de medida de pressão em sinal elétrico.
  - Pressão move a bobina, criando uma tensão nos terminais de saída do transformador.

**Figura 2.14** Transdutor de pressão que combina um transformador linear diferencial variável com um tubo de Bourdon (Ref.[4], reprodução autorizada).

Tubo de Bourdon — Tomada de pressão — Núcleo — Transformador diferencial linear — Dispositivo para montagem — Mola — Entrada — Saída

![Transdutor de pressão — Figura 2.14](Slide%202/30.png)

## Medição da Pressão

- O manômetro de Bourdon é um aparelho mecânico que mede a pressão pela deformação de um tubo elíptico, para leitura por inspeção visual de um indivíduo

Tipo-C — Espiral — Tubo torcido — Helicoidal — Seção transversal de tubo

![Manômetro de Bourdon](Slide%202/31.png)

## Medição da Pressão

- Transdutor de pressão:
  - Uso várias técnicas para converter o efeito de pressão em um efeito elétrico, como uma mudança de tensão, resistência ou capacitância.
  - Os transdutores de pressão são menores e mais rápidos e podem ser mais sensíveis, confiáveis e precisos do que os seus equivalentes mecânicos.

### Exercício 3.4

**3.4** Você está sobre a lateral de uma montanha e, ao ferver água, nota que a temperatura de ebulição é 90°C. Qual é a altitude aproximada em que você se encontra? No dia seguinte, você está em outro local nesta montanha onde a água ferve a 85°C. Considere a Atmosfera-Padrão Americana.

**Condições da Atmosfera-Padrão nos EUA ao nível do mar**

| Propriedade | Símbolo | SI |
| :--- | :--- | :--- |
| Temperatura | T | 15°C |
| Pressão | p | 101,3 kPa (abs) |
| Massa específica | $\rho$ | 1,225 kg/m³ |
| Peso específico | $\gamma$ | — |
| Viscosidade | $\mu$ | $1{,}789 \times 10^{-5}$ kg/(m·s) (Pa·s) |

![Atmosfera-Padrão — gráfico e tabela](Slide%202/33.png)

**3.8** Um cubo metálico oco, com arestas de 100 mm, flutua na interface entre uma camada de água e uma camada de óleo SAE 10W de tal forma que 10% do cubo está imerso no óleo. Qual é a diferença de pressão entre a face horizontal superior e a inferior do cubo? Qual é a massa específica média do cubo?

**3.15** Com o polegar, você fecha o topo do canudinho do seu refrigerante e levanta-o para fora do copo que contém a bebida. Mantendo-o na vertical, o seu comprimento total é 45 cm, mas o refrigerante ocupa 15 cm no interior do canudinho, contadas a partir do fundo. Qual é a pressão dentro do canudinho logo abaixo do seu polegar? Ignore qualquer efeito de tensão superficial.

**3.17** Um reservatório com dois tubos cilíndricos verticais de diâmetros $d_1 = 39{,}5$ mm e $d_2 = 12{,}7$ mm é parcialmente preenchido com mercúrio. O nível de equilíbrio do líquido é mostrado no diagrama da esquerda. Um objeto cilíndrico sólido, feito de latão, flutua no tubo maior conforme mostrado no diagrama da direita. O objeto tem diâmetro $D = 37{,}5$ mm e altura $H = 76{,}2$ mm. Calcule a pressão na superfície inferior necessária para fazer flutuar o objeto. Determine o novo nível de equilíbrio, $h$, do mercúrio com a presença do cilindro de metal.

**3.26** Água flui para baixo ao longo de um tubo inclinado de $30^\circ$ em relação à horizontal conforme mostrado. A diferença de pressão $p_A - p_B$ é causada parcialmente pela gravidade e parcialmente pelo atrito. Deduza uma expressão algébrica para a diferença de pressão. Calcule a diferença de pressão se $L = 1{,}5$ m e $h = 150$ mm.

![Exercícios 3.8, 3.15, 3.17 e 3.26](Slide%202/34.png)

**2.68** Um barômetro que apresenta imprecisão de medida igual a 1 mbar (0,001 bar) foi utilizado para medir a pressão atmosférica no nível do chão e na cobertura de um edifício alto. Determine a incerteza no valor da altura do prédio calculada a partir dos valores das pressões atmosféricas medidas.

**2.68** Assume we use a pressure gauge to measure the air pressure at street level and at the roof of a tall building. If the pressure difference can be determined with an accuracy of 1 mbar (0.001 bar) what uncertainty in the height estimate does that corresponds to?

$\rho_{air} = 1{,}169\ \text{kg/m}^3$ from Table A.5

$\Delta P = 0{,}001\ \text{bar} = 100\ \text{Pa}$

$$L = \frac{\Delta P}{\rho g} = \frac{100}{1{,}169 \times 9{,}807} = 8{,}72\ \text{m}$$

**Atenção:** a pergunta em inglês é diferente da pergunta em português. A resposta da pergunta em português é duas vezes a resposta da pergunta em inglês.

![Exercício 2.68 — barômetro](Slide%202/35.png)
