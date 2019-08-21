hour_value = float(input('Digite o valor da hora de trabalho: '))
qtde_hours = float(input('Digite a qtde de horas trabalhadas: '))

salario_bruto = (hour_value * qtde_hours)

def desconto(s):
    if s <= 900:
        print('\nSalário Bruto ({} * {}): {}\n(-) IR isento.'.format(hour_value, qtde_hours, salario_bruto))
        inss = s * 0.1
        s = s - inss
        fgts = s * 0.11
        print('(-) INSS (10%): {}\nFGTS (11%): {}\nTotal de descontos: {}\nSalario Liquido: {}'.format(inss, fgts, inss, s))
    elif s > 900 and s <= 1500:
        print('\nSalário Bruto ({} * {}): {}'.format(hour_value, qtde_hours, salario_bruto))
        fgts = s * 0.11
        ir = s * 0.05
        inss = s * 0.1
        desconto = (ir + inss)
        s = s - desconto
        print('(-) IR (5%): {}.\n(-) INSS (10%): {}\nFGTS (11%): {}\nTotal de descontos: {}\nSalario Liquido: {}'.format(ir, inss, fgts, desconto, s))
    elif s > 1500 and s <= 2500:
        print('\nSalário Bruto ({} * {}): {}'.format(hour_value, qtde_hours, salario_bruto))
        fgts = s * 0.11
        ir = s * 0.1
        inss = s * 0.1
        desconto = (ir + inss)
        s = s - desconto
        print('(-) IR (10%): {}.\n(-) INSS (10%): {}\nFGTS (11%): {}\nTotal de descontos: {}\nSalario Liquido: {}'.format(ir, inss, fgts, desconto, s))
    elif s > 2500:
        print('\nSalário Bruto ({} * {}): {}'.format(hour_value, qtde_hours, salario_bruto))
        fgts = s * 0.11
        ir = s * 0.2
        inss = s * 0.1
        desconto = (ir + inss)
        s = s - desconto
        print('(-) IR (20%): {}.\n(-) INSS (10%): {}\nFGTS (11%): {}\nTotal de descontos: {}\nSalario Liquido: {}'.format(ir, inss, fgts, desconto, s))

desconto(salario_bruto)
