import random
import calcDist as CD

class Cidade:
    def __init__(self, x,y):
      self.x = x 
      self.y = y
    def __str__(self):
      return "(x: " + str(self.x) + " " + "y: " + str(self.y) + ")"
    def __repr__(self):
      return "(x: " + str(self.x) + " " + "y: " + str(self.y) + ")"

class Cidades:
  def __init__(self, num): 
    self.lista = []
    self.preencher(num)
    
  def __repr__(self):
      return str(self.lista)

  def preencher(self, num):
    for i in range(0,num,1):
      i = i
      self.lista.append(Cidade(random.uniform(2.5, 10.0),random.uniform(2.5, 10.0)))
  def calcDistTotal(self,vetor):
    total = 0
    for i in range(0,len(vetor)-1,1):     
      total = total + CD.CalcDist().euclidiana([self.lista[vetor[i]],self.lista[vetor[i+1]]])
    return total