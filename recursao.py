"""for k in range(10):
    print(k)"""

"""k = 0
while k < 10:
    print(k)
    k += 1"""

"""def f(k):
    if k < 10:
        print(k)
        f(k+1)
f(0)"""

l = [2, 3, 5, 7, 11]
"""soma = 0
for num in l:
    soma += num
print(soma)"""

def soma(l, k):
    if k < len(l):
        return soma(l, k+1) + l[k]
    else:
        return 0
#soma(l, 0)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(40))

#Solução por programação dinâmica:
n = 5
f = [None]*n
f[0] = 0
f[1] = 1
k = 2
while k < n:
    f[k] = f[k-1] + f[k-2]
    k += 1
print(f[n-1])