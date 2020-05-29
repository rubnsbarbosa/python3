import math

peso = [43, 50, 52, 56, 60, 62, 67, 68, 70, 72, 73, 75, 77, 78, 80, 95]
soma = 0
for i in range(len(peso)):
	soma = soma + peso[i]
	qtde = len(peso)
mediaPeso = (soma/float(qtde))
print ('media do peso e altura respectivamente')
print (mediaPeso)

altu = [1.54, 1.60, 1.63, 1.67, 1.67, 1.67, 1.67, 1.68, 1.68, 1.68, 1.69, 1.70, 1.70, 1.72, 1.73, 1.78]
s = 0
for i in range(len(altu)):
	s = s + altu[i]
	qtdeElem = len(altu)
mediaAltu =  (s/float(qtdeElem))
print (mediaAltu)

varianciaPeso = 0
plus = 0
for i in range(len(peso)):
	plus += math.pow((peso[i] - mediaPeso),2)
varianciaPeso = (plus / float(len(peso)))
print ('variancia do peso e altura respectivamente')
print (varianciaPeso)

varianciaAltura = 0
pluss = 0
for i in range(len(altu)):
	pluss += math.pow((altu[i] - mediaAltu),2)
varianciaAltura = (pluss / float(len(altu)))
print (varianciaAltura)

# desvio padrao eh a raiz quadrada da variancia
desvioPadraoPeso = math.sqrt(varianciaPeso)
desvioPadraoAltu = math.sqrt(varianciaAltura)
print ('desvio padrao do peso e altura respectivamente')
print (desvioPadraoPeso)
print (desvioPadraoAltu)

# coeficiente de variacao eh o desvio padrao dividido pela media
cvPeso = 0
cvAltu = 0
cvPeso = (desvioPadraoPeso / mediaPeso)
cvAltu = (desvioPadraoAltu / mediaAltu)
print ('coeficiente de variacao do peso e altura respectivamente')
print (cvPeso)
print (cvAltu)
