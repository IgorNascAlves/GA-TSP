import random
class primeiraGeracao:
  def __init__(self, list):
    self.vetor = self.gerarVetor(list)
  def gerarVetor(self,list):
    vetor = []
    vetor = random.sample(range(len(list)), len(list))
    return vetor