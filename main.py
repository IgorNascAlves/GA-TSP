print("Hello Word")
arquivo = open('mapa250.txt', 'r')
stream = arquivo.readlines()
lines = []
for line in stream:
    lines.append(line.split())
print(lines)
arquivo.close()