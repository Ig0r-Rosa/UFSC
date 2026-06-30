"""Exporta gráficos do Trabalho 3 com verificação visual dos requisitos."""

from __future__ import annotations

import warnings
from pathlib import Path

import control as ct
import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")
plt.rcParams.update(
    {
        "figure.dpi": 130,
        "font.size": 10,
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.35,
    }
)

FIG = Path(__file__).parent / "figuras"
FIG.mkdir(exist_ok=True)
s = ct.tf("s")


def salvar(fig: plt.Figure, nome: str) -> None:
    fig.tight_layout()
    fig.savefig(FIG / nome, bbox_inches="tight")
    plt.close(fig)


def tempo_acomodacao(y: np.ndarray, t: np.ndarray, ref: float, band_pct: float) -> float:
    """Último instante em que |y-ref| excede band_pct% de |ref|."""
    faixa = (band_pct / 100.0) * abs(ref)
    for i in range(len(y) - 1, -1, -1):
        if abs(y[i] - ref) > faixa:
            return float(t[i + 1]) if i + 1 < len(t) else float(t[-1])
    return 0.0


def zeta_dominante(polos: np.ndarray) -> float | None:
    complexos = polos[np.abs(np.imag(polos)) > 1e-4]
    if len(complexos) == 0:
        return None
    p = complexos[np.argmax(np.real(complexos))]
    return float(-np.real(p) / abs(p))


def plot_degrau_verificacao(
    T: ct.TransferFunction,
    nome: str,
    titulo: str,
    *,
    tmax: float = 8,
    ref: float = 1.0,
    band_pct: float = 5.0,
    ts_alvo: float | None = None,
) -> dict:
    """Plota resposta ao degrau com faixa de tolerância e $T_s$ medido."""
    t = np.linspace(0, tmax, 3000)
    tout, yout = ct.step_response(T, t)
    info = ct.step_info(T)
    y_final = float(info["SteadyStateValue"])
    ts_med = tempo_acomodacao(yout, tout, y_final, band_pct)
    zeta = zeta_dominante(ct.poles(T))

    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.plot(tout, yout, "b", lw=2, label=r"$y(t)$")
    ax.axhline(ref, color="k", ls=":", alpha=0.6, label="Referência")
    ax.axhline(y_final, color="orange", ls="-.", alpha=0.7,
               label=rf"$y_{{ss}}={y_final:.3f}$")
    ax.axhline(y_final * (1 + band_pct / 100), color="r", ls="--", alpha=0.6,
               label=rf"Faixa ±{band_pct:.0f}%")
    ax.axhline(y_final * (1 - band_pct / 100), color="r", ls="--", alpha=0.6)
    ax.axvline(ts_med, color="g", ls="--", alpha=0.85,
               label=rf"$T_s={ts_med:.2f}\,$s")

    if ts_alvo is not None:
        ax.axvline(ts_alvo, color="purple", ls=":", alpha=0.7,
                   label=rf"Alvo $T_s={ts_alvo:.2f}\,$s")

    if info["Overshoot"] > 0.1:
        ax.plot(info["PeakTime"], info["Peak"], "ro", ms=7,
                label=rf"$M_p={info['Overshoot']:.1f}\%$")

    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(titulo)
    ax.legend(loc="lower right", fontsize=8)
    salvar(fig, nome)

    return {
        "ts_med": ts_med,
        "y_final": y_final,
        "ess": ref - y_final,
        "overshoot": float(info["Overshoot"]),
        "zeta": zeta,
    }


