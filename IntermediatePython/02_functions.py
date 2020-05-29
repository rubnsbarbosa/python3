#coding:UTF-8
from random import randint

def mediaNumerosAleatorios(tamanhoLista = int(input("Digite o tamanho da lista: "))):
	lista = []
	soma = 0
	for i in range(tamanhoLista):
		numAleatorio = randint(0,9)
		lista.append(numAleatorio)
		soma = soma + lista[i]
		media = (soma/float(tamanhoLista))
	print('Lista de números aleatórios {}'.format(lista))
	print('Média da lista de num aleatórios {}'.format(media))

def numerosAleatoriosDistintos(tamanhoLista = 10):
	lista = []
	for i in range(tamanhoLista):
		numAleatorio = randint(0,9)
		if(numAleatorio not in lista):
			lista.append(numAleatorio)
	print('Lista de números distintos {}'.format(lista))

def produtoEscalar(tamanhoLista = 5):
	listaA = []
	listaB = []
	for i in range(tamanhoLista):
		listaA.append(randint(0,9))
		listaB.append(randint(0,9))
	listaC = []
	for j in range(tamanhoLista):
		listaC.append(listaA[j] * listaB[j])
	print('Lista_A {}'.format(listaA))
	print('Lista_B {}'.format(listaB))
	print('Lista_C = Lista_A * Lista_B {}'.format(listaC))

def listaPrimos(tamanhoLista = 10):
	lista = []
	for i in range(tamanhoLista):
		num = randint(0,9)
		lista.append(num)
	listaPrimo = []
	for j in range(tamanhoLista):
		cont = 0
		div = 1
		while(div < tamanhoLista):
			if(j % div == 0):
				cont += 1
			div += 1
		if(cont == 2):
			listaPrimo.append(j)
	print(lista)
	print('lista Primo {}'.format(listaPrimo))

def listaInvertida(qtde = 6):
	lista = []
	for i in range(qtde):
		n = randint(0,9)
		lista.append(n)
	print (lista)
	print (lista[::-1])

def listaImparesInvertidos():
	lista = [0,1,2,3,4,5]
	aux = 0
	for i in range(len(lista)):
		if((i % 2) != 0):
			for j in range(len(lista)):
				if((j % 2) != 0):
					aux = lista[i]
					lista[i] = lista[j]
					lista[j] = aux
	print ('lista invertida {}'.format(lista))

mediaNumerosAleatorios()
numerosAleatoriosDistintos()
produtoEscalar()
listaPrimos()
listaInvertida()
listaImparesInvertidos()
