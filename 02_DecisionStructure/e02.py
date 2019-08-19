num = int(input('Digite um valor: '))

def posNeg(n):
    if n >= 0:
        print('{} eh positivo'.format(n))
    else:
        print('{} eh negativo'.format(n))

posNeg(num)
