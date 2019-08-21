ano = int(input('Digite um ano: '))

def isLeap(a):
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        return True
    return False

def showMessage(r):
    if r == True:
        print('Este ano é bissexto!')
    elif r == False:
        print('Este ano nao é bissexto!')

result = isLeap(ano)
showMessage(result)
