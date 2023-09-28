import filemngr
from tkinter import *
from tkinter import ttk
from datetime import datetime

def cleanForm():
    entDesc.delete(0, END)
    entSolic.delete(0, END)
    entSetor.delete(0, END)
    entRamal.delete(0, END)

def btnSalvarListener():
    now = datetime.now().strftime('%d-%m-%y %H:%M')
    newRow = filemngr.newEntry(filemngr.newId(),entDesc.get(),entSolic.get(),entSetor.get(),entRamal.get(), now, ' ')
    filemngr.validRow(newRow)
    print(newRow)
    filemngr.addRow(f'{newRow}')
    cleanForm()

root = Tk()
root.title('Anotação de OS')
root.resizable(False, False)

frm = ttk.Frame(root, borderwidth=5, padding=5, relief="ridge", width=200, height=100)
frm.pack()

lblSolic = ttk.Label(frm, text='Solicitante')
lblSolic.grid(row=0, column=0)
lblSetor = ttk.Label(frm, text='Setor')
lblSetor.grid(row=2, column=0)
lblRamal = ttk.Label(frm, text='Ramal')
lblRamal.grid(row=2, column=1)
lblDesc = ttk.Label(frm, text='Descrição')
lblDesc.grid(row=4, column=0)

entSolic = ttk.Entry(frm)
entSolic.grid(row=1, column=0, columnspan=2)
entSetor = ttk.Entry(frm)
entSetor.grid(row=3, column=0)
entRamal = ttk.Entry(frm)
entRamal.grid(row=3, column=1)
entDesc = ttk.Entry(frm, )
entDesc.grid(row=5, column=0, columnspan=2)

for w in frm.winfo_children():
    w.grid_configure(padx=5, sticky='news')

btnSalvar = ttk.Button(frm, text='Salvar', command=btnSalvarListener)
btnSalvar.grid(row=8, column=1, sticky='e', pady=[10,0])

root.mainloop()