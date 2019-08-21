import math as m

a = int(input('Digite o lado A: '))
if a == 0:
    exit()
else:
    b = float(input('Digite o lado B: '))
    c = float(input('Digite o lado C: '))

delta = b**2 - 4 * a * c

def checkRoots(dlt):
    if dlt < 0:
        print('A equacao nao possui raizes reais')
    elif dlt == 0:
        root = -b + m.sqrt(dlt) / 2*a
        print('A equacao possui apenas uma raiz real: {}'.format(root))
    elif dlt > 0:
        root1 = -b + m.sqrt(dlt) / 2*a
        root2 = -b - m.sqrt(dlt) / 2*a
        print('A equacao possui duas raizes reais.\nr1: {} e r2: {}'.format(root1, root2))

checkRoots(delta)
