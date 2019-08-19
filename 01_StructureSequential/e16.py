# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_quadrada = float(input('Digite o tamanho em metros quadrados da area a ser pintada: '))
qtde_litros = area_quadrada / 3
qtde_latas  = qtde_litros / 18
preco_total = qtde_latas * 80

print('A qtde de latas de tinta a serem compradas: {}\nPreco total: {}'.format(qtde_latas, preco_total))
