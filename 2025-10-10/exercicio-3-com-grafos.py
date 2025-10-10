def P(v, w, custo):
    global penalidadeMin #declarando variável global
    Q.append((v, w))
    if v == N and w == N: #chegamos no destino
        penalidade = calculaPenalidade(custo)
        if penalidadeMin == -1 or penalidade < penalidadeMin:
            penalidadeMin = penalidade
    for vi in tabuleiro[v, w]:
        P(vi[0], vi[1], custo*vi[2])
    Q.pop()
    

def calculaPenalidade(num):
    num = str(num)
    num = num[::-1]
    cont = 0
    for digito in num:
        if digito != '0':
            break
        else:
            cont += 1
    return cont

N = int(input())
s = [None]*N
for i in range(N):
    s[i] = input().split()

tabuleiro = {}
for i in range(N):
    for j in range(N):
        tabuleiro[i+1, j+1] = []
        if j+1 < N and s[i][j+1] != '0':
            tabuleiro[i+1, j+1].append((i+1, j+2, int(s[i][j+1]))) 
        if i+1 < N and s[i+1][j] != '0':
            tabuleiro[i+1, j+1].append((i+2, j+1, int(s[i+1][j])))

Q = []
penalidadeMin = -1
P(1, 1, int(s[0][0]))
print(penalidadeMin)
