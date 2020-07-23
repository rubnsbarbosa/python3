def sintax():
    #This is a comment.
    print("Hello, world!")

    """This is a
    multiline docstring."""

    year = 2020 # year is of type int
    name = "Rubens Barbosa" # name is of type String
    print(name)
    print(year)

    x = "awesome"
    print("Python is " + x)

    x = "Computer "
    y = "Science"
    z = x + y
    print(z)

    x = 5
    y = 10
    print(x + y)

sintax()

def hello():
    print('hello world')

hello()
hello()

def welcome(msg, name):
    print(msg, name)

welcome('welcome', 'rubens')

lista = [1, 2, 3, 4, 5, 6]
def get_odd(l):
    list_odd = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            list_odd.append(l[i])

    return list_odd

print(get_odd(lista))

def division(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

d = division(4, 2)
print(d)

def summation(a, b, c):
    return a + b + c

print(summation(1,2,3))


def porcentagem(num, por):
    aux = num * (por / 100)
    return num + aux

print(porcentagem(15, 10))

# ======== args/kwargs ======== #
def func(*args):
    print(args)

n1, n2, *n = lista
func(n1, n2, n)

def fun(*args):
    for i in args:
        print(i)

fun(lista)

lista2 = [10, 20, 30, 40, 50]

def f(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])

    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade nao existe')

f(*lista, *lista2, nome='Rubens', sobrenome='Barbosa', idade=20)

# ======== escopo de variaveis ======== #

# escopo global
var = 'valor X'

def func_var_global():
    print(var)

def func_var_local():
    # escopo local (essa var só existe dentro da funcao)
    var = 'valor Y'
    print(var)

## isso nao eh uma boa pratica de programacao
## pra eu poder mudar o valor de uma variavel global dentro de uma funcao temos que fazer assim:
def func_change_var_global():
    global var
    var = 'valor W'
    print(var)

func_var_global()
func_var_local()
func_change_var_global()
## perceba que agora var = valor W
## e nao mais var = valor X
print(var)

'''
Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada
'''
def f2():
    print('function 2')

def f1(function):
    return function()

f1(f2)

def ola(nome, maisculo=False):

    if maisculo:
        msg = f"Olá, {nome}".upper()
    else:
        msg = f"Olá, {nome}"

    print(msg)

ola("Grad")
ola("Groove", maisculo=True)