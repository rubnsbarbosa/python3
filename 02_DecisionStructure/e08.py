p1 = float(input('Digite o preco do produto 1: '))
p2 = float(input('Digite o preco do produto 2: '))
p3 = float(input('Digite o preco do produto 3: '))

def menor_preco(a, b, c):
    if a < b and a < c:
        print('Voce deve comprar o produto 1 que é o mais barato: R$ {}'.format(a))
    elif b < a and b < c:
        print('Voce deve comprar o produto 2 que é o mais barato: R$ {}'.format(b))
    elif c < a and c < b:
        print('Voce deve comprar o produto 3 que é o mais barato: R$ {}'.format(c))

menor_preco(p1, p2, p3)
