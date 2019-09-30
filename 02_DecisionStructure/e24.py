import math

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
op = input('Qual operacao voce quer realizar? (+) (-) (*) (/): ')

if op == '+':
    res = n1 + n2
    frac, whole = math.modf(res)
    print('Resultado {}:'.format(res))
    if res % 2 == 0:
        print('Numero Par')
    else:
        print('Numero Impar')
    if frac == 0.0:
        print('Numero Inteiro')
    else:
        print('Numero Decimal')
    if res > 0:
        print('Numero Positivo')
    else:
        print('Numero Negativo')

elif op == '-':
    res = n1 - n2
    frac, whole = math.modf(res)
    print('Resultado {}:'.format(res))
    if res % 2 == 0:
        print('Numero Par')
    else:
        print('Numero Impar')
    if frac == 0.0:
        print('Numero Inteiro')
    else:
        print('Numero Decimal')
    if res > 0:
        print('Numero Positivo')
    else:
        print('Numero Negativo')

elif op == '*':
    res = n1 * n2
    frac, whole = math.modf(res)
    print('Resultado {}:'.format(res))
    if res % 2 == 0:
        print('Numero Par')
    else:
        print('Numero Impar')
    if frac == 0.0:
        print('Numero Inteiro')
    else:
        print('Numero Decimal')
    if res > 0:
        print('Numero Positivo')
    else:
        print('Numero Negativo')
        
elif op == '/':
    res = n1 / n2
    frac, whole = math.modf(res)
    print('Resultado {}:'.format(res))
    if res % 2 == 0:
        print('Numero Par')
    else:
        print('Numero Impar')
    if frac == 0.0:
        print('Numero Inteiro')
    else:
        print('Numero Decimal')
    if res > 0:
        print('Numero Positivo')
    else:
        print('Numero Negativo')
