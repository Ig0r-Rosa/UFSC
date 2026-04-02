#!/usr/bin/env python3
"""
Interface visual: abas (dados, tabela, cálculos, gráfico) e colagem estilo Excel.
Cálculos e tabela de regressão com precisão numérica completa (sem arredondar dados).
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import re
import tkinter as tk
from tkinter import messagebox, ttk

import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

plt.ioff()
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from analise_relatorio_fisica import (
    _fmt,
    criar_figura_grafico_linear,
    estatisticas_repeticoes,
    formatar_estatisticas_repeticao,
    formatar_regressao,
    regressao_minimos_quadrados,
)


def _para_float(celula: str) -> float:
    s = celula.strip().replace("\xa0", " ").strip()
    s = s.replace(" ", "").replace(",", ".")
    return float(s)


def _e_numero(s: str) -> bool:
    if not s.strip():
        return False
    try:
        _para_float(s)
        return True
    except ValueError:
        return False


def parsear_dados_colados(texto: str) -> tuple[list[str], np.ndarray, list[np.ndarray]]:
    """Cabeçalhos, coluna referência (x) e listas de medidas por linha."""
    linhas = [ln.rstrip("\r") for ln in texto.splitlines() if ln.strip()]
    if not linhas:
        raise ValueError("Cole pelo menos uma linha de dados.")
    tabela: list[list[str]] = []
    for ln in linhas:
        if "\t" in ln:
            celulas = [c.strip() for c in ln.split("\t")]
        else:
            partes = re.split(r"\s{2,}", ln.strip())
            if len(partes) > 1:
                celulas = [p.strip() for p in partes]
            else:
                celulas = [p.strip() for p in ln.split()]
        tabela.append(celulas)
    largura = max(len(r) for r in tabela)
    tabela = [r + [""] * (largura - len(r)) for r in tabela]
    primeira = tabela[0]
    if largura < 2:
        raise ValueError("São necessárias pelo menos 2 colunas (referência + medidas).")
    if all(_e_numero(c) for c in primeira):
        cab = ["Referência"] + [f"Medida{i}" for i in range(1, largura)]
        ini = 0
    else:
        cab = [c if c else f"Col{i}" for i, c in enumerate(primeira)]
        ini = 1
    xs: list[float] = []
    blocos: list[np.ndarray] = []
    for idx, lin in enumerate(tabela[ini:], start=ini + 1):
        if not any(lin):
            continue
        if any(not lin[i].strip() for i in range(largura)):
            raise ValueError(f"Linha {idx}: célula vazia.")
        try:
            nums = [_para_float(c) for c in lin[:largura]]
        except ValueError as e:
            raise ValueError(f"Linha {idx}: valor não numérico ({e}).") from e
        xs.append(nums[0])
        blocos.append(np.array(nums[1:], dtype=float))
    if len(xs) < 2:
        raise ValueError("Inclua pelo menos 2 linhas de medições numéricas.")
    return cab, np.array(xs, dtype=float), blocos


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Laboratório de Física — análise de dados")
        self.minsize(960, 720)
        self.configure(bg="#e8eef2")
        self._reg = None
        self._grafico_state: dict | None = None
        self._fig_grafico_aberto = None
        self._canvas_grafico = None
        self._toolbar_grafico = None
        self._config_estilo()
        self._montar_ui()
        self.protocol("WM_DELETE_WINDOW", self._ao_fechar)

    def _ao_fechar(self) -> None:
        """Encerra o Tk e libera o matplotlib (evita terminal preso após fechar a janela)."""
        try:
            for w in list(self.frame_graf_placeholder.winfo_children()):
                try:
                    w.destroy()
                except tk.TclError:
                    pass
        except tk.TclError:
            pass
        self._fig_grafico_aberto = None
        self._canvas_grafico = None
        self._toolbar_grafico = None
        try:
            plt.close("all")
        except Exception:
            pass
        self.quit()
        self.destroy()

    def _config_estilo(self) -> None:
        s = ttk.Style()
        try:
            s.theme_use("clam")
        except tk.TclError:
            pass
        bg = "#e8eef2"
        s.configure("TFrame", background=bg)
        s.configure("TLabelframe", background=bg)
        s.configure("TLabelframe.Label", background=bg, font=("Segoe UI", 10, "bold"))
        s.configure("TNotebook", background=bg, tabmargins=[4, 4, 0, 0])
        s.configure("TNotebook.Tab", padding=[14, 6], font=("Segoe UI", 10))
        s.map("TNotebook.Tab", background=[("selected", "#ffffff"), ("!selected", "#d0dae0")])
        s.configure("Excel.Treeview", rowheight=24, font=("Consolas", 10), fieldbackground="#ffffff")
        s.configure(
            "Excel.Treeview.Heading",
            font=("Segoe UI", 9, "bold"),
            background="#217346",
            foreground="white",
        )
        s.map("Excel.Treeview.Heading", background=[("active", "#1a5c38")])
        s.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))

    def _montar_ui(self) -> None:
        topo = tk.Frame(self, bg="#1a5c38", height=56)
        topo.pack(fill=tk.X)
        topo.pack_propagate(False)
        tk.Label(
            topo,
            text="Laboratório de Física",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#1a5c38",
        ).pack(side=tk.LEFT, padx=20, pady=12)
        tk.Label(
            topo,
            text="Análise genérica · mínimos quadrados · algarismo duvidoso",
            font=("Segoe UI", 10),
            fg="#c8e6d0",
            bg="#1a5c38",
        ).pack(side=tk.LEFT, pady=12)

        nb = ttk.Notebook(self)
        nb.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))

        tab_dados = ttk.Frame(nb)
        tab_tabela = ttk.Frame(nb)
        tab_contas = ttk.Frame(nb)
        tab_graf = ttk.Frame(nb)
        nb.add(tab_dados, text="  Dados  ")
        nb.add(tab_tabela, text="  Tabela  ")
        nb.add(tab_contas, text="  Cálculos  ")
        nb.add(tab_graf, text="  Gráfico  ")
        self._notebook = nb

        self._montar_aba_dados(tab_dados)
        self._montar_aba_tabela(tab_tabela)
        self._montar_aba_contas(tab_contas)
        self._montar_aba_grafico(tab_graf)

    def _montar_aba_dados(self, parent: ttk.Frame) -> None:
        wrap = ttk.LabelFrame(parent, text="Área de colagem (Tab = coluna, como no Excel)")
        wrap.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        inner = ttk.Frame(wrap)
        inner.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)
        self.txt_dados = tk.Text(
            inner,
            height=12,
            wrap=tk.NONE,
            font=("Consolas", 11),
            bg="#ffffff",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#c5d4dc",
            padx=10,
            pady=10,
        )
        sy = ttk.Scrollbar(inner, orient=tk.VERTICAL, command=self.txt_dados.yview)
        sx = ttk.Scrollbar(inner, orient=tk.HORIZONTAL, command=self.txt_dados.xview)
        self.txt_dados.configure(yscrollcommand=sy.set, xscrollcommand=sx.set)
        self.txt_dados.grid(row=0, column=0, sticky="nsew")
        sy.grid(row=0, column=1, sticky="ns")
        sx.grid(row=1, column=0, sticky="ew")
        inner.rowconfigure(0, weight=1)
        inner.columnconfigure(0, weight=1)

        hint = ttk.Label(
            wrap,
            text="Primeira coluna = referência (x). Demais = repetições da mesma grandeza (y). "
            "A última casa decimal escrita define o algarismo duvidoso.",
            font=("Segoe UI", 9),
            foreground="#555",
        )
        hint.pack(anchor=tk.W, padx=8, pady=(0, 6))

        par = ttk.LabelFrame(parent, text="Parâmetros")
        par.pack(fill=tk.X, padx=10, pady=(0, 10))
        g1 = ttk.Frame(par)
        g1.pack(fill=tk.X, padx=8, pady=8)
        ttk.Label(g1, text="ε nas medidas (y):").grid(row=0, column=0, sticky=tk.W, padx=4)
        self.var_erro_y = tk.StringVar(value="0.0005")
        ttk.Entry(g1, textvariable=self.var_erro_y, width=12).grid(row=0, column=1, padx=4)
        ttk.Label(g1, text="ε na referência (x):").grid(row=0, column=2, sticky=tk.W, padx=12)
        self.var_erro_x = tk.StringVar(value="0.0005")
        ttk.Entry(g1, textvariable=self.var_erro_x, width=12).grid(row=0, column=3, padx=4)
        ttk.Label(g1, text="Eixo X:").grid(row=1, column=0, sticky=tk.W, padx=4, pady=4)
        self.var_lbl_x = tk.StringVar(value="m (kg)")
        ttk.Entry(g1, textvariable=self.var_lbl_x, width=18).grid(row=1, column=1, padx=4)
        ttk.Label(g1, text="Eixo Y:").grid(row=1, column=2, sticky=tk.W, padx=12)
        self.var_lbl_y = tk.StringVar(value="alongamento (m)")
        ttk.Entry(g1, textvariable=self.var_lbl_y, width=18).grid(row=1, column=3, padx=4)
        ttk.Label(g1, text="Título:").grid(row=2, column=0, sticky=tk.W, padx=4)
        self.var_titulo = tk.StringVar(value="Dados experimentais e ajuste linear")
        ttk.Entry(g1, textvariable=self.var_titulo, width=52).grid(row=2, column=1, columnspan=3, padx=4)

        bar = ttk.Frame(parent)
        bar.pack(fill=tk.X, padx=10, pady=6)
        ttk.Button(bar, text="Processar tudo", style="Accent.TButton", command=self._processar).pack(
            side=tk.LEFT, padx=4
        )
        ttk.Button(bar, text="Limpar", command=self._limpar).pack(side=tk.LEFT, padx=4)
        ttk.Button(bar, text="Exemplo", command=self._inserir_exemplo).pack(side=tk.LEFT, padx=4)

        self._inserir_exemplo()

    def _montar_aba_tabela(self, parent: ttk.Frame) -> None:
        wrap = ttk.LabelFrame(parent, text="Valores colados e médias ȳ (já com arredondamento exibido)")
        wrap.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tree = ttk.Treeview(wrap, show="headings", style="Excel.Treeview", height=14)
        sy = ttk.Scrollbar(wrap, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=sy.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=4, pady=4)
        sy.pack(side=tk.RIGHT, fill=tk.Y, pady=4)

    def _montar_aba_contas(self, parent: ttk.Frame) -> None:
        wrap = ttk.LabelFrame(parent, text="Passo a passo")
        wrap.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.txt_contas = tk.Text(
            wrap,
            wrap=tk.WORD,
            font=("Consolas", 10),
            bg="#fafafa",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#c5d4dc",
            padx=12,
            pady=12,
        )
        sy = ttk.Scrollbar(wrap, orient=tk.VERTICAL, command=self.txt_contas.yview)
        self.txt_contas.configure(yscrollcommand=sy.set)
        self.txt_contas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=4, pady=4)
        sy.pack(side=tk.RIGHT, fill=tk.Y, pady=4)

    def _montar_aba_grafico(self, parent: ttk.Frame) -> None:
        self.frame_graf_placeholder = ttk.Frame(parent)
        self.frame_graf_placeholder.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.lbl_graf_info = ttk.Label(
            self.frame_graf_placeholder,
            text="Processe os dados na aba «Dados», depois use o botão abaixo.",
            font=("Segoe UI", 11),
        )
        self.lbl_graf_info.pack(expand=True)
        bar_g = ttk.Frame(parent)
        bar_g.pack(pady=10)
        ttk.Button(
            bar_g,
            text="Atualizar o gráfico",
            style="Accent.TButton",
            command=self._atualizar_grafico_na_aba,
        ).pack()

    def _inserir_exemplo(self) -> None:
        self.txt_dados.delete("1.0", tk.END)
        ex = (
            "Referência\tMedida1\tMedida2\tMedida3\n"
            "0,020\t0,0080\t0,0080\t0,0088\n"
            "0,030\t0,0145\t0,0140\t0,0145\n"
            "0,040\t0,0185\t0,0190\t0,0190\n"
            "0,050\t0,0250\t0,0250\t0,0235\n"
            "0,060\t0,0298\t0,0290\t0,0285\n"
        )
        self.txt_dados.insert("1.0", ex)

    def _limpar(self) -> None:
        self.txt_dados.delete("1.0", tk.END)
        self._limpar_tree()
        self.txt_contas.delete("1.0", tk.END)
        self._reg = None
        self._grafico_state = None
        self._limpar_grafico_aba()

    def _limpar_tree(self) -> None:
        self.tree.delete(*self.tree.get_children())
        for c in self.tree["columns"]:
            self.tree.heading(c, text="")
        self.tree["columns"] = ()

    def _limpar_grafico_aba(self) -> None:
        if self._fig_grafico_aberto is not None:
            plt.close(self._fig_grafico_aberto)
            self._fig_grafico_aberto = None
        for w in self.frame_graf_placeholder.winfo_children():
            w.destroy()
        self.lbl_graf_info = ttk.Label(
            self.frame_graf_placeholder,
            text="Processe os dados na aba «Dados», depois use «Atualizar o gráfico».",
            font=("Segoe UI", 11),
        )
        self.lbl_graf_info.pack(expand=True)
        self._canvas_grafico = None
        self._toolbar_grafico = None

    def _preencher_tree(
        self,
        cab: list[str],
        xs: np.ndarray,
        medidas: list[np.ndarray],
    ) -> None:
        self._limpar_tree()
        cols = list(cab) + ["ȳ"]
        self.tree["columns"] = cols
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=100, anchor=tk.CENTER)
        for i, x in enumerate(xs):
            m = medidas[i]
            media = float(np.mean(m))
            linha = [f"{float(x):g}"] + [f"{float(v):g}" for v in m] + [f"{media:g}"]
            self.tree.insert("", tk.END, values=linha)

    def _ler_erros(self) -> tuple[float, float]:
        try:
            ey = float(self.var_erro_y.get().replace(",", "."))
            ex = float(self.var_erro_x.get().replace(",", "."))
        except ValueError as e:
            raise ValueError("ε nas medidas e ε na referência precisam ser números.") from e
        if ey < 0 or ex < 0:
            raise ValueError("Incertezas não podem ser negativas.")
        return ey, ex

    def _processar(self) -> None:
        texto = self.txt_dados.get("1.0", tk.END)
        try:
            ey, ex = self._ler_erros()
            cab, xs, medidas = parsear_dados_colados(texto)
        except ValueError as e:
            messagebox.showerror("Dados inválidos", str(e))
            return

        partes: list[str] = [
            "═" * 58,
            "Modelo: x = 1ª coluna (referência); y = médias das demais colunas.",
            "Estatística: desvio padrão, erro aleatório e erro combinado por linha.",
            "Regressão linear: y = a·x + b (mínimos quadrados) sobre (x, ȳ) sem arredondar os dados.",
            "═" * 58,
            "",
        ]

        y_med: list[float] = []
        err_y: list[float] = []
        nomes_rep = cab[1:] if len(cab) > 1 else None

        for i, (xv, vals) in enumerate(zip(xs, medidas)):
            st = estatisticas_repeticoes(vals, ey)
            rot = f"x = {_fmt(xv)} — repetições ({cab[1] if len(cab) > 1 else 'medidas'})"
            partes.append(formatar_estatisticas_repeticao(rot, st, nomes_rep))
            y_med.append(st.media)
            err_y.append(st.erro_combinado)

        x_arr = np.asarray(xs, dtype=float)
        y_arr = np.array(y_med, dtype=float)
        err_x = np.full_like(x_arr, ex, dtype=float)
        err_y_arr = np.array(err_y, dtype=float)

        try:
            reg = regressao_minimos_quadrados(x_arr, y_arr)
        except ValueError as e:
            messagebox.showerror("Regressão", str(e))
            return

        self._reg = reg
        partes.append(formatar_regressao(reg))

        self.txt_contas.delete("1.0", tk.END)
        self.txt_contas.insert("1.0", "\n".join(partes))
        self._preencher_tree(cab, xs, medidas)
\
        self._grafico_state = {
            "x": x_arr,
            "y": y_arr,
            "ex": err_x,
            "ey": err_y_arr,
            "a": reg.a,
            "b": reg.b,
            "xlabel": self.var_lbl_x.get().strip() or "x",
            "ylabel": self.var_lbl_y.get().strip() or "y",
            "titulo": self.var_titulo.get().strip() or "Gráfico",
        }
        self._notebook.select(1)

    def _atualizar_grafico_na_aba(self) -> None:
        if not self._grafico_state:
            messagebox.showinfo("Gráfico", "Processe os dados primeiro (aba Dados).")
            return
        st = self._grafico_state
        if self._fig_grafico_aberto is not None:
            plt.close(self._fig_grafico_aberto)
            self._fig_grafico_aberto = None
        for w in self.frame_graf_placeholder.winfo_children():
            w.destroy()

        fig, _ = criar_figura_grafico_linear(
            st["x"],
            st["y"],
            st["ex"],
            st["ey"],
            st["a"],
            st["b"],
            st["xlabel"],
            st["ylabel"],
            st["titulo"],
        )
        self._fig_grafico_aberto = fig
        canvas = FigureCanvasTkAgg(fig, master=self.frame_graf_placeholder)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        bar = ttk.Frame(self.frame_graf_placeholder)
        bar.pack(side=tk.BOTTOM, fill=tk.X)
        NavigationToolbar2Tk(canvas, bar)
        self._canvas_grafico = canvas
        self._toolbar_grafico = bar
        self._notebook.select(3)


def main() -> None:
    app = App()
    try:
        app.mainloop()
    finally:
        try:
            plt.close("all")
        except Exception:
            pass


if __name__ == "__main__":
    main()
