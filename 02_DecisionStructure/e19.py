num = int(input('Digite um numero inteiro: '))

def findCenDezUnit(n):
    cent = (n / 100)
    dez = cent % 1
    dez = dez * 10
    unit = n % 10
    print('{} = {} centenas, {} dezenas e {} unidades'.format(num, int(cent), int(dez), unit))

if num < 1000 and num > 0:
    findCenDezUnit(num)
else:
    print('O numero deve ser menor que 1000')
