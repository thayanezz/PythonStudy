#UM MANUAL DE INSTRUÇÕES DENTRO DO PRÓPRIO PYTHON
#USA O COMANDO help()
#help(print)

#OUTRA FORMA
#print(input.__doc__)

#DOCSTRINGS
def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: início a contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end= " ")
        c += p

contador(0, 10, 2)

help(contador)

#PARÂMETROS OPCIONAIS

def soma(a=0, b=0, c=0):                     #Caso qualquer parâmetro não receba valor coloca = 0 para não dar erro
    s = a + b + c                          #Pode colocar em todos também
    print(f'A soma {a} + {b} + {c} = {s}')

soma(2,4,3)
soma(4,7)
soma()

#ESCOPO DE VARIÁVEIS

def valor():
    x = 4
    print(f'Nesse lugar a variável x vale {x}')


#PROGRAMA PRINCIPAL
n = 2
print(f'A variável n no programa principal vale {n}')
valor()
#print(f'A variável x vale {x}')   #AQUI VAI DAR ERRO PORQUE A VARIÁVEL x ESTÁ DETERMINADA APENAS NA FUNÇÃO valor()

# VARIÁVEL GLOBAL

def teste(b):
    global a                   #O "a" PASSA A VALER SÓ 8 AGORA
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'O A fora vale {a}')

#RETORNO DE VALORES (return)

def soma(a=0, b=0 , c=0):
    s = a + b + c
    return s

resul= soma(1,4,2,), soma(5,6,3)
print(f"Os resultados foram {resul}")
       #ou
print(soma(5,3,1))

# PODE RETORNAR VALORES VERDADEIROS OU FALSOS

def par(n=1):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número para saber se é par: "))

if par(num):
    print("É PAR!")
else:
    print("É ÍMPAR!")