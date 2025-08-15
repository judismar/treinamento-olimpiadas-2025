#Problema da OBI, 2006, Penalidade Mínima

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
for k in range(N):
    s[k] = input()

tabuleiro = {}
i = 0
j = 0
for linha in s:
    l = linha.split()
    for item in l:
        tabuleiro[j, i] = int(item)
        j += 1
    i += 1
    j = 0

pilhaMovimento = [{"posição": (0, 0), "pontuação": tabuleiro[0, 0],  "direção": 'b'}, {"posição": (0, 0), "pontuação": tabuleiro[0, 0],  "direção": 'd'}]
penalidadeMinima = -1

while len(pilhaMovimento) > 0:
    elementoPilha = pilhaMovimento.pop()
    passo = elementoPilha["direção"] #passo seguinte
    x, y = elementoPilha["posição"]
    pontuacao = elementoPilha["pontuação"]

    if x == N-1 and y == N-1: #está no final do tabuleiro?
        penalidade = calculaPenalidade(pontuacao)
        if penalidade == 0:
            penalidadeMinima = 0
            break
        elif penalidadeMinima == -1 or penalidade < penalidadeMinima: #penalidade inicial, para começar
            penalidadeMinima = penalidade
            
    elif passo == 'd':
        if x + 1 != N and tabuleiro[x+1, y] != 0:
            x += 1
            pontuacao *= tabuleiro[x, y]
            pilhaMovimento.append({"posição": (x, y), "pontuação": pontuacao,  "direção": 'b'})
            pilhaMovimento.append({"posição": (x, y), "pontuação": pontuacao,  "direção": 'd'})
    else:
        if y + 1 != N and tabuleiro[x, y+1] != 0:
            y += 1
            pontuacao *= tabuleiro[x, y]
            pilhaMovimento.append({"posição": (x, y), "pontuação": pontuacao,  "direção": 'b'})
            pilhaMovimento.append({"posição": (x, y), "pontuação": pontuacao,  "direção": 'd'})
print(penalidadeMinima)
