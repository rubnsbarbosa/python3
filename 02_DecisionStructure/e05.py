nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))

m = (nota1 + nota2) / 2

def checkStatus(media):
    if media == 10:
        print('Aprovado com Distincao')
    elif media >= 7 and media < 10:
        print('Aprovado')
    elif media < 7:
        print('Reprovado')

checkStatus(m)
