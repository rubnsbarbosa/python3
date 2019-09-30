n1 = float(input('Digite a primeira nota parcial: '))
n2 = float(input('Digite a segunda nota parcial: '))
n3 = float(input('Digite a terceira nota parcial: '))

media = (n1 + n2 + n3) / 3

def check_status(m):
    if m == 10:
        print('Aprovado com Distinção')
    elif m >= 7:
        print('Aprovado')
    else:
        print('Reprovado')

check_status(media)
