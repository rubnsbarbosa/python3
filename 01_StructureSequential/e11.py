# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       o produto do dobro do primeiro com metade do segundo .
#       a soma do triplo do primeiro com o terceiro.
#       o terceiro elevado ao cubo.
n1_int = int(input('Digite um numero inteiro: '))
n2_int = int(input('Digite um numero inteiro: '))
n3_real = float(input('Digite um numero real: '))

r1 = (n1_int * 2) * (n2_int / 2)
r2 = (n1_int * 3) + n3_real
r3 = (n3_real ** 3)

print('{}\n{}\n{}\n'.format(r1, r2, r3))
