#import calc_dist as CD
#import leArq as LA
#import matrizDist as MD
import criaCidades as CC
import criaGeracao as CG

#matriz = MD.MatrizDist().funcTeste()
cidades = CC.Cidades(10)
primeira = CG.primeiraGeracao(cidades.lista).vetor
print(primeira)
print(cidades.calcDistTotal(primeira))

#lines = (LA.LeitorArq()).funcTeste() #ler arquivo
#CD.Teste.funcTeste([lines[0], lines[1]]) #calcular distancia
#construir matriz dist
#AlgoritimoGenetica