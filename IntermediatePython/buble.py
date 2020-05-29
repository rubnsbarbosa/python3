from random import randint
import matplotlib.pyplot as plt
import timeit

def criaListaAleatoria(quantidadeElementos):
    lista = []
    for i in range(quantidadeElementos):
        lista.append(randint(0,9))
    return lista

def selectionSort(lista):
    for i in range(len(lista)):
        menor = i
        for j in range(i+1, len(lista)):
            if (lista[j] < lista[menor]):
                menor = j
        aux = lista[menor]
        lista[menor] = lista[i]
        lista[i] = aux

def insertionSort(lista):
    for i in range(0, len(lista)):
        aux = lista[i]
        j = i
        while(j>0 and lista[j-1] > aux):
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = aux

def bubleSort(lista):
    for i in range(0, len(lista)):
        for j in range(0, len(lista)-1):
            if(lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

x = [100,300,600,900,1200,1500,1800,2100,2400]
selection = []
insertion = []
bolha = []
criar = []

for i in x:
    lista = criaListaAleatoria(i)
    criar.append(timeit.timeit("criaListaAleatoria({})".format(i), setup="from __main__ import criaListaAleatoria", number=1))
    selection.append(timeit.timeit("selectionSort({})".format(lista), setup="from __main__ import selectionSort", number=1))
    insertion.append(timeit.timeit("insertionSort({})".format(lista), setup="from __main__ import insertionSort", number=1))
    bolha.append(timeit.timeit("bubleSort({})".format(lista), setup="from __main__ import bubleSort", number=1))

plt.plot(x, insertion, 'o-', label='Tempo Insertion Sort')
plt.plot(x, selection, '+-', label='Tempo Selection Sort')
plt.plot(x, bolha, 'o-', label='Tempo BubleSort')
plt.plot(x, criar, '*-', label='Tempo de Criação')
plt.legend(('Tempo Insertion Sort','Tempo Selection Sort','Tempo BubleSort','Tempo de Criação'), loc='best')
plt.ylabel('Tempo')
plt.xlabel('Valores')
plt.show()
