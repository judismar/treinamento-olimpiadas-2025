#Problema Senha da Vó Zinha, 2021, fase 2

entrada = input().split()
palavra = input()
N = int(entrada[0])
M = int(entrada[1])
K = int(entrada[2])

l = []
for _ in range(M): #repeat M times
	l.append(input())
P = int(input())

n = M
l2 = [palavra]
l3 = []
while len(l2) > 0:
	palavra = l2.pop()
	i = n - palavra.count('#')
	if i == n:
		l3.append(palavra)
		continue
	indice = palavra.index('#')
	for letra in l[i]:
		p = palavra[:indice:] + letra + palavra[indice+1::]
		l2.append(p)

l3.sort()
print(l3[P-1])
