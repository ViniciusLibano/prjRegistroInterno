from dal import filemanager

def newId():
    return len(filemanager.listRows())

class Registro():

    def __init__(self, descricao: str, sol: str, setor: str, ramal: str, data: str, obs: str, finalizado: bool):
        self.cd: int = newId()
        self.descricao: str = descricao
        self.sol: str = sol
        self.setor: str = setor
        self.ramal: str = ramal
        self.data: str = data
        self.obs: str = obs
        self.finalizado: bool = finalizado

    def __str__(self):
        return f'{self.cd},{self.descricao},{self.sol},{self.setor},{self.ramal},{self.data},{self.obs},{self.finalizado}'
    
def verificar(reg: Registro):
    obs = []

    if reg.sol == '' or reg.sol == None:
        reg.sol = 'vllalves'
        obs.append('Nao anotou o campo: Solicitante')
    if reg.setor == '' or reg.setor == None:
        reg.setor = 'TI'
        obs.append('Nao anotou o campo: Setor')
    if reg.ramal == '' or reg.ramal == None:
        reg.ramal = '10000'
        obs.append('Nao anotou o campo: Ramal')
    
    reg.obs = ' - '.join(obs)