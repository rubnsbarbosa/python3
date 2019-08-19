letter = input('Digite F ou M: ')

def checkLetter(l):
    if l == 'F':
        print('F - Feminino')
    elif l == 'M':
        print('M - Masculino')
    else:
        print('Sexo Invalido')

checkLetter(letter)
