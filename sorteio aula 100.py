from random import randint
numeros= list()
def sorteio(lista):
    for num in range(0,5):
        lista.append(randint(1,10))
    print(numeros)
sorteio(numeros)