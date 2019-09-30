valor = int(input('Digite o valor do saque: '))

def encontra_notas(v):
    cent = (v / 100)
    cinq = cent % 1
    cinq = cinq * 100
    dez = cinq % 50
    cinq = cinq / 50
    dez = dez / 10
    cinco = dez * 10

    aux = ''.join(str(int(cinco)))
    aux = (int(len(aux)))
    if aux > 1:
        cinco = cinco / 5
        cinco = cinco / 5
        v_aux = (int(cent) * 100) + (int(cinq) * 50) + (int(dez) * 10) + (int(cinco) * 5)
        print('R$ {} = {} notas de 100, {} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1'.format(v, int(cent), int(cinq), int(dez), int(cinco), (v - v_aux) ))
    else:
        cinco = cinco / 5
        v1_aux = (int(cent) * 100) + (int(cinq) * 50) + (int(dez) * 10) + (int(cinco) * 5)
        print('R$ {} = {} notas de 100, {} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1'.format(v, int(cent), int(cinq), int(dez), int(cinco), (v - v1_aux) ))

encontra_notas(valor)
