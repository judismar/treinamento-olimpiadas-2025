from time import clock_gettime
from random import *
from sys import argv

n = int(argv[1])
N_MEDIA = int(argv[2])

def buscaLista(x, lista):
    for elemento in lista:
        if elemento == x:
            return True
    return False

def listaParaTabelaHash(lista):
    d = {}
    for elemento in lista:
        d[elemento] = elemento
    return d

def expLista(n, numExp):
    U = range(1, 10**7+1)
    S = sample(U, n)
    l = list(S)
    inicio = clock_gettime(1)
    for ___ in range(numExp):
        i = randint(0, len(S)-1)
        buscaLista(S[i], l)
    fim = clock_gettime(1)
    tempoMedio = (fim - inicio)/numExp
    print("Tempo médio de execução \
de uma busca em uma lista \
linear: " + str(tempoMedio) + " segundos.")

def expTabelaDispersao(n, numExp):
    U = range(1, 10**7+1)
    S = sample(U, n)
    d = listaParaTabelaHash(S)
    inicio = clock_gettime(1)
    for ___ in range(numExp):
        i = randint(0, len(S)-1)
        d[S[i]]
    fim = clock_gettime(1)
    tempoMedio = (fim - inicio)/numExp
    print("Tempo médio de execução \
de uma busca em uma tabela \
de dispersão: " + str(tempoMedio) + " segundos.")

expLista(n, N_MEDIA)
expTabelaDispersao(n, N_MEDIA)
