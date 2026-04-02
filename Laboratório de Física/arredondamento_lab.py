"""
Arredondamento para laboratório: algarismo duvidoso a partir das casas
decimais escritas nas medições; meia unidade para cima (ABNT / prática usual).
"""

from __future__ import annotations

import math
import re
from decimal import ROUND_HALF_UP, Decimal


def casas_decimais_string(s: str) -> int:
    """Número de casas após a vírgula/ponto conforme o texto colado (ex.: 0,0088 → 4)."""
    t = s.strip().replace("\xa0", "").replace(" ", "")
    t = t.replace(",", ".")
    if re.search(r"[eE]", t):
        return 0
    if "." not in t:
        return 0
    parte = t.split(".", 1)[1]
    return len(parte)


def arredondar_meia_acima(valor: float, ndec: int) -> float:
    if ndec < 0:
        ndec = 0
    if ndec == 0:
        q = Decimal("1")
    else:
        q = Decimal(10) ** -ndec
    d = Decimal(str(float(valor))).quantize(q, rounding=ROUND_HALF_UP)
    return float(d)


def precisao_minima_linha(celulas: list[str]) -> int:
    """A medida menos precisa (menor nº de casas decimais) fixa o algarismo duvidoso da linha."""
    if not celulas:
        return 0
    return min(casas_decimais_string(c) for c in celulas if c.strip())


def precisao_global_linhas(listas: list[list[str]]) -> int:
    return min(precisao_minima_linha(L) for L in listas) if listas else 0


def arredondar_incerteza_um_algarismo(delta: float) -> float:
    if delta <= 0 or math.isnan(delta) or math.isinf(delta):
        return delta
    exp = math.floor(math.log10(abs(delta)))
    base = 10**exp
    return round(delta / base) * base


def arredondar_valor_com_incerteza(valor: float, delta: float) -> tuple[float, float]:
    """
    Incerteza com um algarismo significativo; valor alinhado à última casa da incerteza.
    Retorna (valor_arredondado, delta_arredondada).
    """
    if delta <= 0 or math.isnan(delta) or math.isinf(delta):
        return valor, delta
    du = arredondar_incerteza_um_algarismo(delta)
    if du == 0:
        return valor, du
    exp = math.floor(math.log10(abs(du)))
    ndec = max(0, -exp)
    q = Decimal(10) ** -ndec if ndec > 0 else Decimal("1")
    v = Decimal(str(float(valor))).quantize(q, rounding=ROUND_HALF_UP)
    d = Decimal(str(float(du))).quantize(q, rounding=ROUND_HALF_UP)
    return float(v), float(d)


def formatar_valor_ndec(x: float, ndec: int) -> str:
    if ndec < 0:
        ndec = 0
    r = arredondar_meia_acima(x, ndec)
    return f"{r:.{ndec}f}".replace(".", ",")


def formatar_float_gui(x: float, ndec: int | None) -> str:
    if ndec is None:
        s = f"{x:.10g}"
        return s.replace(".", ",")
    return formatar_valor_ndec(x, ndec)
