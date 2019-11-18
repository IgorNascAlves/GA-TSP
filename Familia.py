import Filho as F
import operator

class Familia:

    def __init__(self, filhos, dados):
        self.filhos = filhos
        #self.ordenarFilhos()
        self.ordenarDecreFilhos()

    def ordenarFilhos(self):
        self.filhos.sort(key=operator.attrgetter('distTotal'))
    def ordenarDecreFilhos(self):
        self.filhos.sort(reverse = True, key=operator.attrgetter('distTotal'))