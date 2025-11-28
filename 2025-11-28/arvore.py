class Arvore:
    def __init__(self, num):
        self.valor = num
        self.esquerda = None
        self.direita = None
    def insere(self, num):
        if num <= self.valor:
            if self.esquerda == None: #nó folha
                self.esquerda = Arvore(num)
            else:
                self.esquerda.insere(num)
        else: #caso seja maior
            if self.direita == None: #nó folha
                self.direita = Arvore(num)
            else:
                self.direita.insere(num)
    
    def busca(self, num):
        if num == self.valor:
            return True
        elif self.esquerda != None and num < self.valor:
            return self.esquerda.busca(num)
        elif self.direita != None and num > self.valor:
            return self.direita.busca(num)
        else:
            return False
        
    def imprime(self):
        if self.esquerda != None:
            self.esquerda.imprime()
        print(self.valor)
        if self.direita != None:
            self.direita.imprime()

a = Arvore(42)
a.insere(10)
a.insere(5)
a.insere(90)
a.insere(20)
a.insere(60)
print(a.busca(999))
print(a.busca(90))
print(a.busca(7))
print(a.busca(5))
#a.imprime()
