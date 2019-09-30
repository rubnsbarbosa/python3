arr = []
r1 = input('Telefonou para a vítima? (s ou n): ')
r2 = input('Esteve no local do crime? (s ou n): ')
r3 = input('Mora perto da vítima? (s ou n): ')
r4 = input('Devia para a vítima? (s ou n): ')
r5 = input('Já trabalhou com a vítima? (s ou n): ')

arr.append(r1)
arr.append(r2)
arr.append(r3)
arr.append(r4)
arr.append(r5)

qtd_pos = arr.count('s')

if qtd_pos == 2:
    print('Suspeita')
elif qtd_pos == 4 or qtd_pos == 3:
    print('Cúmplice')
elif qtd_pos == 5:
    print('Assassino')
elif qtd_pos == 1:
    print('Inocente')
