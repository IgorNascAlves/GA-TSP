class Teste:
    def funcTeste(self, lista):
        i = 0
        dist = 0
        for i in range(0,len(lista)-1):     
            DeltaX = float(lista[i][0]) - float(lista[i+1][0])    
            DeltaY = float(lista[i][1]) - float(lista[i+1][1])    
            dist = dist + pow(pow(DeltaX,2) + pow(DeltaY,2),.5)
            i = i + 1
        print(dist)