from tkinter import *
from tkinter import ttk

from dal import filemanager

class Tabela():
    def __init__(self, root, rows: list):
        self.n_linhas = len(rows)
        self.n_colunas = len(list(rows[0].split(',')))

        for l in range(self.n_linhas):
            linha = list(rows[l].split(','))
            for c in range(self.n_colunas):
                self.t = Text(root, width=10, height=1)
                self.t.grid(row=l, column=c)
                self.t.insert(INSERT, linha[c])
                self.t.config(state=DISABLED)

def run():
    root = Tk()
    root.title('Anotações')
    root.resizable(False,False)
    tabelaFrame = ttk.Frame(height=300, width=500, borderwidth=1, relief=GROOVE)
    tabelaFrame.pack(padx=10, pady=10)

    optionFrame = ttk.Frame(height=100, width=500, borderwidth=1, relief=GROOVE)
    optionFrame.pack(padx=10, pady=[0,10])

    tabela = Tabela(tabelaFrame, filemanager.listRows())

    root.mainloop()