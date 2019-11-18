class Filho:

    def __init__(self, ordemCidade, dados):
        self.ordemCidade = ordemCidade
        self.distTotal = dados.calcDistTotal(ordemCidade)
        #self.distTotal = cC.Cidades().calcDistTotal(self.vetor)
    def __repr__(self):
      #return str(self.ordemCidade) + " DistTotal: " + str(self.distTotal) + "\n"
      #return str(self.ordemCidade) + "\n"
      return "DistTotal: " + str(self.distTotal) + "\n"