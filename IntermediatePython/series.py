#coding:UTF-8
from random import randint

def criaListaAleatoria(quantidadeElementos):
	lista = []
	for i in range(quantidadeElementos):
		numeroAleatorio = randint(0,9)
		lista.append(numeroAleatorio)
	print ('Lista Aleatória: {}'.format(lista))

def serieImpar(qtde = 10):
	lista = []
	for i in range(qtde):
		if((i % 2) != 0):
			lista.append(i)
	print ('Serie Impar: {}'.format(lista))

def serieSoma(qtde = 6):
	lista = []
	resp = 1
	for i in range(qtde):
		resp += i
		lista.append(resp)
	print ('Serie Soma: {}'.format(lista))

def seriePrimo(a = 5, b = 10):
	lista = []
	for i in range(a, b+1):
		cont = 0
		div = 1
		while(div < b+1):
			if(i % div == 0 and i % 1 == 0):
				cont += 1
			div += 1
		if(cont == 2):
			lista.append(i)
	print ('Serie Primo: {}'.format(lista))

def serieFibonacci(qtde = 6):
	lista = []
	a = 1
	b = 1
	x = 0
	lista.append(a)
	lista.append(b)
	for i in range(qtde - 1):
		x = b
		b = b + a
		a = x
		lista.append(b)
	print ('Serie Fibonacci: {}'.format(lista))

criaListaAleatoria(5)
serieImpar()
serieSoma()
seriePrimo()
serieFibonacci()
