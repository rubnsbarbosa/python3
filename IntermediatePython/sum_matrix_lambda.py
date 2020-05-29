m1 = [[1,2,3], [4,5,6], [7,8,9]]
m2 = [[9,8,7], [6,5,4], [3,2,1]]

## somar duas matrizes 
def somaMatriz(m,n):
	nl = len(m)
	matriz = [None] * nl
	for i in range (nl):
		matriz[i] = list(map(lambda x, y: x+y, m[i], n[i]))
	return matriz

valor = somaMatriz(m1, m2)
print (valor)
