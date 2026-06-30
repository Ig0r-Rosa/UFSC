---
lang: pt-BR
geometry: margin=0.65cm
fontsize: 7.5pt
header-includes:
  - \usepackage{multicol}
  - \usepackage{amsmath}
  - \setlength{\columnsep}{0.35cm}
  - \setlength{\parskip}{0pt}
  - \setlength{\parindent}{0pt}
  - \pagestyle{empty}
  - \setlength{\abovedisplayskip}{2pt}
  - \setlength{\belowdisplayskip}{2pt}
  - \renewcommand{\arraystretch}{0.9}
---

\begin{center}
\textbf{\large COLINHA P4 -- Fenômenos de Transporte} \quad $g=9{,}81$ m/s$^2$ \quad $\gamma=\rho g$
\end{center}

\begin{multicols}{2}

\textbf{1. O QUE USAR EM CADA TIPO DE QUESTÃO}

| Problema | Ferramenta |
|---|---|
| Tanque, jato, bandeja | Continuidade + Bernoulli + momento |
| Turbina / bomba | Bernoulli + $\dot{W}=\dot{Q}\Delta p$ |
| Tubo (laminar/turb.) | Re, Darcy, Colebrook, Hagen-Poiseuille |
| Jato em placa / colisão | VC + continuidade + $\sum \dot{m}\vec{V}$ |
| Comporta / represa | $F_R=\gamma h_c A$, centro de pressão |
| Empuxo / flutuação | $E=\gamma V$, $E=W$ ou $E-W=ma$ |

---

\textbf{2. CONTINUIDADE E BERNOULLI}

$$\dot{m}=\rho Q=\rho A V \qquad Q_1=Q_2 \Rightarrow A_1V_1=A_2V_2$$

$$\frac{p}{\gamma}+\frac{V^2}{2g}+z=C \qquad p_1+\tfrac12\rho V_1^2+\gamma z_1=p_2+\tfrac12\rho V_2^2+\gamma z_2$$

Torricelli (jato livre): $V=\sqrt{2gh}$

Venturi/orifício: $Q=A_2\sqrt{\dfrac{2(p_1-p_2)}{\rho[1-(A_2/A_1)^2]}}$

Pitot: $V=\sqrt{2(p_3-p_4)/\rho}$

Bernoulli com máquina/perdas:
$\dfrac{p_1}{\gamma}+\dfrac{V_1^2}{2g}+z_1+h_{bomba}=\dfrac{p_2}{\gamma}+\dfrac{V_2^2}{2g}+z_2+h_L$

Potência: $\dot{W}=\dot{Q}(p_2-p_1)=\dot{Q}\rho g h_{bomba}$

---

\textbf{3. HIDRÁSTATICA (Parte 2)}

$$p=\gamma h \qquad dF=\gamma h\,dA \qquad F_R=\gamma h_c A=\gamma\sin\theta\int y\,dA$$

Centro de pressão: $y_R=\dfrac{I_{xc}}{y_c A}+y_c$ \quad Eixos paralelos: $I_x=I_{xc}+Ay_c^2$

Superfície curva: $F_H=\gamma h_{cg}A_{proj}$; $F_V=\gamma V_{fluido}$; $F_R=\sqrt{F_H^2+F_V^2}$

Empuxo: $E=\gamma V$ \quad Flutua se $\rho_{fl}>\rho_{obj}$

$SG=\rho/\rho_{ref}$ \quad Coroa: $\rho=\dfrac{W_a}{W_a-W_w}\rho_{agua}$

---

\textbf{4. TUBOS -- RE, LAMINAR E TURBULENTO}

$$\text{Re}=\dfrac{\rho V D}{\mu}=\dfrac{V D}{\nu} \qquad \nu=\mu/\rho$$

Laminar: Re$<2100$ \quad Turb.: Re$>4000$ \quad $f=64/\text{Re}$ (laminar)

Hagen-Poiseuille:
$Q=\dfrac{\pi\Delta p D^4}{128\mu L}$, $\bar{V}=\dfrac{\Delta p D^2}{32\mu L}$, $u_{max}=2\bar{V}$

Perfil laminar placas: $\tau=\mu du/dy$, $u=u_{max}[1-(2y/h)^2]$

Darcy-Weisbach: $h_L=f\dfrac{L}{D}\dfrac{V^2}{2g}$ \quad $\Delta p=f\dfrac{L}{D}\dfrac{\rho V^2}{2}$

