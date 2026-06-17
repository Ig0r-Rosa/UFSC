#!/bin/bash
# Compila os PDFs da versão para iniciantes (leigos).
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/../Conteudo"

for i in 1 2 3 4; do
  echo "=== Compilando Parte $i ==="
  pandoc "$DIR/Slides-P4-Parte${i}-Conteudo-Leigo.md" \
    -o "$OUT/Slides-P4-Parte${i}-Conteudo-Leigo.pdf" \
    --pdf-engine=pdflatex \
    -V geometry:margin=2.5cm \
    -V documentclass=article \
    -V fontsize=11pt \
    --toc \
    --toc-depth=2 \
    -N
  pdfinfo "$OUT/Slides-P4-Parte${i}-Conteudo-Leigo.pdf" | grep -E "Pages|File size"
done

echo "Concluído."
