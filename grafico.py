import matplotlib.pyplot as plt
class grafico:
    def __init__(self,dados,vetor):
        self.x = []
        self.y = []
        self.construir(dados,vetor.ordemCidade)
        self.rodar(vetor.distTotal)    
    def rodar(self,distTotal):                
        plt.plot(self.x,self.y,'ro-')
        plt.plot(self.x[0],self.y[0],'bo-')
        plt.title(str(distTotal))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    def construir(self,dados,vetor):
        for x in vetor:
            self.x.append(dados.cidades[x].x)            
            self.y.append(dados.cidades[x].y)
        