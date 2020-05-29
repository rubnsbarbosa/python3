f = open('arqsort.txt', 'r')

elementos = f.readlines()
for x in elementos:
	vetor = x.split() #Separando os elementos do vetor
	vetor = [int(x) for x in vetor] #Transformando os elementos do vetor de string para inteiro

def quicksort(L):
    if L == []: return []
    return quicksort([x for x in L[1:] if x< L[0] ]) + L[0:1] + quicksort([x for x in L[1:] if x>=L[0] ])

resp = map(quicksort, [vetor])
resp = resp[0]
print (resp)
