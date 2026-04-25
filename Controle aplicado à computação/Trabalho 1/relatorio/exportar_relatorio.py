#!/usr/bin/env python3
"""
Exporta figuras (PNG) e saídas de texto (stdout) dos notebooks .ipynb.

Objetivo:
- Extrair automaticamente as figuras geradas nos notebooks (outputs image/png).
- Extrair os blocos de texto impressos (stdout) para uso no relatório LaTeX.

Saídas:
- relatorio/figs/<notebook>_figNN.png
- relatorio/outputs.json (estrutura com título inferido, textos e figuras)
"""

from __future__ import annotations

import base64
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
FIGS_DIR = ROOT / "relatorio" / "figs"
OUTPUT_JSON = ROOT / "relatorio" / "outputs.json"


PC_TITLE_RE = re.compile(r"(PC\d+\.\d+[^\n\"]*)", re.IGNORECASE)
PROBLEMA_RE = re.compile(r"(PROBLEMA\s+PC\d+\.\d+[^\n\"]*)", re.IGNORECASE)


def _clean_text(text: str) -> str:
    text = text.replace("\r", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _infer_title(nb: Dict[str, Any], fallback: str) -> str:
    joined = "".join("".join(c.get("source", [])) for c in nb.get("cells", []))
    m = PC_TITLE_RE.search(joined) or PROBLEMA_RE.search(joined)
    if m:
        return _clean_text(m.group(1))
    return fallback


def _iter_outputs(nb: Dict[str, Any]):
    for cell in nb.get("cells", []):
        for out in cell.get("outputs", []) or []:
            yield out


def _extract_stdout(nb: Dict[str, Any]) -> List[str]:
    blocks: List[str] = []
    for out in _iter_outputs(nb):
        if out.get("output_type") == "stream" and out.get("name") == "stdout":
            txt = _clean_text("".join(out.get("text", [])))
            if txt:
                blocks.append(txt)
    return blocks


def _extract_pngs(nb: Dict[str, Any], base_name: str) -> List[str]:
    FIGS_DIR.mkdir(parents=True, exist_ok=True)
    saved: List[str] = []
    idx = 1
    for out in _iter_outputs(nb):
        data = out.get("data") or {}
        b64 = data.get("image/png")
        if not b64:
            continue
        if isinstance(b64, list):
            b64 = "".join(b64)
        try:
            raw = base64.b64decode(b64)
        except Exception:
            continue
        out_path = FIGS_DIR / f"{base_name}_fig{idx:02d}.png"
        out_path.write_bytes(raw)
        saved.append(str(out_path.relative_to(ROOT)))
        idx += 1
    return saved


def main() -> int:
    ipynbs = sorted(ROOT.glob("*.ipynb"), key=lambda p: p.name)
    results: List[Dict[str, Any]] = []

    for p in ipynbs:
        nb = json.loads(p.read_text(encoding="utf-8"))
        fallback = f"PC{p.stem}"
        title = _infer_title(nb, fallback=fallback)
        stdout_blocks = _extract_stdout(nb)
        figs = _extract_pngs(nb, base_name=p.stem.replace(".", "_"))

        results.append(
            {
                "notebook": p.name,
                "title": title,
                "stdout_blocks": stdout_blocks,
                "figures": figs,
            }
        )

    OUTPUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Export concluído: {len(results)} notebooks")
    print(f"- JSON: {OUTPUT_JSON.relative_to(ROOT)}")
    print(f"- Figuras: {FIGS_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

