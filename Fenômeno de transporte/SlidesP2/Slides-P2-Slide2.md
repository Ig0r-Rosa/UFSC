# Exercícios sobre conservação de energia

## Tanque rígido — amônia

Considere um tanque rígido e fechado, de $150\ \text{L}$, com vapor de amônia, que está numa temperatura de $100\,^{\circ}\text{C}$, e pressão de $100\ \text{kPa}$. O tanque é resfriado até $-10\,^{\circ}\text{C}$. Calcule a quantidade de calor que sai do sistema durante o processo. Qual a pressão no tanque ao final do processo? Assuma a amônia como um gás ideal.

$$\Delta E = Q - W \Rightarrow \Delta U = Q - W$$

$$\Rightarrow m C_{v0}(T_2 - T_1) = Q - 0$$

$$m = \frac{P_1 V}{R T_1} = \frac{100 \times 0{,}15}{0{,}4882 \times 373{,}15} = 0{,}0823\ \text{kg}$$

$$Q = 0{,}0823 \times 1{,}642 \times (-10 - 100) = -14{,}87\ \text{kJ}$$

$$m = \frac{P_1 V}{R T_1} = \frac{P_2 V}{R T_2} \Rightarrow \frac{P_1}{T_1} = \frac{P_2}{T_2} \Rightarrow P_2 = \frac{263{,}15 \times 100}{373{,}15} = 70{,}52\ \text{kPa}$$

E se a pressão fosse 7 MPa e a amônia estivesse inicialmente na fase líquida?

E se o fluido fosse água?

![Tanque rígido — amônia](Slide%202/2.png)

## Computador em quarto fechado

Um computador em um quarto fechado de $200\ \text{m}^3$ dissipa energia a uma taxa de $10\ \text{kW}$. O quarto tem $50\ \text{kg}$ de madeira, $25\ \text{kg}$ de aço, e ar, e todo o ambiente está a $300\ \text{K}$ e $100\ \text{kPa}$. Quanto tempo será necessário para que a temperatura aumente $10\,^{\circ}\text{C}$. Assuma que todas as massas se aquecem uniformemente.

$$\frac{dE}{dt} = \dot{Q} - \dot{W}$$

$$\frac{\Delta E_W}{\Delta t} + \frac{\Delta E_S}{\Delta t} + \frac{\Delta E_{\text{Air}}}{\Delta t} = \dot{Q} \quad \text{(Não há trabalho)}$$

$$\frac{m_W(u_2 - u_1)_W + m_S(u_2 - u_1)_S + m_{\text{Air}}(u_2 - u_1)_{\text{Air}}}{\Delta t} = \dot{Q}$$

$$\frac{m_W C_W (T_2 - T_1)_W + m_S C_S (T_2 - T_1)_S + m_{\text{Air}} C_{v,\text{Air}} (T_2 - T_1)_{\text{Air}}}{\Delta t} = \dot{Q}$$

$$\Delta t = \frac{(m_W C_W + m_S C_S + m_{\text{Air}} C_{v,\text{Air}})\,\Delta T}{\dot{Q}} = 4{,}2\ \text{min.}$$

![Computador em quarto fechado](Slide%202/3.png)

## Tanque rígido isolado — compartimentos A e B

Um tanque rígido e isolado, está separado em dois compartimentos, por uma placa rígida. O compartimento A tem $0{,}5\ \text{m}^3$ e contém ar a $250\ \text{kPa}$ e $300\ \text{K}$. O compartimento B tem $1\ \text{m}^3$ de ar a $150\ \text{kPa}$ e $1000\ \text{K}$. Qual é a pressão e temperatura final, após a placa ser removida?

E se o fluido fosse água, nas mesmas condições?

Compartimento A — Compartimento B

![Tanque — compartimentos A e B](Slide%202/4.png)

## Sistema com 3 kg

Um sistema com $3\ \text{kg}$ passa por um processo no qual uma quantidade $30\ \text{kJ}$ de calor é transferida da vizinhança para o sistema. A altura do sistema aumenta $600\ \text{m}$ durante o processo. A energia interna específica do sistema diminui $20\ \text{kJ/kg}$.

(a) Assumindo que não há variação de energia cinética no sistema, determine o trabalho que ocorre neste processo.

(b) Assumindo que a velocidade do sistema varia de $60$ a $0\ \text{m/s}$ durante o processo, determine o trabalho nessa situação.

Assuma a aceleração da gravidade como $9{,}81\ \text{m/s}^2$.

![Sistema com 3 kg](Slide%202/5.png)

## Cilindro-pistão — amônia

