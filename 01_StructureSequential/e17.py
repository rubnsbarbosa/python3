# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;

area_quadrada = float(input('Digite o tamanho em metros quadrados da area a ser pintada: '))
qtde_litros = area_quadrada / 6
qtde_latas  = qtde_litros / 18
preco_total_latas = qtde_latas * 80

qtde_galoes = qtde_litros / 3.6
preco_total_galoes = qtde_galoes * 25

print('A qtde de latas de 18 litros de tinta a serem compradas: {}\nPreco total das latas: {}\n\n'.format(qtde_latas, preco_total_latas))
print('A qtde de galoes de 3,6 listros de tinta a serem compradas: {}\nPreco total das latas: {}'.format(qtde_galoes, preco_total_galoes))
