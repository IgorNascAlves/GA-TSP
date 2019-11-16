import Filho as F
import operator

class Familia:

    def __init__(self, filhos, dados):
        self.filhos = filhos
        self.ordenarFilhos()

    def ordenarFilhos(self):
        self.filhos.sort(key=operator.attrgetter('distTotal'))