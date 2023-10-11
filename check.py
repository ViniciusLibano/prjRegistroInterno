import filemanager
from tkinter import *
from tkinter import ttk

rows=[]
for i in filemanager.listRows():
    rows.append(list(i.split(',')))

class Table:
    def __init__(self, root, list):
        for j in range(len(list)): #pra cada linha
            for i in range(len(list[0])):
                self.e = ttk.Label(root, text=list[j][i-1], width=9, foreground='black', font=('Arial', 10))
                self.e.grid(row=j, column=i)
                self.c = ttk.Checkbutton(root, text='Registrado?')
                self.c.grid(row=j, column=len(list[0]))

root = Tk()
root.title('Anotações')
root.resizable(False, False)

t = Table(root, rows)

root.mainloop()