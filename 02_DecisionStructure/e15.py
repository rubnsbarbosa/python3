l1 = float(input('Digite o lado A do triângulo: '))
l2 = float(input('Digite o lado B do triângulo: '))
l3 = float(input('Digite o lado C do triângulo: '))

def isTriangle(a, b, c):
    if (((a + b) > c) > abs(a - b)) or (((a + c) > b) > abs(a - c)) or (((b + c) > a) > abs(b - c)):
        return True
    else:
        return False

def equilateral(a, b, c):
    if a == b == c:
        print('Triângulo Equilátero')

def isosceles(a, b, c):
    if a == b or a == c or b == c:
        print('Triângulo Isósceles')

def scalene(a, b, c):
    if a != b or a != c or b != c:
        print('Triângulo Escaleno')

def sideTriangle(result, a, b, c):
    if result == True:
        equilateral(a, b, c)
        isosceles(a, b, c)
        scalene(a, b, c)
    else:
        print('Os valores digitados nao formam um triangulo')

r = isTriangle(l1,l2,l3)
sideTriangle(r,l1,l2,l3)
