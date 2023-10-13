import os
import csv
import shutil
from datetime import datetime

default_path = os.path.join(os.getenv("APPDATA"), 'RegistroInterno')
file_name = 'registros.csv'
fields = ['id','desc','solic','setor','ramal','dt','obs','finalizado']
now = datetime.now().strftime('%d-%m-%y_%H-%M-%S')

def getFields():
    return fields

def getPath(arquivo: str = ''):
    return f'{os.path.join(default_path, arquivo)}'

def toList(string):
    li = list(string.split(','))
    return li

def field_check(full_path):
    header = []
    
    with open(full_path, 'r') as file:
        reader = csv.reader(file)
        header = reader.__next__()
        
    if header == fields:
        print(f'Campos: True')
    else:
        print(f'Campos: False')
        new_file = f'{str(file_name).replace(".csv", "")}_{now}.csv'
        
        shutil.copyfile(full_path, os.path.join(default_path, new_file))

        with open(full_path, 'w', newline='', encoding='UTF8') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
        
        print('Arquivo recriado: True')

def tb_check():
    full_path = os.path.join(default_path, file_name)

    path_exists = os.path.isdir(default_path)
    print(f'Caminho existe: {path_exists}')
    if path_exists == False:
        os.mkdir(default_path)
        print(f'Pasta criada: {path_exists}')

    file_exists = os.path.isfile(full_path)
    print(f'Arquivo existe: {file_exists}')
    if file_exists == False:
        with open(full_path, 'w', newline='', encoding='UTF8') as file:
            file.write(''.join(fields))
        print(f'Arquivo criado: {file_exists}')

    field_check(full_path)

    return full_path

full_path = tb_check()

def listRows():
    rows = []
    with open(full_path, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            rows.append(f'{",".join(row)}')
    
    return rows

def addRow(string):
    newRow = toList(string)

    with open(full_path, 'a', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(newRow)

def newId():
    return len(listRows())