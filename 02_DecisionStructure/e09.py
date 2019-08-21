x, y, z = map(int, input().split())

def ordem_decrescente(a, b, c):
    if a < b and b < c:
        print('Ordem decrescente: {} {} {}'.format(a, b, c))
    elif a < c and c < b:
        print('Ordem decrescente: {} {} {}'.format(a, c, b))
    elif b < a and a < c:
        print('Ordem decrescente: {} {} {}'.format(b, a, c))
    elif b < c and c < a:
        print('Ordem decrescente: {} {} {}'.format(b, c, a))
    elif c < a and a < b:
        print('Ordem decrescente: {} {} {}'.format(c, a, b))
    elif c < b and b < a:
        print('Ordem decrescente: {} {} {}'.format(c, b, a))

ordem_decrescente(x,y,z)