def plot_polos_ab_fech(
    T_ol: ct.TransferFunction,
    T_cl: ct.TransferFunction,
    nome: str,
    titulo: str,
    zeta_ref: float | None = None,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, sys, sub in zip(axes, [T_ol, T_cl], ["Malha aberta", "Malha fechada"]):
        p, z = ct.poles(sys), ct.zeros(sys)
        ax.scatter(np.real(p), np.imag(p), marker="x", s=80, color="crimson", label="Polos")
        if len(z):
            ax.scatter(np.real(z), np.imag(z), marker="o", s=60,
                       facecolors="none", edgecolors="royalblue", label="Zeros")
        ax.axvline(0, color="k", lw=0.8)
        ax.axhline(0, color="k", lw=0.8)
        ax.set_xlabel("Re(s)")
        ax.set_ylabel("Im(s)")
        ax.set_title(sub)
        ax.legend()
    if zeta_ref is not None:
        polos = ct.poles(T_cl)
        cx = polos[np.abs(np.imag(polos)) > 1e-4]
        if len(cx):
            p = cx[np.argmax(np.real(cx))]
            sigma, wd = -np.real(p), abs(np.imag(p))
            axes[1].plot([0, -2 * sigma], [0, 2 * wd], "g--", alpha=0.6,
                         label=rf"$\zeta={zeta_ref}$")
            axes[1].plot([0, -2 * sigma], [0, -2 * wd], "g--", alpha=0.6)
            axes[1].legend()
    fig.suptitle(titulo, fontsize=11)
    salvar(fig, nome)


def plot_lgr(L: ct.TransferFunction, nome: str, titulo: str) -> None:
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ct.rlocus(L, ax=ax, grid=True)
    ax.set_title(titulo)
    salvar(fig, nome)


def plot_comp(t, y_sem, y_com, nome: str, titulo: str) -> None:
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, y_sem, color="gray", ls="--", label="Sem controlador")
    ax.plot(t, y_com, "b", lw=2, label="Com controlador")
    ax.axhline(1.0, color="k", ls=":", alpha=0.5)
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title(titulo)
    ax.legend()
    salvar(fig, nome)


# --- Q1 ---
G1 = 1 / ((s + 2) * (s + 5))
C1 = (5 * s**2 + 38 * s + 64) / s
L1, T1 = C1 * G1, ct.feedback(C1 * G1, 1)
plot_degrau_verificacao(T1, "q1_degrau.png", "Q1 — Verificação: resposta ao degrau", tmax=3, ts_alvo=1.0)
plot_polos_ab_fech(L1, T1, "q1_polos.png", "Q1 — Polos e zeros")
plot_lgr(L1, "q1_lgr.png", r"Q1 — Lugar das raízes de $L(s)$")
t1 = np.linspace(0, 10, 2000)
_, y1s = ct.step_response(G1, t1)
_, y1c = ct.step_response(T1, t1)
plot_comp(t1, y1s, y1c, "q1_comparacao.png", "Q1 — Com e sem controlador")

# --- Q2 ---
G2 = 20 / ((s + 2) * (s + 4))
C2 = (0.8 * s**2 + 6.1 * s + 18.75) / s
L2, T2 = C2 * G2, ct.feedback(C2 * G2, 1)
plot_degrau_verificacao(T2, "q2_degrau.png", r"Q2 — Verificação ($\zeta=0{,}7$)", tmax=3)
plot_polos_ab_fech(L2, T2, "q2_polos.png", "Q2 — Polos e zeros", 0.7)
plot_lgr(L2, "q2_lgr.png", r"Q2 — Lugar das raízes de $L(s)$")
t2 = np.linspace(0, 4, 2000)
_, y2s = ct.step_response(G2, t2)
_, y2c = ct.step_response(T2, t2)
plot_comp(t2, y2s, y2c, "q2_comparacao.png", "Q2 — Com e sem controlador")

