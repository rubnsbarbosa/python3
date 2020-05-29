#coding:utf-8
from random import randint

# funcao que cria uma lista aleatoria com elementos distintos
def listaAleatoria(n = int(input("Digite a qtde de elementos da lista: "))):
	lista = []
	for i in range(n):
		num = randint(0,9)
		if(num not in lista):
			lista.append(num)
	return lista

def selectionSort(lista = listaAleatoria()):
	for i in range(len(lista)):
		menor = i
		for j in range(i+1, len(lista)):
			if (lista[j] < lista[menor]):
				menor = j
		aux = lista[menor]
		lista[menor] = lista[i]
		lista[i] = aux
	print (lista)

selectionSort()
