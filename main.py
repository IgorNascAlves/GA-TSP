import Cidades as C
import GeneticAlgorithms as GA

cidades = C.Cidades()
cidades.aleatorio(5)
GA = GA.GeneticAlgorithms(3,cidades)
print(GA.familia.filhos)