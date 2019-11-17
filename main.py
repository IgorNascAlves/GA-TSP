import Cidades as C
import GeneticAlgorithms as GA
import grafico as g

cidades = C.Cidades()
#cidades.aleatorio(5)
cidades.leitorArq()
#cidades.leitorArqVar(10)
GA = GA.GeneticAlgorithms(3,cidades)
#print(GA.familia.filhos)

g.grafico(cidades,GA.familia.filhos[0])