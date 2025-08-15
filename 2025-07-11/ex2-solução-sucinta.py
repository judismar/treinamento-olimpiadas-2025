#Problema da OBI, 2021, Cifras da Nglonia

dicionarioCifras = {'a': 'a', 'b': 'bac', 'c': 'cad', 'd': 'def', 'e': 'e', 'f': 'feg', 'g': 'geh', 'h': 'hij', 'i': 'i', 'j': 'jik', 'k': 'kil', 'l': 'lim', 'm': 'mon', 'n': 'nop', 'o': 'o', 'p': 'poq', 'q': 'qor', 'r': 'ros', 's': 'sut', 't': 'tuv', 'u': 'u', 'v': 'vux', 'x': 'xuz', 'z': 'zuz'}
palavra = input()
cifrada = ""
for letra in palavra:
        cifrada += dicionarioCifras[letra]
print(cifrada)
