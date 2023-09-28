import csv
import os

path = 'out/os.csv'

if os.path.isfile(path) == False:
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        header = ['id', 'ds', 'solic', 'setor', 'ramal', 'dt', 'obs']
        writer.writerow(header)

class newEntry:
    def __init__(self,id,ds,solic,setor,ramal,dt,obs):
        self.id = id
        self.ds = ds
        self.solic = solic
        self.setor = setor
        self.ramal = ramal
        self.dt = dt
        self.obs = obs
    def __str__(self):
        return f'{self.id},{self.ds},{self.solic},{self.setor },{self.ramal},{self.dt},{self.obs}'

def addRow(str):
    newRow = list(str.split(','))
    print(newRow)

    with open(path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(newRow)

def listRows():
    with open(path, 'r') as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            format_row = ','.join(row)
            rows.append(format_row)
        
    return rows

def validRow(entry):
    erro = []

    if entry.solic == '':
        entry.solic = 'vllalves'
        erro.append('Solicitante não preenchido')
    if entry.setor == '':
        entry.setor = 'TI'
        erro.append('Setor não preenchido')
    if entry.ramal == '':
        entry.ramal = '10000'
        erro.append('Ramal não preenchido')
    
    entry.obs = '/'.join(erro)

def newId():
    return len(listRows())

print(newId())