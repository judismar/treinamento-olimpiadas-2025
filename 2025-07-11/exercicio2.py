alfabeto = "a b c d e f g h i j k l m n o p q r s t u v x z".split()
vogais = "a e i o u".split()
def criaDicionario(alfabeto, vogais):
    d = {}
    for letra in alfabeto:
        if letra in vogais:
            d[letra] = letra
        else:
            k = alfabeto.index(letra)
            distancia = -1
            cifra = letra
            for i in range(k+1, len(alfabeto)):
                if alfabeto[i] in vogais:
                    c = alfabeto[i]
                    distancia = i - k
                    break
            for i in range(k-1, -1, -1):
                if alfabeto[i] in vogais:
                    if k - i <= distancia:
                        c = alfabeto[i]
                    break
            if letra == 'z':
                cifra += 'uz'
            else:
                cifra += c
                for i in range(k+1, len(alfabeto)):
                    if not alfabeto[i] in vogais:
                        cifra += alfabeto[i]
                        d[letra] = cifra
                        break
    return d
d = criaDicionario(alfabeto, vogais)
d['z'] = 'zuz'
palavra = input()
cifrado = ""

for letra in pala   vra:
        cifrado += d[letra]
print(cifrado)
