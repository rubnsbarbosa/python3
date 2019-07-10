'''
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float) :.2f
:.(NÚMERO)f - Quantidade de casas decimais float

> - Esquerda
< - Direita
^ - Centro
'''

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('{:.2f}' .format(divisao))
print(f'{divisao:.2f}')

nome = 'Rubens barbosa'
print(f'{nome:#^50}')
print(nome.lower())
print(nome.upper())
print(nome.title())

name = 'Rubens'
sobrenome = 'Barbosa'
nome_formatado = '{0:$^50} {1:#^50}'.format(name, sobrenome)
print(nome_formatado)

get_sobrenome = '{1}'.format(name, sobrenome)
print(get_sobrenome)

a = 1
print(f'{a:0>10}')

b = 1150
print(f'{b:0>10.2f}')

'''
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* funções built-in len, abs, type, print, etc...
'''

#positi[012345678]
text = 'Python s2'
#nega -[987654321]

# pegar os últimos 2 caracteres
print(text[-2:])
# pegando do -9 até o -3
print(text[-9:-3])
# pulando de 2 em 2 caracteres => passo = 2
print(text[0:6:2])  #pto
print(text[0::2])  #pto 2
print(len(text))

url = 'www.google.com.br/'
print(url[:-1])
























