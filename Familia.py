import Filho as F
class Familia:
    def __init__(self, filhos):
        self.filhos = filhos
        self.ordenarFilhos()
    def ordenarFilhos(self):
        self.filhos[0].sort()