# --- Q3 ---
G3 = 1 / (s * (1 + 0.1 * s))
C3 = 640 / 9 + (5 / 3) * s
L3, T3 = C3 * G3, ct.feedback(C3 * G3, 1)
plot_degrau_verificacao(T3, "q3_degrau.png", r"Q3 — Verificação ($\zeta=0{,}5$, $T_s$)", tmax=1.2, ts_alvo=0.3)
plot_polos_ab_fech(L3, T3, "q3_polos.png", "Q3 — Polos e zeros", 0.5)
plot_lgr(L3, "q3_lgr.png", r"Q3 — Lugar das raízes de $L(s)$")
t3 = np.linspace(0, 2, 2000)
_, y3s = ct.step_response(G3, t3)
_, y3c = ct.step_response(T3, t3)
plot_comp(t3, y3s, y3c, "q3_comparacao.png", "Q3 — Com e sem controlador")

# --- Q4 ---
G4 = 5 / (1 + 0.5 * s)
C4 = (19.8 * s + 792) / (s + 40)
L4, T4 = C4 * G4, ct.feedback(C4 * G4, 1)
m4 = plot_degrau_verificacao(
    T4, "q4_degrau.png", "Q4 — Verificação ($e_{ss}=1\\%$, $T_s$)",
    tmax=0.5, band_pct=5.0, ts_alvo=0.1,
)
t4 = np.linspace(0, 0.8, 2000)
tout4, yout4 = ct.step_response(T4, t4)
erro4 = 1.0 - yout4
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(tout4, erro4, "r", lw=2, label=r"$e(t)=1-y(t)$")
ax.axhline(0.01, color="k", ls=":", label=r"$e_{ss}=1\%$")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Erro")
ax.set_title("Q4 — Verificação do erro ao degrau")
ax.legend()
salvar(fig, "q4_erro.png")
plot_polos_ab_fech(L4, T4, "q4_polos.png", "Q4 — Polos e zeros")
plot_lgr(L4, "q4_lgr.png", r"Q4 — Lugar das raízes de $L(s)$")
t4c = np.linspace(0, 1, 2000)
_, y4s = ct.step_response(G4, t4c)
_, y4c = ct.step_response(T4, t4c)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t4c, y4s, color="gray", ls="--", label="Sem controlador")
ax.plot(t4c, y4c, "b", lw=2, label="Com compensador")
ax.axhline(1.0, color="orange", ls="-.", alpha=0.5, label="Referência")
ax.axhline(0.99, color="k", ls=":", alpha=0.5, label="Alvo 99%")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Q4 — Com e sem controlador")
ax.legend()
salvar(fig, "q4_comparacao.png")

# --- Q5 ---
G5 = 4 / ((s + 1) * (s + 3) * (s + 4))
C5 = (2.8503 * s**2 + 8.8972 * s + 6.0469) / s
L5, T5 = C5 * G5, ct.feedback(C5 * G5, 1)
plot_degrau_verificacao(T5, "q5_degrau.png", r"Q5 — Verificação ($\zeta=0{,}7$, $T_s$)", tmax=6, ts_alvo=1.5)
plot_polos_ab_fech(L5, T5, "q5_polos.png", "Q5 — Polos e zeros", 0.7)
plot_lgr(L5, "q5_lgr.png", r"Q5 — Lugar das raízes de $L(s)$")
t5 = np.linspace(0, 8, 2000)
_, y5s = ct.step_response(G5, t5)
_, y5c = ct.step_response(T5, t5)
plot_comp(t5, y5s, y5c, "q5_comparacao.png", "Q5 — Com e sem controlador")

