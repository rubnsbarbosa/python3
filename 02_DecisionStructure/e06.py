n1, n2, n3 = map(int,input().split())

#print(type(n1))
def getBiggester(a, b, c):
    if a > b and a > c:
        print('{} eh o maior'.format(a))
    elif b > a and b > c:
        print('{} eh o maior'.format(b))
    elif c > a and c > b:
        print('{} eh o maior'.format(c))

getBiggester(n1, n2, n3)
