from random import randint
import matplotlib.pyplot as plt
import timeit
import random

lista = []
def criaLista(tamanho):
    random.seed()
    global lista
    lista=[]
    i = 0
    while i < tamanho:
        x  = random.randint(1,10000*tamanho)
        if x not in lista:
            lista.append(x)
            i += 1
    return lista

def selectionSort(x):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[menor]):
                menor = j
        aux = lista[menor]
        lista[menor] = lista[i]
        lista[i] = aux
    return lista

#lista = []
x = [100,300,600,900,1200,1500,1800,2100,2400]
y = []
yCria = []
for i in x:
    lista = []
    for k in range(i):
        lista.append(randint(0, 99))
    y.append(timeit.timeit("selectionSort({})".format(i), setup="from __main__ import selectionSort", number=1))
    yCria.append(timeit.timeit("criaLista({})".format(i), setup="from __main__ import criaLista", number=1))

plt.plot(x, y)
plt.plot(x, yCria)
plt.ylabel('Tempo')
plt.xlabel('Valores')
plt.show()
