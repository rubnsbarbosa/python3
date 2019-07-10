'''
Condições IF, ELIF e ELSE

Operadores Relacionais
== igualdade
>  maior que
>= maior ou igual a que
<  menor que
<= menor ou igual a que
!= diferente

Operadores Lógicos
and, or, not, in, not in
'''

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

# limite para pegar empréstimo
idade_menor = 20  # jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:    
    print(f'{nome} NÃO pode pegar o empréstimo.')


if 'u' in nome:
    print('Existe a letra U no seu nome.')
