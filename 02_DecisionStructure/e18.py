dia, mes, ano = map(int, input('Digite uma data no formado dd mm aaaa: ').split())

def check_date(d, m, a):
    if (d >= 1 and d <= 31) and (m >= 1 and m <= 12) and (a >= 1 and a <= 9999):
        print('data válida')
    else:
        print('data inválida')

check_date(dia, mes, ano)
