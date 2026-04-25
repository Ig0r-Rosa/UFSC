#!/usr/bin/env python3
"""
Gera um relatório LaTeX a partir de `relatorio/outputs.json`.

Critérios:
- Documento organizado, contendo apenas as respostas/resultados (texto e figuras).
- Seções por problema (PCx.y), conforme inferido dos notebooks.
- Inclui as figuras exportadas em `relatorio/figs/`.
"""

from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "relatorio" / "outputs.json"
TEX_OUT = ROOT / "relatorio" / "relatorio.tex"


def _latex_escape(s: str) -> str:
    # Escapa apenas o necessário (texto comum). Saídas longas entram em listings.
    return (
        s.replace("\\", "\\textbackslash{}")
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("#", "\\#")
        .replace("_", "\\_")
        .replace("{", "\\{")
        .replace("}", "\\}")
        .replace("~", "\\textasciitilde{}")
        .replace("^", "\\textasciicircum{}")
    )


def _select_stdout_blocks(blocks: List[str], max_blocks: int = 3, max_chars: int = 3500) -> str:
    """
    Seleciona os últimos blocos (normalmente o 'resultado final') e limita tamanho.
    """
    if not blocks:
        return ""
    sel = blocks[-max_blocks:]
    txt = "\n\n".join(sel).strip()
    if len(txt) > max_chars:
        txt = txt[: max_chars - 200].rstrip() + "\n...\n(continuação omitida por brevidade)"
    return txt


def _problem_key(title: str, notebook: str) -> str:
    # Ordenação: tenta PCx.y; senão usa o nome do arquivo.
    m = re.search(r"PC(\d+)\.(\d+)", title, flags=re.IGNORECASE)
    if m:
        return f"{int(m.group(1)):02d}.{int(m.group(2)):03d}"
    m2 = re.search(r"(\d+)\.(\d+)\.ipynb$", notebook)
    if m2:
        return f"{int(m2.group(1)):02d}.{int(m2.group(2)):03d}"
    return notebook


def main() -> int:
    data = json.loads(OUTPUTS.read_text(encoding="utf-8"))
    data.sort(key=lambda x: _problem_key(x.get("title", ""), x.get("notebook", "")))

    today = _dt.date.today().strftime("%d/%m/%Y")

    parts: List[str] = []
    parts.append(r"\documentclass[12pt,a4paper]{article}")
    parts.append(r"\usepackage[utf8]{inputenc}")
    parts.append(r"\usepackage[T1]{fontenc}")
    parts.append(r"\usepackage[brazil]{babel}")
    parts.append(r"\usepackage[a4paper,margin=2.5cm]{geometry}")
    parts.append(r"\usepackage{graphicx}")
    parts.append(r"\usepackage{float}")
    parts.append(r"\usepackage{hyperref}")
    parts.append(r"\usepackage{xcolor}")
    parts.append(r"\usepackage{listings}")
    parts.append(r"\lstset{")
    parts.append(r"  basicstyle=\ttfamily\small,")
    parts.append(r"  breaklines=true,")
    parts.append(r"  columns=fullflexible,")
    parts.append(r"  frame=single,")
    parts.append(r"  framerule=0.4pt,")
    parts.append(r"  rulecolor=\color{black!30},")
    parts.append(r"  xleftmargin=0.8em,")
    parts.append(r"  xrightmargin=0.8em,")
    parts.append(r"}")
    parts.append("")

    parts.append(r"\title{Trabalho 1: Desempenho de Sistemas de Controle e Projetos}")
    parts.append(r"\author{Igor de Matos da Rosa \\ Matrícula: 20103930 \\ Universidade Federal de Santa Catarina \\ Disciplina: Controle Aplicado à Computação}")
    parts.append(rf"\date{{{today}}}")
    parts.append("")
    parts.append(r"\begin{document}")
    parts.append(r"\maketitle")
    parts.append(r"\thispagestyle{empty}")
    parts.append(r"\vspace{0.5cm}")
    parts.append(r"\noindent\textbf{Observação:} Este relatório contém apenas as respostas/resultados (texto e gráficos) obtidos via execução em Python, conforme notebooks fornecidos.")
    parts.append(r"\vspace{0.8cm}")

    for item in data:
        title = item.get("title") or item.get("notebook", "Problema")
        notebook = item.get("notebook", "")
        stdout_blocks = item.get("stdout_blocks", []) or []
        figs = item.get("figures", []) or []

        parts.append("")
        parts.append(r"\clearpage")
        parts.append(rf"\section*{{{_latex_escape(title)}}}")
        if notebook:
            parts.append(rf"\noindent\textit{{Fonte:}} {_latex_escape(notebook)}")
            parts.append(r"\vspace{0.4cm}")

        selected = _select_stdout_blocks(stdout_blocks, max_blocks=3)
        if selected:
            parts.append(r"\subsection*{Resultados (saída do código)}")
            parts.append(r"\begin{lstlisting}")
            parts.append(selected)
            parts.append(r"\end{lstlisting}")

        if figs:
            parts.append(r"\subsection*{Gráficos}")
            for i, rel in enumerate(figs, start=1):
                # Caminho relativo ao .tex (relatorio/relatorio.tex -> figuras em relatorio/figs)
                fig_path = Path(rel).name
                parts.append(r"\begin{figure}[H]")
                parts.append(r"\centering")
                parts.append(rf"\includegraphics[width=0.95\linewidth]{{figs/{_latex_escape(fig_path)}}}")
                parts.append(rf"\caption{{{_latex_escape(title)} -- Figura {i}.}}")
                parts.append(r"\end{figure}")

        if not selected and not figs:
            parts.append(r"\textit{Nenhuma saída/figura registrada no notebook para este item.}")

    parts.append("")
    parts.append(r"\end{document}")

    TEX_OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"Gerado: {TEX_OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

