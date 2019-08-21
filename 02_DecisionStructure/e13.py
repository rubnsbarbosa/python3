num = int(input('Digite um numero corresponde ao dia conforme exibido abaixo.\n1 - Domingo\n2 - Segunda\n3 - Terça\n4 - Quarta\n5 - Quinta\n6 - Sexta\n7 - Sabado\n'))

def show_day(n):
    if n == 1:
        print('Domingo')
    elif n == 2:
        print('Segunda')
    elif n == 3:
        print('Terça')
    elif n == 4:
        print('Quarta')
    elif n == 5:
        print('Quinta')
    elif n == 6:
        print('Sexta')
    elif n == 7:
        print('Sabado')
    else:
        print('Valor invalido!')

show_day(num)
