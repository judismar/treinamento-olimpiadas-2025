#Problema da OBI, 2021, Cálculo rápido

S, A, B = int(input()), int(input()), int(input())
cont = 0
for num in range(A, B+1):
    num = str(num)
    l = []
    for digito in num:
        l.append(int(digito))
    if sum(l) == S:
        cont += 1
print(cont)
