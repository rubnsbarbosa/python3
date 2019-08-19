x, y, z = map(int,input().split())

def maior(a, b, c):
    if a > b and a > c:
        print('{} eh o maior'.format(a))
    elif b > a and b > c:
        print('{} eh o maior'.format(b))
    elif c > a and c > b:
        print('{} eh o maior'.format(c))

def menor(a, b, c):
    if a < b and a < c:
        print('{} eh o menor'.format(a))
    elif b < a and b < c:
        print('{} eh o menor'.format(b))
    elif c < a and c < b:
        print('{} eh o menor'.format(c))

maior(x,y,z)
menor(x,y,z)
