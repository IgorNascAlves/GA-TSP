import random
import Cidades as cC

class GeneticAlgorithms:
    def __init__(self, numeroGeracoes, numeroFilhos, dados):
        self.numeroGeracoes = numeroGeracoes
        self.numeroFilhos = numeroFilhos
        self.familia = []
        self.dados = dados

    def primeiraGeracao(self, list):
        vetor = []
        for i in range(0, self.numeroFilhos, 1):
            i = i
            vetor = random.sample(range(len(list)), len(list))
            self.familia.append(vetor)
        return self.familia

    def fitness(self):
        print(self.familia[0])
        self.familia[0].sort()
        print(self.familia[0])

    def leitorArq(self):
        arquivo = open('mapa250.txt', 'r')
        stream = arquivo.readlines()
        lines = []
        for line in stream:
            lines.append(line.split())            
        arquivo.close()
        self.dados = lines
        return lines