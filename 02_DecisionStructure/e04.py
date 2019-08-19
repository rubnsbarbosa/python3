vogal = ['a','e','i','o','u']
consoante = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','x','z','y','w','ç']

letter = input('Digite uma letra: ')

def checkLetter(l):
    if l in vogal:
        print('Letra digitada eh uma vogal')
    elif l in consoante:
        print('Letra digitada eh uma consoante')
    else:
        print('Nao eh vogal nem consoante')

checkLetter(letter)
