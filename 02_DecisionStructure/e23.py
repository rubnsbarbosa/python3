import math

num = float(input('Digite um numero: '))
frac, whole = math.modf(num)

if frac == 0.0:
    print('Numero Inteiro')
else:
    print('Numero Decimal')
