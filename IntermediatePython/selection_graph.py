from random import randint
import matplotlib.pyplot as plt
import timeit

def selectionSort(l):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[menor]):
                menor = j
        aux = lista[menor]
        lista[menor] = lista[i]
        lista[i] = aux
    return lista

lista = []
x = [100,300,600,900,1200,1500,1800,2100,2400]
y = []

for i in x:
    lista = []
    for k in range(i):
        lista.append(randint(0, 99))
    y.append(timeit.timeit("selectionSort({})".format(i), setup="from __main__ import selectionSort", number=1))

plt.plot(x, y)
plt.ylabel('Tempo')
plt.xlabel('Valores')
plt.show()
