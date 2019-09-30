num_litro = int(input('Digite a qtde de litros: '))
tipo = input('Qual tipo de combustivel? \nA-álcool\nG-gasolina: ')
print('\n')

if tipo == 'A':
    valor = num_litro * 1.9
    if num_litro > 20:
        valor = valor * 0.5
        print('Valor a pagar: {}'.format(valor))
    else:
        valor = valor * 0.3
        print('Valor a pagar: {}'.format(valor))

elif tipo == 'G':
    valor = num_litro * 2.5
    if num_litro > 20:
        valor = valor * 0.6
        print('Valor a pagar: {}'.format(valor))
    else:
        valor = valor * 0.4
        print('Valor a pagar: {}'.format(valor))

else:
    print('O tipo de combustivel informado nao eh valido!')
