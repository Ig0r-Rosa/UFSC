#!/usr/bin/env python3
"""
Análise de dados para Laboratório de Física (UFSC): estatística de repetições,
erro aleatório, erro combinado, regressão linear por mínimos quadrados e gráfico.

Lê `Experimento Fisica.xlsx` no formato da aba tipo mola (massa + D1, D2, …)
ou pêndulo (L + t1, t2, …).
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from arredondamento_lab import arredondar_meia_acima, arredondar_valor_com_incerteza


def _fmt(x: float, dec: int = 6) -> str:
    return f"{x:.{dec}f}".rstrip("0").rstrip(".")


def _fmt_cientifica_se_muito_pequeno(z: float) -> str:
    """Mantém algarismos visíveis em resíduos², SSE, etc."""
    if z == 0:
        return "0"
    if abs(z) < 1e-4:
        return f"{z:.6e}"
    return _fmt(z)


def _celula_texto(val) -> str:
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return ""
    return str(val).strip().lower()


def encontrar_erro_regua(df: pd.DataFrame, padrao: str = "régua") -> float | None:
    lim = min(25, len(df))
    for i in range(lim):
        row = df.iloc[i]
        for j, val in enumerate(row):
            t = _celula_texto(val)
            if "erro" in t and padrao in t:
                for k in range(j + 1, len(row)):
                    x = row.iloc[k]
                    if isinstance(x, (int, float)) and not pd.isna(x):
                        return float(x)
    return None


def _linha_cabecalho_mola(df: pd.DataFrame) -> int | None:
    for i in range(len(df)):
        t = _celula_texto(df.iat[i, 0])
        if "massa" in t and "kg" in t:
            return i
    return None


def _colunas_distancia(df: pd.DataFrame, row: int) -> list[int]:
    """Primeira coluna de cada D1, D2, … (a planilha pode repetir D1 para resíduos)."""
    primeiro: dict[int, int] = {}
    for j in range(1, df.shape[1]):
        h = _celula_texto(df.iat[row, j])
        hcmp = re.sub(r"\s+", "", h)
        m = re.match(r"^d(\d)", hcmp)
        if m:
            k = int(m.group(1))
            if k not in primeiro:
                primeiro[k] = j
    return [primeiro[i] for i in sorted(primeiro)]


def carregar_bloco_mola(
    df: pd.DataFrame,
) -> tuple[np.ndarray, list[np.ndarray], list[str]]:
    h = _linha_cabecalho_mola(df)
    if h is None:
        raise ValueError("Não encontrei linha com 'massa (kg)' na primeira coluna.")
    cols_d = _colunas_distancia(df, h)
    if not cols_d:
        raise ValueError("Não encontrei colunas D1, D2, … após o cabeçalho.")
    massas: list[float] = []
    medidas: list[list[float]] = []
    for r in range(h + 1, len(df)):
        m = df.iat[r, 0]
        if not isinstance(m, (int, float)) or pd.isna(m):
            break
        linha: list[float] = []
        ok = True
        for c in cols_d:
            v = df.iat[r, c]
            if not isinstance(v, (int, float)) or pd.isna(v):
                ok = False
                break
            linha.append(float(v))
        if not ok:
            break
        massas.append(float(m))
        medidas.append(linha)
    if not massas:
        raise ValueError("Nenhuma linha numérica de dados após o cabeçalho da mola.")
    nomes = [str(df.iat[h, c]) for c in cols_d]
    return np.array(massas), [np.array(x) for x in medidas], nomes


def _linha_cabecalho_pendulo(df: pd.DataFrame) -> int | None:
    for i in range(len(df)):
        t = _celula_texto(df.iat[i, 0])
        if "l" in t and "(m)" in t and "cm" not in t:
            return i
    return None


def _colunas_tempo(df: pd.DataFrame, row: int) -> list[int]:
    primeiro: dict[int, int] = {}
    for j in range(1, df.shape[1]):
        h = _celula_texto(df.iat[row, j])
        hcmp = re.sub(r"\s+", "", h)
        m = re.match(r"^t(\d)", hcmp)
        if m:
            k = int(m.group(1))
            if k not in primeiro:
                primeiro[k] = j
    return [primeiro[i] for i in sorted(primeiro)]


def carregar_bloco_pendulo(
    df: pd.DataFrame,
) -> tuple[np.ndarray, list[np.ndarray], list[str]]:
    h = _linha_cabecalho_pendulo(df)
    if h is None:
        raise ValueError("Não encontrei linha com 'L (m)' (comprimento).")
    cols_t = _colunas_tempo(df, h)
    if not cols_t:
        raise ValueError("Não encontrei colunas t1, t2, …")
    Ls: list[float] = []
    tempos: list[list[float]] = []
    for r in range(h + 1, len(df)):
        L = df.iat[r, 0]
        if not isinstance(L, (int, float)) or pd.isna(L):
            break
        linha: list[float] = []
        ok = True
        for c in cols_t:
            v = df.iat[r, c]
            if not isinstance(v, (int, float)) or pd.isna(v):
                ok = False
                break
            linha.append(float(v))
        if not ok:
            break
        Ls.append(float(L))
        tempos.append(linha)
    if not Ls:
        raise ValueError("Nenhum dado de pêndulo após o cabeçalho.")
    nomes = [str(df.iat[h, c]) for c in cols_t]
    return np.array(Ls), [np.array(x) for x in tempos], nomes


@dataclass
class StatsRepeticao:
    valores: np.ndarray
    media: float
    desvios_quadrados: np.ndarray
    soma_sq: float
    desvio_padrao: float
    erro_aleatorio: float
    erro_escala: float
    erro_combinado: float


def estatisticas_repeticoes(
    valores: np.ndarray, erro_escala: float
) -> StatsRepeticao:
    v = np.asarray(valores, dtype=float)
    n = len(v)
    media = float(np.mean(v))
    dq = (v - media) ** 2
    soma_sq = float(np.sum(dq))
    if n < 2:
        s = 0.0
        ea = 0.0
    else:
        s = math.sqrt(soma_sq / (n - 1))
        ea = s / math.sqrt(n)
    ec = math.sqrt(ea**2 + erro_escala**2)
    return StatsRepeticao(v, media, dq, soma_sq, s, ea, erro_escala, ec)


def _fmt_sep_ndec(x: float, ndec: int | None, sep: str) -> str:
    if ndec is None:
        return _fmt(x)
    r = arredondar_meia_acima(x, ndec)
    t = f"{r:.{ndec}f}"
    return t.replace(".", sep) if sep == "," else t


def formatar_estatisticas_repeticao(
    rotulo: str,
    st: StatsRepeticao,
    nomes_col: Sequence[str] | None = None,
    ndec: int | None = None,
    sep_decimal: str = ".",
) -> str:
    """Se ndec for informado, todos os valores y seguem esse algarismo duvidoso (casas decimais)."""
    linhas: list[str] = [f"\n--- {rotulo} ---"]
    n = len(st.valores)
    fs = lambda z: _fmt_sep_ndec(z, ndec, sep_decimal)
    ym = arredondar_meia_acima(st.media, ndec) if ndec is not None else st.media
    for i, val in enumerate(st.valores):
        nome = nomes_col[i] if nomes_col and i < len(nomes_col) else f"x_{i + 1}"
        linhas.append(f"  {nome} = {fs(val)}")
    linhas.append(
        f"  Média aritmética: ȳ = ({' + '.join(fs(x) for x in st.valores)}) / {n}"
    )
    linhas.append(f"               ȳ = {fs(st.media)}")
    linhas.append("  Desvios ao quadrado (yᵢ − ȳ)²:")
    for i in range(n):
        vi, dq = st.valores[i], st.desvios_quadrados[i]
        if ndec is not None:
            vi_d, ym_d = arredondar_meia_acima(vi, ndec), ym
            dq_d = (vi_d - ym_d) ** 2
            linhas.append(
                f"    ({fs(vi)} − {fs(ym)})² = {_fmt_sep_ndec(dq_d, min(ndec * 2, 8), sep_decimal)}"
            )
        else:
            linhas.append(f"    ({fs(vi)} − {fs(st.media)})² = {fs(dq)}")
    linhas.append(f"  Σ(yᵢ − ȳ)² = {fs(st.soma_sq)}")
    ndec_s = ndec + 1 if ndec is not None else None
    if n >= 2:
        linhas.append(
            f"  Desvio padrão amostral: s = √[Σ(yᵢ − ȳ)² / (n−1)] = "
            f"√({fs(st.soma_sq)} / {n - 1}) = {_fmt_sep_ndec(st.desvio_padrao, ndec_s, sep_decimal)}"
        )
        linhas.append(
            f"  Erro aleatório da média: ε_ale = s/√n = "
            f"{_fmt_sep_ndec(st.desvio_padrao, ndec_s, sep_decimal)}/√{n} = "
            f"{_fmt_sep_ndec(st.erro_aleatorio, ndec_s, sep_decimal)}"
        )
    else:
        linhas.append("  (n < 2: desvio padrão e erro aleatório não definidos.)")
    linhas.append(f"  Erro de escala (instrumento): ε_esc = {fs(st.erro_escala)}")
    linhas.append(
        f"  Erro combinado na média: ε = √(ε_ale² + ε_esc²) = "
        f"{_fmt_sep_ndec(st.erro_combinado, ndec_s, sep_decimal)}"
    )
    return "\n".join(linhas) + "\n"


def imprimir_stats_repeticao(
    rotulo: str, st: StatsRepeticao, nomes_col: Sequence[str] | None = None
) -> None:
    print(formatar_estatisticas_repeticao(rotulo, st, nomes_col), end="")


@dataclass
class ResultadoRegressao:
    n: int
    x: np.ndarray
    y: np.ndarray
    soma_x: float
    soma_y: float
    soma_xy: float
    soma_x2: float
    delta: float
    a: float
    b: float
    sse: float
    sigma2: float
    sigma: float
    sxx: float
    delta_a: float
    delta_b: float


def regressao_minimos_quadrados(x: np.ndarray, y: np.ndarray) -> ResultadoRegressao:
    """y = a·x + b (a = angular, b = linear)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    n = len(x)
    sx, sy = float(np.sum(x)), float(np.sum(y))
    sxy = float(np.sum(x * y))
    sx2 = float(np.sum(x * x))
    delta = n * sx2 - sx**2
    if abs(delta) < 1e-30:
        raise ValueError("Δ ≈ 0: pontos em x não variam o suficiente para a reta.")
    a = (n * sxy - sx * sy) / delta
    b = (sy - a * sx) / n
    y_hat = a * x + b
    sse = float(np.sum((y - y_hat) ** 2))
    nu = max(n - 2, 1)
    sigma2 = sse / nu
    sigma = math.sqrt(sigma2)
    xm = float(np.mean(x))
    sxx = float(np.sum((x - xm) ** 2))
    if sxx < 1e-30:
        delta_a = delta_b = float("nan")
    else:
        delta_a = sigma / math.sqrt(sxx)
        delta_b = sigma * math.sqrt(1.0 / n + xm**2 / sxx)
    return ResultadoRegressao(
        n, x, y, sx, sy, sxy, sx2, delta, a, b, sse, sigma2, sigma, sxx, delta_a, delta_b
    )