# --- Q6 ---
Ku = 35.0
Pu = 2 * np.pi / np.sqrt(19)
C6 = 0.45 * Ku + (0.54 * Ku / Pu) / s
T6_crit = ct.feedback(Ku * G5, 1)
T6 = ct.feedback(C6 * G5, 1)
t6c = np.linspace(0, 3 * Pu, 2000)
tout6c, y6c = ct.step_response(T6_crit, t6c)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(tout6c, y6c, "r", lw=1.8, label=rf"$K_p=K_u={Ku:.0f}$")
ax.axhline(0, color="k", lw=0.6)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.set_title(rf"Q6 — Oscilações sustentadas ($P_u\approx{Pu:.2f}\,$s)")
ax.legend()
salvar(fig, "q6_critico.png")
plot_degrau_verificacao(T6, "q6_degrau.png", "Q6 — Verificação: resposta PI (ZN)", tmax=25)
pol6 = [ct.poles(T6_crit), ct.poles(T6)]
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
for ax, p, sub in zip(axes, pol6, [r"Com $K=K_u$", "Com PI (ZN)"]):
    ax.scatter(np.real(p), np.imag(p), marker="x", s=80, color="crimson")
    ax.axvline(0, color="k", lw=0.8)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_xlabel("Re(s)")
    ax.set_ylabel("Im(s)")
    ax.set_title(sub)
fig.suptitle("Q6 — Polos no plano-s", fontsize=11)
salvar(fig, "q6_polos.png")
t6 = np.linspace(0, 20, 3000)
_, y6zn = ct.step_response(T6, t6)
_, y6pid = ct.step_response(T5, t6)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t6, y6zn, "b", lw=2, label="PI — Ziegler-Nichols")
ax.plot(t6, y6pid, "g--", lw=2, label="PID — Questão 5")
ax.axhline(1.0, color="k", ls=":", alpha=0.5)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Q6 — Comparação PI (ZN) vs. PID (Q5)")
ax.legend()
salvar(fig, "q6_comparacao.png")

# --- Q7 ---
G7 = 400 / (s * (s + 40))
C7_ini = (0.5477 * s + 2.9645) / s
C7 = 0.5295 + 1.0494 / s
L7, T7 = C7 * G7, ct.feedback(C7 * G7, 1)
T7_ini = ct.feedback(C7_ini * G7, 1)
plot_degrau_verificacao(
    T7, "q7_degrau.png", "Q7 — Verificação ($M_p$, $T_s$)",
    tmax=5, band_pct=2.0, ts_alvo=1.5,
)
t7c = np.linspace(0, 5, 2500)
_, y7i = ct.step_response(T7_ini, t7c)
_, y7a = ct.step_response(T7, t7c)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t7c, y7i, color="gray", ls="--", lw=2, label="PI inicial")
ax.plot(t7c, y7a, "b", lw=2, label="PI ajustado")
ax.axhline(1.0, color="k", ls=":", alpha=0.5)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Q7 — PI inicial vs. PI ajustado")
ax.legend()
salvar(fig, "q7_ajuste.png")
plot_polos_ab_fech(L7, T7, "q7_polos.png", "Q7 — Polos e zeros")
plot_lgr(L7, "q7_lgr.png", r"Q7 — Lugar das raízes de $L(s)$")
t7b = np.linspace(0, 8, 2000)
_, y7s = ct.step_response(G7, t7b)
_, y7c = ct.step_response(T7, t7b)
plot_comp(t7b, y7s, y7c, "q7_comparacao.png", "Q7 — Com e sem controlador")

# --- Q8 ---
G8 = 3 / ((5 * s + 1) * (6 * s + 1))
C8 = (104.93 * s**2 + 95.67 * s + 100) / s
L8, T8 = C8 * G8, ct.feedback(C8 * G8, 1)
plot_degrau_verificacao(T8, "q8_degrau.png", r"Q8 — Verificação ($\zeta=0{,}43$)", tmax=10)
plot_polos_ab_fech(L8, T8, "q8_polos.png", "Q8 — Polos e zeros", 0.43)
plot_lgr(L8, "q8_lgr.png", r"Q8 — Lugar das raízes de $L(s)$")
t8 = np.linspace(0, 15, 2000)
_, y8s = ct.step_response(G8, t8)
_, y8c = ct.step_response(T8, t8)
plot_comp(t8, y8s, y8c, "q8_comparacao.png", "Q8 — Com e sem controlador")

print(f"Exportadas {len(list(FIG.glob('*.png')))} figuras em {FIG}")
