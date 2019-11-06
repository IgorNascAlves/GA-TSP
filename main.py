import calc_dist as CD
arquivo = open('mapa250.txt', 'r')
stream = arquivo.readlines()
lines = []
for line in stream:
    lines.append(line.split())
teste1 =  CD.Teste()
teste1.funcTeste([lines[0], lines[1], lines[2]])
arquivo.close()