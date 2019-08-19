num1 = int(input('Digite num1: '))
num2 = int(input('Digite num2: '))

def maior(n1, n2):
    if n1 > n2:
        return n1
    return n2

result = maior(num1, num2)

print('O maior numero eh: {}'.format(result))
