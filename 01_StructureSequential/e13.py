# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#       Para homens: (72.7*h) - 58
#       Para mulheres: (62.1*h) - 44.7
h = float(input('Digite a altura (h) de uma pessoa: '))
h_homens = (72.7 * h) - 58
h_mulher = (62.1 * h) - 44.7

print('Com essa altura o peso ideal para homem eh {:.2f} e para mulher eh {:.2f}'.format(h_homens, h_mulher))
