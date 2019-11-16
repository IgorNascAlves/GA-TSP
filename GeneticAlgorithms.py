import random
import Cidades as cC
import Familia as Fa
import Filho as Fi

class GeneticAlgorithms:
    familia = []
    def __init__(self, numeroFilhos, dados):
        self.numeroFilhos = numeroFilhos
        self.dados = dados
        self.familia = self.primeiraGeracao(dados)

    def primeiraGeracao(self, dados):
        filhos = []
        for i in range(0, self.numeroFilhos, 1):
            i = i
            ordemCidade = random.sample(range(1,len(dados.cidades),1), len(dados.cidades)-1)
            ordemCidade.insert(0,0)
            ordemCidade.append(0)
            filhos.append(Fi.Filho(ordemCidade,dados))
        return Fa.Familia(filhos,dados)
