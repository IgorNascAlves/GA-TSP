import criaCidades as CC
import criaGeracao as CG
cidades = CC.Cidades(10)
#for x in lista:
  #print(x)
primeira = CG.primeiraGeracao(cidades.lista).vetor
print(primeira)
print(cidades.calcDistTotal(primeira))