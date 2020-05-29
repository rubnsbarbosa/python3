#Matriz A e B que serao somadas
A = [[1,2], [3,4]]
B = [[0,5], [-1,6]]

#Funcao que retorna a soma das matrizes A e B
def somaDuasMatrizes(X):
	a = X[0]
	b = X[1]

	soma = []
	for i in range(len(b)):
		soma.append([])

		for j in range(len(b)):
			soma[i].append(a[i][j] + b[i][j])

	return soma

#Matriz resultado, recebe a soma das matrizes A e B
resultado = list(map(somaDuasMatrizes, [[A, B]]))
resultado = resultado[0]

print (resultado)