Um cilindro pistão contém $5\ \text{kg}$ de amônia gasosa a uma temperatura $80\,^{\circ}\text{C}$ e pressão de $800\ \text{kPa}$. Assuma a amônia como um gás ideal.

A amônia expande vagarosamente num processo isotérmico até $300\ \text{kPa}$.

(a) Qual a quantidade de calor e de trabalho transferido no processo? Qual o volume final?

(b) E se a expansão ocorresse através de um processo politrópico com expoente $1{,}3$ até a pressão de $300\ \text{kPa}$, qual seria a quantidade de calor e de trabalho transferido no processo? Qual o volume e temperatura final?

(c) E se a expansão fosse isobárica até o volume final do item (a), qual a quantidade de calor e de trabalho transferido no processo? Qual a temperatura final?

(d) E se a expansão fosse isobárica até o volume final do item (b), qual a quantidade de calor e de trabalho transferido no processo? Qual a temperatura final?

![Cilindro-pistão — amônia (enunciado)](Slide%202/6.png)

### (a) Processo isotérmico

$$\Delta E = Q - W \Rightarrow \Delta U = Q - W$$

$$\Rightarrow m C_{v0}(T_2 - T_1) = Q - W;\ \text{Isotérmico,}\ T_2 = T_1$$

$$0 = Q - W \Rightarrow Q = W$$

$$W_{12} = \int_{V_1}^{V_2} P\, dV$$

$$P V = m R T \Rightarrow P = \frac{m R T}{V} = \frac{C}{V}$$

$$W_{12} = C \int_{V_1}^{V_2} \frac{dV}{V} = C \ln\left(\frac{V_2}{V_1}\right) = m R T \ln\left(\frac{P_1}{P_2}\right)$$

$$W_{12} = 5 \times 0{,}4882 \times 353{,}15 \times \ln\left(\frac{8}{3}\right) = 845{,}5\ \text{kJ}$$

$$V_2 = \frac{m R T}{P_2} = \frac{5 \times 0{,}4882 \times 353{,}15}{300} = 2{,}873\ \text{m}^3$$

![Amônia — isotérmico (a)](Slide%202/7.png)

### (b) Processo politrópico ($n = 1{,}3$)

$$\Delta E = Q - W \Rightarrow \Delta U = Q - W$$

$$\Rightarrow m C_{v0}(T_2 - T_1) = Q - W;\ \text{Politrópico,}\ P_1 V_1^n = P_2 V_2^n \Rightarrow V_2 = V_1 \left(\frac{P_1}{P_2}\right)^{1/n}$$

$$V_1 = \frac{m R T_1}{P_1} = \frac{5 \times 0{,}4882 \times 353{,}15}{800} = 1{,}078\ \text{m}^3 \Rightarrow V_2 = 1{,}078 \left(\frac{8}{3}\right)^{1/1{,}3} = 2{,}292\ \text{m}^3$$

$$P = \frac{P_1 V_1^n}{V^n} = \frac{P_2 V_2^n}{V^n} \Rightarrow P = \frac{C}{V^n}$$

$$W_{12} = C \int_{V_1}^{V_2} \frac{dV}{V^n} = C \left(\frac{V_2^{1-n} - V_1^{1-n}}{1-n}\right) = \frac{P_2 V_2 - P_1 V_1}{1-n} = \frac{m R (T_2 - T_1)}{1-n}$$

$$W_{12} = \frac{300 \times 2{,}292 - 800 \times 1{,}078}{1 - 1{,}3} = 582{,}67\ \text{kJ}$$

$$T_2 = \frac{P_2 V_2}{m R} = \frac{300 \times 2{,}292}{5 \times 0{,}4882} = 281{,}68\ \text{K} = 8{,}5\,^{\circ}\text{C}$$

$$Q = m C_{v0}(T_2 - T_1) + W = 5 \times 1{,}642 \times (8{,}5 - 80) + 582{,}67 = -4{,}345\ \text{kJ}$$

![Amônia — politrópico (b)](Slide%202/8.png)

### (c) e (d) Processo isobárico

$$\Delta E = Q - W \Rightarrow \Delta U = Q - W$$

$$\Rightarrow m C_{v0}(T_2 - T_1) = Q - W;\ \text{Isobárica,}\ P_2 = P_1$$

**(c)**

$$W_{12} = \int_{V_1}^{V_2} P\, dV = 800(2{,}873 - 1{,}078) = 1436\ \text{kJ}$$

$$P V = m R T \Rightarrow \frac{V_1}{T_1} = \frac{V_2}{T_2} \Rightarrow T_2 = 353{,}15 \times \frac{2{,}873}{1{,}078} = 941{,}2\ \text{K} \Rightarrow 668{,}0\,^{\circ}\text{C}$$

