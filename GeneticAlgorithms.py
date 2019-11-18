import random
import Cidades as cC
import Familia as Fa
import Filho as Fi

class GeneticAlgorithms:
    def __init__(self, numeroFilhos, dados):
        self.numeroFilhos = numeroFilhos
        self.dados = dados
        self.familia = self.primeiraGeracao(dados)
        
    def primeiraGeracao(self, dados):
        filhos = []
        for i in range(0, self.numeroFilhos, 1):
            i = i
            ordemCidade = random.sample(range(1, len(dados.cidades), 1), len(dados.cidades)-1)
            ordemCidade.insert(0, 0)
            ordemCidade.append(0)
            filhos.append(Fi.Filho(ordemCidade, dados))
        return Fa.Familia(filhos, dados)

    def roletaNL(self):
        total = 0
        for i in self.familia.filhos:
            total = total + i.distTotal 
        r = random.randint(0,int(total))
        escolhido = 0
        for i in range(0,len(self.familia.filhos),1):
            aptidao = 0
            for x in range(0,i,1):
                aptidao = aptidao + self.familia.filhos[x].distTotal 
            if(aptidao >= r):
                escolhido = i
        return self.familia.filhos[escolhido]
    
    def crossoverLista(self):
        filhos = []
        for x in range(0,self.numeroFilhos-2,1):
            x=x
            pai1 = self.roletaNL()
            pai2 = self.roletaNL()
            ordemCidade = []
            lista = []
            [lista.append(x) for x in range(0,len(self.dados.cidades),1)]
            i = 1
            tamanho = int(len(self.dados.cidades)/2)
            for i in range(1,tamanho,1):
                lista.remove(pai1.ordemCidade[i])
                ordemCidade.append(pai1.ordemCidade[i])    
            while(len(ordemCidade) != len(self.dados.cidades)-1):
                try:      
                    lista.remove(pai2.ordemCidade[i])                 
                    ordemCidade.append(pai2.ordemCidade[i]) 
                except:
                    i=i    
                i = i + 1
                if(i >= len(self.dados.cidades)):
                    i = 1
            ordemCidade.insert(0, 0)
            ordemCidade.append(0)     
            filhos.append(Fi.Filho(ordemCidade, self.dados))
        filhos.append(self.familia.filhos[0])
        filhos.append(self.familia.filhos[1])
        self.familia = Fa.Familia(filhos, self.dados)
        self.mutacao()

    def troca(self, vetor):
        pontoA = random.randint(0,len(vetor)-1)
        pontoB = random.randint(0,len(vetor)-1)
        valor = vetor[pontoA]
        vetor[pontoA] = vetor[pontoB]
        vetor[pontoB] = valor
        return vetor


    def mutacao(self):
        for x in range(0,int(self.numeroFilhos*0.1),1):
            x = x 
            qualFilho = random.randint(0,self.numeroFilhos-1)
            self.familia.filhos[qualFilho].ordemCidade = self.troca(self.familia.filhos[qualFilho].ordemCidade)
