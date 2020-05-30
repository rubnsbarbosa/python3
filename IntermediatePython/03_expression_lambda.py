## funcao anonima

## multiplicando com lambda to passando 2 parametros e multiplicando
a = lambda x, y: x * y
print(a(2, 2)) # 2*2 = 4

## passar uma funcao por parametro pra outra funcao
gordice = [
    ['Coca-Cola', 6],
    ['Kalzone', 14],
    ['Fritas', 9],
    ['BigMac', 19],
    ['Coxinha', 3],
]

## vamos ordenar a lista de gordice pelo preço do menor para o maior
## usamos 1 porque refere-se ao preço na lista da lista
gordice.sort(key= lambda item: item[1])
print(gordice)

## vamos ordenar a lista de gordice pelo preço do maior para o menor
print(sorted(gordice, key=lambda i: i[1], reverse=True))
