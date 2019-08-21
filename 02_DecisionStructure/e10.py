turno = input('Digite o turno que voce estuda conforme descrito abaixo\nM - matutino\nV - Vespertino\nN - Noturno\n')

if turno == 'M' or turno == 'm':
    print('Bom Dia!')
elif turno == 'V' or turno == 'v':
    print('Boa Tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa Noite')
else:
    print('Valor Inválido!')
