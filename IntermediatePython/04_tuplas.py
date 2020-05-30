## a diferença da tupla com a lista é que vc não pode editar os elementos
## vc nao pode add elementos, remover elementos, mudar o valor de um indice de uma tupla

tuple1 = (1, 2, 3, 'A', 'Rubens')

for i in tuple1:
    print(i)

## criando tupla com um valor e sem parentesis
t1 = 1
t2 = 2,

print(t1, type(t1))
print(t2, type(t2))

## concatenando tuplas
t3 = 1,2,3,4,5
t4 = 6,7,8,9,10
t5 = t3 + t4
print(t5)

## desempacotando uma tupla
n1, n2, n3, *_ = t5
print(*_)

## convertendo tupla em lista
tuple1 = list(tuple1)
tuple1[4] = 'Rubens Barbosa'
print(tuple1)

## se eu quiser voltar tuple1 p/ ser tupla:
tuple1 = tuple(tuple1)
print(tuple1)