$$Q = m C_{v0}(T_2 - T_1) + W = 5 \times 1{,}642 \times (668 - 80) + 1436 = 6263{,}5\ \text{kJ}$$

**(d)**

$$W_{12} = \int_{V_1}^{V_2} P\, dV = 800(2{,}292 - 1{,}078) = 971{,}2\ \text{kJ}$$

$$T_2 = 353{,}15 \times \frac{2{,}292}{1{,}078} = 750{,}9\ \text{K} \Rightarrow 477{,}7\,^{\circ}\text{C}$$

$$Q = m C_{v0}(T_2 - T_1) + W = 5 \times 1{,}642 \times (477{,}7 - 80) + 971{,}2 = 4236{,}3\ \text{kJ}$$

![Amônia — isobárico (c) e (d)](Slide%202/9.png)

## Exemplos de volume de controle (estado estacionário) — Bocais e difusores

**Bocais:** Aumento da velocidade — $V_e \rightarrow$; $\rightarrow V_s > V_e$

**Difusor:** Redução da velocidade — $V_e \rightarrow$; $\rightarrow V_s < V_e$

- Estado estacionário
- Uma vazão de entrada e de saída
- Processo adiabático
- Sem trabalho de eixo
- $\Delta EP$ negligível

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \dot{m} \left(h_s + g z_s + \frac{V_s^2}{2}\right) + \dot{m} \left(h_E + g z_E + \frac{V_E^2}{2}\right)$$

$$h_s + \frac{V_s^2}{2} = h_E + \frac{V_E^2}{2}$$

Se $V_s > V_E$ (Bocal): $h_s < h_E$

Se $V_s < V_E$ (difusor): $h_s > h_E$

**T aumenta ou diminuir?**

![Bocais e difusores](Slide%202/10.png)

## EXEMPLO 6.4

Vapor d'água a $0{,}6\ \text{MPa}$ e $200\,^{\circ}\text{C}$ entra num bocal isolado termicamente com uma velocidade de $50\ \text{m/s}$ e sai com velocidade de $600\ \text{m/s}$ à pressão de $0{,}15\ \text{MPa}$. Determine, no estado final, a temperatura do vapor, se esse estiver superaquecido, ou o título, se estiver saturado.

- **Volume de controle:** Bocal.
- **Estado de entrada:** Determinado (ver Figura 6.7).
- **Estado de saída:** Conhecida $P_s$.
- **Processo:** Regime permanente.
- **Modelo:** Tabelas de vapor d'água.

**Análise:** $\dot{Q}_{v.c.} = 0$ (bocal isolado); $\dot{W}_{v.c.} = 0$; $EP_e \approx EP_s$

**Primeira lei (Equação 6.13)**

$$h_e + \frac{V_e^2}{2} = h_s + \frac{V_s^2}{2}$$

**Solução:**

$$h_s = 2850{,}1 + \frac{(50)^2}{2 \times 1000} - \frac{(600)^2}{2 \times 1000} = 2671{,}4\ \text{kJ/kg}$$

Como $h_s$ é menor que $h_g$ a $0{,}15\ \text{MPa}$:

$$h = h_l + x\, h_{lv}$$

$$2671{,}4 = 467{,}1 + x_s \times 2226{,}5 \Rightarrow x_s = 0{,}99$$

**Figura 6.7** Esboço para o Exemplo 6.4. — $V_e = 50\ \text{m/s}$, $P_e = 0{,}6\ \text{MPa}$, $T_e = 200\,^{\circ}\text{C}$; $V_s = 600\ \text{m/s}$, $P_s = 0{,}15\ \text{MPa}$

![Exemplo 6.4](Slide%202/11.png)

## Ex. 6.23

O bocal de propulsão de um motor a jato é alimentado com ar a $1000\ \text{K}$, $200\ \text{kPa}$ a $30\ \text{m/s}$, como mostra a Figura 6.23. O ar é descarregado do bocal a $850\ \text{K}$ e $90\ \text{kPa}$. Determine a velocidade na seção de descarga admitindo que não haja transferência de calor.

**Figura P6.23** — Entrada de ar — Difusor — Compressor — Câmara de combustão — Entrada de combustível — Turbina — Bocal — Saída de gases quentes

$$\dot{m}_S = \dot{m}_E = \dot{m}$$

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \dot{m} \left(h_S + g z_S + \frac{V_S^2}{2}\right) + \dot{m} \left(h_E + g z_E + \frac{V_E^2}{2}\right)$$

$$h_S + \frac{V_S^2}{2} = h_E + \frac{V_E^2}{2}$$

