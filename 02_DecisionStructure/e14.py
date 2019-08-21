n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

def result(m):
    if m <= 10 and m >= 9.0:
        print('n1: {} - n2: {} - media: {}\nAPROVADO - Conceito A'.format(n1, n2, m))
    elif m < 9.0 and m >= 7.5:
        print('n1: {} - n2: {} - media: {}\nAPROVADO - Conceito B'.format(n1, n2, m))
    elif m < 7.5 and m >= 6.0:
        print('n1: {} - n2: {} - media: {}\nAPROVADO - Conceito C'.format(n1, n2, m))
    elif m < 6.0 and m >= 4.0:
        print('n1: {} - n2: {} - media: {}\nREPROVADO - Conceito D'.format(n1, n2, m))
    elif m < 4.0 and m >= 0.0:
        print('n1: {} - n2: {} - media: {}\nREPROVADO - Conceito E'.format(n1, n2, m))
    else:
        print('Notas invalidas!')

result(media)
