from random import randint
numeros= list()
def sorteio(lista):
    for c in range(0,5):
        lista.append(randint(1,10))
    print(f'Os valores sorteados foram {lista}.', end=" ")

def somaPar(lista):
    soma=0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma de todos os valores pares sorteados entre {numeros} é {soma}')

sorteio(numeros)
somaPar(numeros)