$$\frac{V_S^2}{2} = h_E - h_S + \frac{V_E^2}{2} \Rightarrow \frac{V_S^2}{2} = 1046220 + \frac{900}{2} - 877400 = 169270$$

$$V_S = 582\ \text{m/s}$$

![Ex. 6.23](Slide%202/12.png)

## Restrição (estrangulamento)

**Exemplos de volume de controle de interesse (estado estacionário)**

Restrição: Perda de pressão (alterações de velocidade às vezes são desprezíveis)

- Estado estacionário
- Uma vazão de entrada e de saída
- Processo adiabático
- Sem trabalho de eixo
- $\Delta EP$ desprezível e $\Delta EC$ geralmente desprezível

**Figura 6.8** O processo de estrangulamento — Superfície de controle

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \dot{m} \left(h_S + g z_S + \frac{V_S^2}{2}\right) + \dot{m} \left(h_E + g z_E + \frac{V_E^2}{2}\right)$$

$$h_S = h_E \Rightarrow u_S + P_S v_S = u_E + P_E v_E$$

Para gases ideais: $h = f(T) \Rightarrow T_E = T_S$

![Processo de estrangulamento](Slide%202/13.png)

## EXEMPLO 6.5

Consideremos o processo de estrangulamento numa válvula de expansão, ou através do tubo capilar, num ciclo de refrigeração por compressão de vapor. Nesse processo, a pressão do refrigerante cai da alta pressão no condensador para a baixa pressão no evaporador e, durante esse processo, uma parte do líquido vaporiza. Se considerarmos o processo como adiabático, o título do refrigerante ao entrar no evaporador pode ser calculado. Admitindo que o fluido refrigerante seja amônia, que entra na válvula de expansão a $1{,}5\ \text{MPa}$ e $35\,^{\circ}\text{C}$ e deixa a válvula a $291\ \text{kPa}$, calcule o título da amônia na saída da válvula de expansão.

- **Volume de controle:** Válvula de expansão ou tubo capilar.
- **Estado de entrada:** $P_e$, $T_e$ conhecidos; estado determinado.
- **Estado de saída:** $P_s$ conhecido.
- **Processo:** Regime permanente.
- **Modelo:** Tabelas de amônia.

**Análise:** $h_e = h_s$

**Solução:** Das tabelas de amônia, $h_e = 346{,}8\ \text{kJ/kg}$

(A entalpia de um líquido ligeiramente comprimido é praticamente igual à entalpia do líquido saturado à mesma temperatura).

$$h_s = h_e = 346{,}8 = 134{,}3 + x_s(1296{,}4)$$

$$x_s = 0{,}1638 = 16{,}38\%$$

![Exemplo 6.5](Slide%202/14.png)

## Trocadores de calor

Energia no VC constante. Variação da energia das vazões que cruzam a superfície de controle.

- Estado estacionário
- Processo adiabático
- Sem trabalho de eixo
- $\Delta EP$ e $\Delta EC$ desprezível
- Múltiplas entradas e saídas

**Figura 6.6** Diagrama esquemático de um condensador para R-134a.

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \sum_{S} \dot{m}_s \left(h_s + g z_s + \frac{V_s^2}{2}\right) + \sum_{E} \dot{m}_e \left(h_e + g z_e + \frac{V_e^2}{2}\right)$$

$$\sum_{S} \dot{m}_s \cdot h_s = \sum_{E} \dot{m}_e \cdot h_e$$

![Trocadores de calor](Slide%202/15.png)

## EXEMPLO 6.3

Considere um condensador, resfriado a água, de um sistema de refrigeração de grande porte que utiliza R-134a como fluido refrigerante. O refrigerante entra no condensador a $60\,^{\circ}\text{C}$ e $1\ \text{MPa}$ e o deixa como líquido a $0{,}95\ \text{MPa}$ e $35\,^{\circ}\text{C}$. A água de resfriamento entra no condensador a $10\,^{\circ}\text{C}$ e sai a $20\,^{\circ}\text{C}$. Sabendo que a vazão de refrigerante é igual a $0{,}2\ \text{kg/s}$, determine a vazão de água de resfriamento nesse condensador.

- **Volume de controle:** Condensador. **Esboço:** Figura 6.6.
- **Estados de entrada:** R-134a — determinado; água — determinado.
- **Estados de saída:** R-134a — determinado; água — determinado.
- **Processo:** Regime permanente. **Modelo:** Tabelas de R-134a e de vapor d'água.

**Análise:** $\sum \dot{m}_e h_e = \sum \dot{m}_s h_s$