def formatar_regressao(
    reg: ResultadoRegressao,
    ndec_x: int | None = None,
    ndec_y: int | None = None,
    sep_decimal: str = ".",
) -> str:
    fx = lambda z: _fmt_sep_ndec(z, ndec_x, sep_decimal)
    fy = lambda z: _fmt_sep_ndec(z, ndec_y, sep_decimal)
    ndec_p = (
        min(10, max((ndec_x or 0) + (ndec_y or 0), max(ndec_x or 0, ndec_y or 0) + 2))
        if (ndec_x is not None and ndec_y is not None)
        else None
    )
    fp = lambda z: _fmt_sep_ndec(z, ndec_p, sep_decimal)
    ndec_x2 = (ndec_x or 0) * 2 if ndec_x is not None else None
    fx2 = lambda z: _fmt_sep_ndec(z, ndec_x2, sep_decimal)
    ndec_res = (
        max((ndec_y or 0) + 2, (ndec_x or 0) + 2) if ndec_y is not None else None
    )
    fr = lambda z: _fmt_sep_ndec(z, ndec_res, sep_decimal)

    linhas: list[str] = [
        "\n=== Regressão linear (mínimos quadrados): y = a·x + b ===",
        f"n = {reg.n}",
        "Tabela auxiliar:",
        f"{'i':>3} {'xᵢ':>12} {'yᵢ':>12} {'xᵢyᵢ':>14} {'xᵢ²':>14} {'yᵢ−(a·xᵢ+b)²':>18}",
    ]
    for i in range(reg.n):
        xi, yi = reg.x[i], reg.y[i]
        if ndec_x is not None and ndec_y is not None:
            xyi = xi * yi
            x2i = xi * xi
            res2 = (yi - (reg.a * xi + reg.b)) ** 2
            res_txt = _fmt_cientifica_se_muito_pequeno(res2)
            linhas.append(
                f"{i + 1:3} {fx(xi):>12} {fy(yi):>12} {fp(xyi):>14} {fx2(x2i):>14} "
                f"{res_txt:>18}"
            )
        else:
            res2 = (yi - (reg.a * xi + reg.b)) ** 2
            linhas.append(
                f"{i + 1:3} {xi:12.6f} {yi:12.6f} {xi * yi:14.6f} {xi * xi:14.6f} "
                f"{_fmt_cientifica_se_muito_pequeno(res2):>18}"
            )
    linhas.extend(
        [
            f"Σx  = {fx(reg.soma_x) if ndec_x is not None else _fmt(reg.soma_x)}",
            f"Σy  = {fy(reg.soma_y) if ndec_y is not None else _fmt(reg.soma_y)}",
            f"Σxy = {fp(reg.soma_xy) if ndec_p is not None else _fmt(reg.soma_xy)}",
            f"Σx² = {fx2(reg.soma_x2) if ndec_x2 is not None else _fmt(reg.soma_x2)}",
        ]
    )
    fd = lambda z: _fmt_sep_ndec(z, ndec_p, sep_decimal) if ndec_p is not None else _fmt(z)
    linhas.extend(
        [
            f"Δ = n·Σx² − (Σx)² = {reg.n}·{fd(reg.soma_x2)} − ({fx(reg.soma_x) if ndec_x is not None else _fmt(reg.soma_x)})² = {fd(reg.delta)}",
            f"a = (n·Σxy − Σx·Σy) / Δ = ({reg.n}·{fp(reg.soma_xy) if ndec_p is not None else _fmt(reg.soma_xy)} − "
            f"{fx(reg.soma_x) if ndec_x is not None else _fmt(reg.soma_x)}·{fy(reg.soma_y) if ndec_y is not None else _fmt(reg.soma_y)}) / {fd(reg.delta)}",
        ]
    )
    if ndec_x is not None and ndec_y is not None and not math.isnan(reg.delta_a):
        ar, dar = arredondar_valor_com_incerteza(reg.a, reg.delta_a)
        br, dbr = arredondar_valor_com_incerteza(reg.b, reg.delta_b)
        ndeca = max(0, -int(math.floor(math.log10(abs(dar))))) if dar and dar > 0 else 6
        ndecb = max(0, -int(math.floor(math.log10(abs(dbr))))) if dbr and dbr > 0 else 6
        sa = _fmt_sep_ndec(ar, ndeca, sep_decimal)
        sda = _fmt_sep_ndec(dar, ndeca, sep_decimal)
        sb = _fmt_sep_ndec(br, ndecb, sep_decimal)
        sdb = _fmt_sep_ndec(dbr, ndecb, sep_decimal)
        linhas.extend(
            [
                f"  = {sa}",
                f"b = (Σy − a·Σx) / n = ({fy(reg.soma_y)} − {sa}·{fx(reg.soma_x)}) / {reg.n}",
                f"  = {sb}",
                f"\nReta ajustada (coef. com 1 algarismo na incerteza): y = {sa}·x + ({sb})",
                f"SSE = Σ(yᵢ − a·xᵢ − b)² = {_fmt_cientifica_se_muito_pequeno(reg.sse)}",
                f"σ² = SSE / (n−2) = {_fmt_cientifica_se_muito_pequeno(reg.sigma2)}",
                f"σ = √σ² = {_fmt_cientifica_se_muito_pequeno(reg.sigma)}",
                f"Sxx = Σ(xᵢ − x̄)² = {fx2(reg.sxx) if ndec_x2 is not None else _fmt(reg.sxx)}",
                f"Δa = σ / √Sxx = {sda}",
                f"Δb = σ·√(1/n + x̄²/Sxx) = {sdb}",
                f"a ± Δa = {sa} ± {sda}",
                f"b ± Δb = {sb} ± {sdb}",
            ]
        )
    else:
        linhas.extend(
            [
                f"  = {_fmt(reg.a)}",
                f"b = (Σy − a·Σx) / n = ({_fmt(reg.soma_y)} − {_fmt(reg.a)}·{_fmt(reg.soma_x)}) / {reg.n}",
                f"  = {_fmt(reg.b)}",
                f"\nReta ajustada: y = {_fmt(reg.a)}·x + ({_fmt(reg.b)})",
                f"SSE = Σ(yᵢ − a·xᵢ − b)² = {_fmt_cientifica_se_muito_pequeno(reg.sse)}",
                f"σ² = SSE / (n−2) = {_fmt_cientifica_se_muito_pequeno(reg.sigma2)}",
                f"σ = √σ² = {_fmt_cientifica_se_muito_pequeno(reg.sigma)}",
                f"Sxx = Σ(xᵢ − x̄)² = {_fmt(reg.sxx)}",
            ]
        )
        if not math.isnan(reg.delta_a):
            linhas.extend(
                [
                    f"Δa = σ / √Sxx = {_fmt(reg.delta_a)}",
                    f"Δb = σ·√(1/n + x̄²/Sxx) = {_fmt(reg.delta_b)}",
                    f"a ± Δa = {_fmt(reg.a)} ± {_fmt(reg.delta_a)}",
                    f"b ± Δb = {_fmt(reg.b)} ± {_fmt(reg.delta_b)}",
                ]
            )
    return "\n".join(linhas) + "\n"


