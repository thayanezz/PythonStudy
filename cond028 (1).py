import random
from time import sleep
esc= int(input('Escolha um número de 0 a 5:'))
print ('PROCESSANDO...')
sleep (3)
num= [0,1,2,3,4,5]
nam= random.choice(num)
if nam == [0,1,2,3,4,5]:
	print ('Você acertou. Parabéns!')
else :
	print ('Você errou! O número correto é {}.'.format(nam))

#outra forma
#computador = randint (0,5)
