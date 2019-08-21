salario = float(input('Digite o seu salario atual: '))

def reajuste(s):
    if s <= 280:
        print('\nSalario antes do reajuste: {}\nPercentual de aumento aplicado: 20%'.format(s))
        reaj = s * 0.2
        s = s + reaj
        print('Valor do aumento: {}\nNovo salario: {}'.format(reaj, s))
    elif s > 280 and s < 700:
        print('\nSalario antes do reajuste: {}\nPercentual de aumento aplicado: 15%'.format(s))
        reaj = s * 0.15
        s = s + reaj
        print('Valor do aumento: {}\nNovo salario: {}'.format(reaj, s))
    elif s >= 700 and s < 1500:
        print('\nSalario antes do reajuste: {}\nPercentual de aumento aplicado: 10%'.format(s))
        reaj = s * 0.1
        s = s + reaj
        print('Valor do aumento: {}\nNovo salario: {}'.format(reaj, s))
    elif s >= 1500:
        print('\nSalario antes do reajuste: {}\nPercentual de aumento aplicado: 5%'.format(s))
        reaj = s * 0.05
        s = s + reaj
        print('Valor do aumento: {}\nNovo salario: {}'.format(reaj, s))

reajuste(salario)
