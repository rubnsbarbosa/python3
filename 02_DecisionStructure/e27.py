kg_morango = int(input('Digite quantos quilos de morango voce comprou: '))
kg_macas = int(input('Digite quantos quilos de maças voce comprou: '))

res = kg_morango + kg_macas

if res > 8:
    if kg_morango > 5:
        val_morango = kg_morango * 2.2
    else:
        val_morango = kg_morango * 2.5

    if kg_macas > 5:
        val_macas = kg_macas * 1.5
    else:
        val_macas = kg_macas * 1.8

    tot = val_morango + val_macas
    if tot > 25:
        print('Valor a pagar: {}'.format( tot - (tot * 0.1) ))
    else:
        print('Valor a pagar: {}'.format( tot ))

else:
    if kg_morango > 5:
        val_morango = kg_morango * 2.2
    else:
        val_morango = kg_morango * 2.5

    if kg_macas > 5:
        val_macas = kg_macas * 1.5
    else:
        val_macas = kg_macas * 1.8

    print('Valor a pagar: {}'.format(val_morango + val_macas))
