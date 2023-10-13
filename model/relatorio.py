from dal import filemanager
from os import path
from tkinter import messagebox
from datetime import datetime

default_path = filemanager.getPath()

def relLigacaoXUnid():
    ramais = []
    for line in filemanager.listRows():
        ramais.append(list(line.split(','))[4][1])
    ramais.remove('a')

    emp5 = 0
    emp6 = 0
    emp8 = 0
    outr = 0

    for n in ramais:
        if n == '2':
            emp5 = emp5+1
        elif n == '5':
            emp6 = emp6+1
        elif n == '1':
            emp8 = emp8+1
        else:
            outr = outr+1

    hora = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    fpath = filemanager.getPath("LigacaoXUnid.txt")    
    if path.isfile(fpath):
        with open(fpath, 'a') as file:
            rel = f'\nData: {hora}\n\nEmpr.5: {emp5}\nEmpr.6: {emp6}\nEmpr.8: {emp8}\nOutros: {outr}\n'
            file.write(rel)
    else:
        with open(fpath, 'w') as file:
            rel = f'Relatório de ligações por unidade\nData: {hora}\n\nEmpr.5: {emp5}\nEmpr.6: {emp6}\nEmpr.8: {emp8}\nOutros: {outr}\n'
            file.write(rel)

    messagebox.showinfo(title='Registro interno', message=f'Relaório criado:\n"{fpath}"')