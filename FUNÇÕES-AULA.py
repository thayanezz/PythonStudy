#Cria uma funçao personalizada no python
def mostralinha():
    print("=-" *20)

mostralinha()
print("       CADASTRO DE ESTUDANTES       ")
mostralinha()

#MENSAGEM PROGRAMADA
def título(msg):
    print("-="*30)
    print(msg)
    print("-="*30)

título("     PYTHON É O MELHOR PROGRAMA DE TODOS")

# SOMANDO NÚMEROS
def soma(a, b): # a e b são os parâmetros
    s= a + b
    print(F"A soma entre {a} e {b} tem o resultado = {s}")
    print("-=" * 20)

soma(3,6)
soma(4,9)
soma(a=23, b=5) # PODE EXPLICITAR QUAL É QUAL, PODE TROCAR AS LETRAS ENTRE OS PARÂMETROS DEFINIDOS

#EMPACOTAR PARAMETROS

def contador(* num):#AVISA PRO PYTHON QUE VAI RECEBER PARÂMETROS
    print(num)

contador(9, 7 , 5) #ENVIA ESSES VALORES EM FORMA DE TUPLA
contador(3, 4, 1)
contador(6, 8)

#USANDO O COMANDO FOR
def contador(* num):
    for valor in num:
        print(valor, end=" ")

contador(3,5,2)
contador(7,4,2)

# MEDINDO TAMANHO DE UM EMPACOTAMENTO
def contador(* num):
    tam= len(num)
    print(f'\nOs valores que recebi foram {num} e são ao todo {tam} números')
contador(8,3,2)
contador(2,7,3,5)

#DOBRANDO VALORES DE UMA LISTA

def dobra(lst):
    pos= 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores =[4, 6, 9, 0, 4]
dobra(valores)
print(valores)
