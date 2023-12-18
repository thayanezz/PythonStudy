from time import sleep
print("Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem."
      "\nSeu programa tem que realizar três contagens através da função criada:"
      "\na) De 1 até 10 de 1 em 1;"
      "\nb) De 10 até 0 de 2 em 2;"
      "\nc) Uma contagem personalizada.")
print('=-'*30)
def contador(i,f,p):
    print(f'Contagem de {i} a {f} em {p}')
    cont= i
    while cont <= f:
        print(f'{cont}', end= ' ')
        sleep(0.5)
        cont += p


contador(0,10, 2)
print(' ')
print('=-'*30)
def contador(i, f, p):
    print(f'\nContagem de {i} até {f} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end= ' ')
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end= ' ')
            sleep(0.5)
            cont -= p

contador(10, 0, 2)
print()
print('=-'*20)
def contador (i, f, p):
    print(f'Contagem de {i} a {f} de {p} em {p}')
    inicio = i
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        while inicio <= f:
            print(f"{inicio}", end=" ")
            sleep(0.5)
            inicio += p
    else:
        while inicio >= f:
            print(f"{inicio}", end=" ")
            sleep(0.5)
            inicio -= p

print("CONTAGEM PERSONALIZADA")
i= int(input("INÍCIO: "))
f= int(input("FINAL:  "))
p= int(input("PASSO:  "))
contador(i, f, p)
