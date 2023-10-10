import filemanager
from os import path
from tkinter import messagebox
from datetime import datetime

default_path = filemanager.getPath()

def relLigacoesUnid():
    ramais = []
    for line in filemanager.listRows():
        ramais.append(line.split(',')[4][1]) #pega o segundo caractere de todos os itens da coluna ramal e adiciona na lista "ramais"
    ramais.remove('a') #remove o header da coluna

    emp5 = 0
    emp6 = 0
    emp8 = 0
    outr = 0

    fpath = filemanager.getPath("LigacaoXUnid.txt")

    for n in ramais:
        if n == 2:
            emp5 = emp5+1
        if n == 5:
            emp6 = emp6+1
        if n == 8:
            emp8 = emp8+1
        else:
            outr = outr+1
    if path.isfile(fpath):
        with open(fpath, 'a') as file:
            rel = f'\nData: {datetime.now()}\n\nEmpr.5: {emp5}\nEmpr.6: {emp6}\nEmpr.8: {emp8}\nOutros: {outr}\n'
            file.write(rel)
    else:
        with open(fpath, 'w') as file:
            rel = f'Relatório de ligações por unidade\nData: {datetime.now()}\n\nEmpr.5: {emp5}\nEmpr.6: {emp6}\nEmpr.8: {emp8}\nOutros: {outr}\n'
            file.write(rel)

    messagebox.showinfo(title='Registro interno', message=f'Relaório criado:\n"{fpath}"')