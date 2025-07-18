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

N = 3
s = [None]*N
s[0] = "1 2 3"
s[1] = "4 5 6"
s[2] = "7 8 9"

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

x, y = 0, 0
mult = tabuleiro[0, 0]

pilhaMovimento = ['b', 'd']
pilhaRetorno = []

while len(pilhaMovimento) > 0:
    passo = pilhaMovimento.pop()
    if passo == 'd':
        if x + 1 != N and tabuleiro[x+1, y] != 0:
            x += 1
            mult *= tabuleiro[x, y]
            pilhaMovimento.append('b')
            pilhaMovimento.append('d')
            pilhaRetorno.append(passo)
            print(tabuleiro[x, y])
    else:
        if y + 1 != N and tabuleiro[x, y+1] != 0:
            y += 1
            mult *= tabuleiro[x, y]
            pilhaMovimento.append('b')
            pilhaMovimento.append('d')
            pilhaRetorno.append(passo)
            print(tabuleiro[x, y])