Colebrook (iterativo):
$\dfrac{1}{\sqrt{f}}=-2\log_{10}\!\left(\dfrac{\varepsilon/D}{3{,}7}+\dfrac{2{,}51}{\text{Re}\sqrt{f}}\right)$

Parede: $\tau_w=\dfrac{\Delta p D}{4L}=\dfrac{f\rho V^2}{8}$

Entrada: $l_e/D=0{,}06\,\text{Re}$ (lam.) ou $4{,}4\,\text{Re}^{1/6}$ (turb.)

Perda local: $h_L=K_L V^2/(2g)$ \quad Circuito: $h_{bomba}=\sum h_L$

---

\textbf{5. DIÂMETRO HIDRÁULICO}

$$D_h=\dfrac{4A}{P}$$

Retâng. $A\times B$: $D_h=2AB/(A+B)$ \quad Anel ext.$A$, int.$B$: $D_h=A-B$

Semicírculo raio $R$: $D_h=2R$ ou $D_h=2\pi R/(\pi+2)$ (confirmar figura)

Use Re e Darcy com $D_h$ no lugar de $D$.

---

\textbf{6. VOLUME DE CONTROLE (Parte 4)}

\textbf{Massa (estacionário):} $\sum \dot{m}_e=\sum \dot{m}_s$ \quad $\dot{m}=\rho Q$

Tanque: $\dfrac{dm}{dt}=\dot{m}_{in}-\dot{m}_{out}$ \quad $\dfrac{d\rho}{dt}=\dfrac{\dot{m}_{in}-\dot{m}_{out}}{V}$

\textbf{Momento (estacionário, 1D):}
$\sum F_x=\dot{m}_e V_e-\dot{m}_s V_s$ (cuidado com sinal e direção)

Jato reto em placa: $F_x=\rho QV(1-\cos\theta)$

Jato inclinado (sem atrito, $|V|$ cte):
$A_0V_0=A_1V_1+A_2V_2$; balanço $x$ dá $A_1$, $A_2$

Colisão de 2 jatos (horizontal):
$Q_3=Q_1+Q_2$; $\sum \dot{m}\vec{V}$ em $x$ e $y$ para achar $V_3$, $\theta_3$

\textbf{Energia:}
$\dot{m}(h_s-h_e+\dfrac{V_s^2-V_e^2}{2}+g(z_s-z_e))=\dot{Q}+\dot{W}$

Com perdas: $\dfrac{p_s}{\rho}+\dfrac{V_s^2}{2}+gz_s=\dfrac{p_e}{\rho}+\dfrac{V_e^2}{2}+gz_e+w_{eixo}-h_L$

---

\textbf{7. FLUIDO -- VISCO, SOM, TENSÃO (Parte 1)}

$$\tau=\mu\dfrac{du}{dy} \qquad \nu=\mu/\rho$$

Linha de corrente 2D: $\dfrac{dy}{dx}=\dfrac{v}{u}$

Tensão superficial: $\Delta p=2\sigma/R$ (bolha/gota)

Capilar: $h=2\sigma\cos\theta/(\gamma R)$

Som: $c=\sqrt{kRT}=\sqrt{E_v/\rho}$ \quad Bernoulli: Ma$<0{,}3$

---

\textbf{8. PROVA ANTIGA -- CHECKLIST RÁPIDO}

\textbf{Tanque + bandeja:} massa $m=\rho V$; cabo $T=W$; saída Torricelli $V=\sqrt{2g(h_1+h_2)}$; continuidade no jato $d_1^2V_1=d_2^2V_2$; $\dot{m}=\rho Q$; força na bandeja = impulso do jato ($F=\dot{m}V$ se para repouso).

\textbf{Turbina 67 kW:} $V=Q/A$; Bernoulli entre reservatório e saída; $\Delta p=\dot{W}/Q$; $p_{abs}=p_{atm}+\gamma h$; sem turbina: só Bernoulli; trajetória: $x=Vt$, $y=h_2-\tfrac12 gt^2$.

\textbf{Tubulação 90 m:} $\varepsilon/D$; Re; se laminar: $u_{max}$, $\bar{V}$, $Q$, $\Delta p$, $f$, $l_e$, $\tau_w$; se turb.: Colebrook + $h_L$.

\textbf{Colisão jatos:} $Q_i=AV_i$; conservação massa; momento $x$ e $y$ para jato 3.

\end{multicols}
