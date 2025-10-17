#Problema Dona Formiga, fase 2, 2020
#Solução feita pelos alunos Pedro Henrique Lyra e João Pedro Domingos, usando busca em grafos

entrada = input().split()

S = int(entrada[0])
T = int(entrada[1])
P = int(entrada[2])

altura = input().split()
lista_alturas = []
for x in altura:
    lista_alturas.append(int(x))

listaTuneis = []
for i in range(T):
    entradaS = input().split()
    listaTuneis.append((int(entradaS[0]), int(entradaS[1])))

grafo = {}
for k in range(1, S+1):
    grafo[k] = []

for x in listaTuneis:
    if lista_alturas[x[0]-1] < lista_alturas[x[1]-1]:
        grafo[x[1]].append(x[0])
    elif lista_alturas[x[0]-1] > lista_alturas[x[1]-1]:
        grafo[x[0]].append(x[1])
            
custoMax = []
Q = [(P, 0)]
while len(Q) > 0:
    v, custo = Q.pop(0)
    custoMax.append(custo)
    for w in grafo[v]:
        Q.append((w, custo+1))
custoMax.sort()
print(custoMax[len(custoMax)-1])
