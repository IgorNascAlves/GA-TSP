class LeitorArq:
    def funcTeste(self):
        arquivo = open('mapa250.txt', 'r')
        stream = arquivo.readlines()
        lines = []
        for line in stream:
            lines.append(line.split())            
        arquivo.close()
        return lines