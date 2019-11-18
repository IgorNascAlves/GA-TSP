import Cidades as C
import GeneticAlgorithms as GA
import grafico as g

cidades = C.Cidades()

#cidades.aleatorio(5)
cidades.leitorArq()
#cidades.leitorArqVar(10)

GA = GA.GeneticAlgorithms(20,cidades)
#print(GA.familia.filhos)
#g.grafico(cidades,GA.familia.filhos[0])
print(GA.familia.filhos[0])
for i in range(0,500,1):
    GA.crossoverLista()
    print(GA.familia.filhos[0])
#g.grafico(cidades,GA.familia.filhos[0])