# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#    Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input('Digite quanto vc ganha por hora: '))
numt_horas = float(input('Digite o numero de horas trabalhadas no mes: '))
salario = ganho_hora * numt_horas
print('Seu salario eh: {}'.format(salario))
