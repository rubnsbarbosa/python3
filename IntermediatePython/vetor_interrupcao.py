# criando um vetor/lista vazio(a)
v = []

# criando dez funcoes
def a():
	return 1*1
def b():
	return 2*2
def c():
	return 3*3
def d():
	return 4*4
def e():
	return 5*5
def f():
	return 6*6
def g():
	return 7*7
def h():
	return 8*8
def i():
	return 9*9
def j():
	return 10*10

# cada indice do vetor esta recebendo uma funcao diferente
v.append(a())
v.append(b())
v.append(c())
v.append(d())
v.append(e())
v.append(f())
v.append(g())
v.append(h())
v.append(i())
v.append(j())

# entrando com o indice do vetor e chamando a funcao que foi passada no determinado indice
while(True):
	indice = int(input("Digite o indice: "))

	if(indice >= 0 and indice <= 9):
		print (v[indice])
	else:
		exit("Indice invalido!")