def imprimir_regressao(reg: ResultadoRegressao) -> None:
    print(formatar_regressao(reg), end="")


def criar_figura_grafico_linear(
    x: np.ndarray,
    y: np.ndarray,
    err_x: np.ndarray,
    err_y: np.ndarray,
    a: float,
    b: float,
    xlabel: str,
    ylabel: str,
    titulo: str,
    legenda_dados: str = "Média ± incerteza",
):
    """Retorna (fig, ax) sem salvar nem fechar — para GUI ou uso interativo."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(
        x,
        y,
        xerr=err_x,
        yerr=err_y,
        fmt="o",
        capsize=3,
        label=legenda_dados,
    )
    xs = np.linspace(float(np.min(x)), float(np.max(x)), 100)
    ax.plot(xs, a * xs + b, "-", label=f"Ajuste: y = {_fmt(a)}·x + {_fmt(b)}")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(titulo)
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    return fig, ax


def grafico_mola(
    m: np.ndarray,
    d_media: np.ndarray,
    err_m: np.ndarray,
    err_d: np.ndarray,
    a: float,
    b: float,
    titulo: str,
    arquivo_saida: Path | None,
) -> None:
    fig, ax = criar_figura_grafico_linear(
        m,
        d_media,
        err_m,
        err_d,
        a,
        b,
        "m (kg)",
        "alongamento D (m)",
        titulo,
        "Dados (média ± incerteza)",
    )
    if arquivo_saida:
        fig.savefig(arquivo_saida, dpi=150)
        print(f"\nGráfico salvo em: {arquivo_saida}")
    else:
        plt.show()
    plt.close(fig)


def grafico_pendulo(
    L: np.ndarray,
    T2: np.ndarray,
    err_L: np.ndarray,
    err_T2: np.ndarray,
    a: float,
    b: float,
    titulo: str,
    arquivo_saida: Path | None,
) -> None:
    fig, ax = criar_figura_grafico_linear(
        L,
        T2,
        err_L,
        err_T2,
        a,
        b,
        "L (m)",
        "T² (s²)",
        titulo,
        "Dados (T² ± incerteza)",
    )
    if arquivo_saida:
        fig.savefig(arquivo_saida, dpi=150)
        print(f"\nGráfico salvo em: {arquivo_saida}")
    else:
        plt.show()
    plt.close(fig)


def processar_mola(
    df: pd.DataFrame,
    erro_dist: float,
    erro_massa: float,
    g: float,
    titulo: str,
    saida_png: Path | None,
    constante_mola: float | None,
) -> None:
    massas, medidas, nomes_d = carregar_bloco_mola(df)
    print("=" * 60)
    print("Experimento: LEI DE HOOKE (linearização x = (g/k)·m  →  y = D(m))")
    print("Variável independente: massa m (kg). Dependente: alongamento D (m).")
    print("=" * 60)
    medias: list[float] = []
    err_d: list[float] = []
    for i, (m, vals) in enumerate(zip(massas, medidas)):
        st = estatisticas_repeticoes(vals, erro_dist)
        imprimir_stats_repeticao(f"Massa m = {_fmt(m)} kg — distâncias", st, nomes_d)
        medias.append(st.media)
        err_d.append(st.erro_combinado)
    m_arr = np.array(medias)
    x = massas
    y = m_arr
    err_x = np.full_like(x, erro_massa, dtype=float)
    err_y = np.array(err_d)
    reg = regressao_minimos_quadrados(x, y)
    imprimir_regressao(reg)
    if constante_mola is not None and constante_mola > 0:
        g_est = reg.a * constante_mola
        print(
            f"\nCom constante da mola k = {constante_mola} N/m e coeficiente angular a ≈ g/k:"
        )
        print(f"  g_estimado = a·k = {_fmt(reg.a)} · {constante_mola} = {_fmt(g_est)} m/s²")
        if not math.isnan(reg.delta_a):
            dg = abs(constante_mola) * reg.delta_a
            print(f"  Propagação (k exato): Δg ≈ |k|·Δa = {_fmt(dg)} m/s²")
    print(f"\nReferência: g ≈ {g} m/s² (ajuste para comparação.)")
    grafico_mola(
        x, y, err_x, err_y, reg.a, reg.b, titulo, saida_png
    )


def processar_pendulo(
    df: pd.DataFrame,
    erro_L: float,
    erro_tempo: float,
    g: float,
    titulo: str,
    saida_png: Path | None,
) -> None:
    Ls, tempos, nomes_t = carregar_bloco_pendulo(df)
    print("=" * 60)
    print("Experimento: PÊNDULO SIMPLES — linearização T² = (4π²/g)·L")
    print("=" * 60)
    T_med: list[float] = []
    err_T: list[float] = []
    for i, (L, vals) in enumerate(zip(Ls, tempos)):
        st = estatisticas_repeticoes(vals, erro_tempo)
        imprimir_stats_repeticao(
            f"Comprimento L = {_fmt(L)} m — períodos", st, nomes_t
        )
        T_med.append(st.media)
        err_T.append(st.erro_combinado)
    Tm = np.array(T_med)
    err_T_arr = np.array(err_T)
    T2 = Tm**2
    err_T2 = 2 * Tm * err_T_arr
    print("\n--- Linearização: variável dependente T² ---")
    for i, L in enumerate(Ls):
        Tm_i, et, t2, et2 = Tm[i], err_T_arr[i], T2[i], err_T2[i]
        print(f"  L = {_fmt(L)} m:  T̄ = {_fmt(Tm_i)} s  →  T² = {_fmt(Tm_i)}² = {_fmt(t2)} s²")
        print(
            f"    Propagação (T²): Δ(T²) ≈ 2·T̄·ΔT = 2·{_fmt(Tm_i)}·{_fmt(et)} = {_fmt(et2)} s²"
        )
    x = np.asarray(Ls, dtype=float)
    y = T2
    err_x = np.full_like(x, erro_L, dtype=float)
    err_y = err_T2
    reg = regressao_minimos_quadrados(x, y)
    imprimir_regressao(reg)
    if reg.a > 0:
        g_est = 4 * math.pi**2 / reg.a
        print(f"\nPendulo: coeficiente angular a = 4π²/g  →  g = 4π²/a")
        print(f"  g_estimado = 4π² / {_fmt(reg.a)} = {_fmt(g_est)} m/s²")
        if not math.isnan(reg.delta_a) and reg.a > reg.delta_a:
            dg = 4 * math.pi**2 * reg.delta_a / (reg.a**2)
            print(f"  Δg ≈ (4π²/a²)·Δa = {_fmt(dg)} m/s²")
    print(f"\nReferência: g ≈ {g} m/s²")
    grafico_pendulo(x, y, err_x, err_y, reg.a, reg.b, titulo, saida_png)


def detectar_modo_planilha(df: pd.DataFrame) -> str:
    if _linha_cabecalho_mola(df) is not None:
        return "mola"
    if _linha_cabecalho_pendulo(df) is not None:
        return "pendulo"
    raise ValueError(
        "Não reconheci o formato: inclua bloco 'massa (kg)' + D1… ou 'L (m)' + t1…"
    )


def listar_abas(caminho: Path) -> None:
    xl = pd.ExcelFile(caminho)
    print("Abas disponíveis:")
    for n in xl.sheet_names:
        print(f"  - {n!r}")


def main(argv: Sequence[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Análise de dados — Lab. Física UFSC")
    p.add_argument(
        "--planilha",
        type=Path,
        default=Path(__file__).resolve().parent / "Experimento Fisica.xlsx",
        help="Caminho do .xlsx",
    )
    p.add_argument("--aba", type=str, default=None, help="Nome da aba (padrão: primeira)")
    p.add_argument(
        "--modo",
        choices=("auto", "mola", "pendulo"),
        default="auto",
        help="Tipo de experimento",
    )
    p.add_argument("--erro-distancia", type=float, default=None, help="ε escala distância (m)")
    p.add_argument("--erro-massa", type=float, default=0.0005, help="Incerteza em m (kg)")
    p.add_argument("--erro-L", type=float, default=0.0005, help="Incerteza em L (m)")
    p.add_argument("--erro-tempo", type=float, default=0.001, help="ε escala tempo (s)")
    p.add_argument("--g", type=float, default=9.81, help="g de referência (m/s²)")
    p.add_argument("--k-mola", type=float, default=None, help="k (N/m) para estimar g = a·k")
    p.add_argument("--titulo", type=str, default="Dados experimentais e ajuste linear")
    p.add_argument("--saida-grafico", type=Path, default=None, help="Salvar PNG do gráfico")
    p.add_argument("--listar-abas", action="store_true")
    args = p.parse_args(list(argv) if argv is not None else None)
    if not args.planilha.is_file():
        print(f"Arquivo não encontrado: {args.planilha}", file=sys.stderr)
        return 1
    if args.listar_abas:
        listar_abas(args.planilha)
        return 0
    aba = args.aba
    df = pd.read_excel(args.planilha, sheet_name=aba or 0, header=None)
    modo = args.modo
    if modo == "auto":
        modo = detectar_modo_planilha(df)
        print(f"(Modo detectado automaticamente: {modo})")
    titulo = args.titulo
    png = args.saida_grafico
    try:
        if modo == "mola":
            ed = args.erro_distancia
            if ed is None:
                ed = encontrar_erro_regua(df) or 0.0005
                print(
                    f"(Erro de escala da distância ε_esc = {ed} m; use --erro-distancia para fixar outro.)"
                )
            processar_mola(df, ed, args.erro_massa, args.g, titulo, png, args.k_mola)
        else:
            print(
                f"(Erro de escala do tempo ε_esc = {args.erro_tempo} s; use --erro-tempo para fixar outro.)"
            )
            processar_pendulo(df, args.erro_L, args.erro_tempo, args.g, titulo, png)
    except ValueError as e:
        print(f"Erro: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
