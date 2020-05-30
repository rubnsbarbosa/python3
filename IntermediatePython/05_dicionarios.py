## criando um dicionario
d1 = {'key1': 'value1'}
print(d1)
print(d1['key1'])

## outra forma de criar dicionario
d2 = dict(key1='value2', key2='value3')
print(d2)

d3 = {1 : 'valor 1', 2 : 'valor 2', 3 : 'valor 3'}
print(d3)

## add uma chave valor a um dicionario existente
d1['key2'] = 'agora existe'

if d1.get('key2') is not None:
    print(d1.get('key2'))

## vendo o tamanho de um dicionario
print(len(d1))

## iterando sobre um dicionario
for i in d1:
    print(i, d1[i])

## outra forma
for k in d1.values():
    print(k)

## outra forma
for chave, valor in d1.items():
    print(chave, valor)

## dicionario de clientes
clientes = {
    'cliente1' : {
        'nome' : 'Rubens',
        'sobrenome' : 'Barbosa',
    },
    'cliente2' : {
        'nome' : 'Gabriel',
        'sobrenome' : 'Barbosa',
    },
}

for clientes_k, clientes_v in clientes.items():
    print('exibindo {}'.format(clientes_k))
    for dados_k, dados_v in clientes_v.items():
        print(dados_k, dados_v)

## removendo valores de um dicionario
dic1 = {
    1 : 2,
    2 : 3,
    3 : 4,
    4 : 5,
}
## removendo a chave 4
dic1.pop(4)
print(dic1)

## concatenando dois dicionarios
d1.update(dic1)
print(d1)