$$\dot{m}_r (h_e)_r + \dot{m}_a (h_e)_a = \dot{m}_r (h_s)_r + \dot{m}_a (h_s)_a$$

**Solução:** $(h_e)_r = 441{,}89\ \text{kJ/kg}$; $(h_s)_r = 249{,}10\ \text{kJ/kg}$; $(h_e)_a = 42{,}00\ \text{kJ/kg}$; $(h_s)_a = 83{,}95\ \text{kJ/kg}$

$$\dot{m}_a = \dot{m}_r \frac{(h_e - h_s)_r}{(h_s - h_e)_a} = 0{,}2 \frac{(441{,}89 - 249{,}10)}{(83{,}95 - 42{,}00)} = 0{,}919\ \text{kg/s}$$

$$\dot{Q}_{v.c.} = \dot{m}_r (h_s - h_e)_r = 0{,}2 \times (249{,}10 - 441{,}89) = -38{,}558\ \text{kW}$$

$$\dot{m}_a = \frac{38{,}558}{(83{,}95 - 42{,}00)} = 0{,}919\ \text{kg/s}$$

Para outro exemplo de exercício resolvido, veja o exercício 5.4.2.3 de SCHÜRHAUS, P. *Termodinâmica*. União da Vitória: Centro Universitário de União da Vitória, 2007.

![Exemplo 6.3](Slide%202/16.png)

## Turbina e compressor

**Turbina (2 processos):**

- Expansão a alta pressão de um gás ou vapor (aumento da velocidade em um bocal)
- Transferência de EC para os rotores da turbina (redução da velocidade e produção de trabalho de eixo).

**Figura P6.46** — $\dot{W}_T$

**Compressor (2 processos):**

- Consumo de trabalho de eixo para aumentar a velocidade e a EC do fluido.
- Fluido passa por um difusor para diminuir a velocidade e aumentar a pressão.

**Figura P6.54** — $-\dot{W}_c$

- Estado estacionário
- Uma vazão de entrada e de saída
- Processo adiabático (**nem sempre**)
- $\Delta EP$ geralmente desprezível

$$0 = (\dot{Q} - \dot{W}_{\text{eixo}})_{VC} - \dot{m} \left(h_s + g z_s + \frac{V_s^2}{2}\right) + \dot{m} \left(h_E + g z_E + \frac{V_E^2}{2}\right)$$

$$\dot{W}_{\text{eixo}} = \dot{m}(h_E - h_s) \Rightarrow w_{\text{eixo}} = (h_E - h_s)$$

![Turbina e compressor](Slide%202/17.png)

## Exemplo 3.6

Vapor d'água entra em uma turbina a $4.000\ \text{kPa}$ e $500\,^{\circ}\text{C}$ e sai como mostrado na Figura 3.6. Para uma velocidade de entrada de $200\ \text{m/s}$, calcule a potência de saída da turbina. Considere desprezível qualquer transferência de calor, variação de energia cinética e potencial.

$$\Delta h = w_s \Rightarrow \dot{W} = \dot{m}(h_E - h_S)$$

$h_1 = 3.445{,}0\ \text{kJ/kg}$; $v_1 = 86{,}341\ \text{cm}^3/\text{g}$; $h_2 = 2.665{,}8\ \text{kJ/kg}$ ($x_2 = 1$)

$$\dot{m} = \rho_1 V_1 A_1 = \frac{V_1 A_1}{v_1} = \frac{(200\ \text{m/s})(1{,}96 \times 10^{-3}\ \text{m}^2)}{0{,}086341\ \text{m}^3/\text{kg}} = 4{,}54\ \text{kg/s}$$

$$\dot{W} = 4{,}54(3445{,}0 - 2665{,}8) = 3538\ \text{kW}$$

**Figura 3.6** Turbina operando com vapor d'água. — $V_1 = 200\ \text{m/s}$, $P_1 = 4000\ \text{kPa}$, $T_1 = 500\,^{\circ}\text{C}$, $\phi = 50\ \text{mm}$; $P_2 = 80\ \text{kPa}$, $x_2 = 1{,}0$, $\phi = 250\ \text{mm}$, $\dot{W}_s$

![Exemplo 3.6](Slide%202/18.png)

## Compressor — ar

Ar entra num compressor a $37\,^{\circ}\text{C}$ e $92\ \text{kPa}$, e recebe $355\ \text{kJ/kg}$ de trabalho.

(a) Qual a temperatura do ar na saída do compressor? $^{\circ}\text{C}$.

(b) Considerando que o processo do ar pelo compressor é um processo politrópico com expoente igual a $1{,}32$, qual a pressão na saída do compressor?

![Compressor — ar](Slide%202/19.png)
