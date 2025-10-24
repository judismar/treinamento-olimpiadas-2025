#Problema 2006, penalidade mínima, uma variante

N = int(input())
s = [None]*N
for k in range(N):
    s[k] = input().split()

g = {}
for i in range(N):
    for j in range(N):
        g[i, j] = []
        if j-1 >= 0 and s[i][j-1] != '0':
            g[i, j].append([i, j-1, int(s[i][j-1]), False, 0])
        if j+1 < N and s[i][j+1] != '0':
            g[i, j].append([i, j+1, int(s[i][j+1]), False, 0])
        if i-1 >= 0 and s[i-1][j] != '0':
            g[i, j].append([i-1, j, int(s[i-1][j]), False, 0])
        if i+1 < N and s[i+1][j] != '0':
            g[i, j].append([i+1, j, int(s[i+1][j]), False, 0])

listaSolucao = []

Q = [(0, 0, 0)] #Origem
while Q != []:
    v, w, custo = Q.pop()
    if v == N-1 and w == N-1: #verifivação: chegou no destino?
        listaSolucao.append(custo)
        continue
    for adj in g[v, w]:
        if not adj[3] or custo + adj[2] < adj[4]:
            Q.append((adj[0], adj[1], custo + adj[2]))
            adj[3] = True
            adj[4] = custo + adj[2]

listaSolucao.sort()
print(listaSolucao[0])
