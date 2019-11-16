import random
import numpy as np
import Cidade as C

class Cidades:
  cidades = []
  matrizDist = []

  def leitorArq(self):
    self.cidades.clear()
    arquivo = open('mapa250.txt', 'r')
    stream = arquivo.readlines()
    lines = []
    for line in stream:
      vetor = line.split()
      cidade = C.Cidade(float(vetor[0]),float(vetor[1]))
      lines.append(cidade)
    arquivo.close()
    self.cidades = lines
    self.construirMatriz()

  def aleatorio(self, num):
    self.cidades.clear()    
    for i in range(0, num, 1):
      i = i
      cidade = C.Cidade(random.uniform(2.5, 10.0), random.uniform(2.5, 10.0))
      self.cidades.append(cidade)  
    self.construirMatriz()

  def instanciarMatriz(self):
    self.matrizDist = np.zeros((len(self.cidades),len(self.cidades)), dtype=np.float64)
    
  def construirMatriz(self):
    self.instanciarMatriz()
    for i in range(0,len(self.cidades),1):
      for j in range(0,len(self.cidades),1):
        self.matrizDist[i][j] = self.euclidiana(self.cidades[i],self.cidades[j])

  def euclidiana(self, cidadeA, cidadeB):
      dist = 0  
      DeltaX = float(cidadeA.x) - float(cidadeB.x)    
      DeltaY = float(cidadeA.y) - float(cidadeB.y)    
      dist = pow(pow(DeltaX,2) + pow(DeltaY,2),.5)
      return dist    

  def calcDistTotal(self, vetor):
    total = 0
    for i in range(0, len(vetor)-1, 1):
      total = total + self.matrizDist[vetor[i]][vetor[i+1]]
    return total
    
  def __repr__(self):
      return str(self.cidades)
