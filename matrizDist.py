import calc_dist as CD
import leArq as LA
class MatrizDist:
    def funcTeste(self):
        #[CD.Teste().funcTeste(x) for x in lista]        
        lista = (LA.LeitorArq()).funcTeste()
        
        linha_com_zeros = [0.0]*2
        matriz = [linha_com_zeros] * 2
        #print(matriz[0][0])
        for x in range(0,2,1):
            for y in range(0,2,1):
                #print(x,y,":")                
                #print(matriz[0][0])
                matriz[x][y] = CD.Teste.funcTeste([lista[x], lista[y]])
        print(matriz[0][0])
        print(matriz[0][1])
        print(matriz[1][0])
        print(matriz[1][1])
        return matriz