class CalcDist:
    def euclidiana(self, lista):
        i = 0
        dist = 0
        for i in range(0,len(lista)-1):     
            DeltaX = float(lista[i].x) - float(lista[i+1].x)    
            DeltaY = float(lista[i].y) - float(lista[i+1].y)    
            dist = dist + pow(pow(DeltaX,2) + pow(DeltaY,2),.5)
            i = i + 1
        return dist