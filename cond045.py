from random import randint
from time import sleep
itens= ('PEDRA', 'PAPEL', 'TESOURA')
comp= randint(0 , 3)
print ('Suas opções: \n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jog= int(input ('Escolha uma opção'))
print ('...')
sleep(1)
print('=-'*15)
if jog == 0:
	if comp == 0:
		print ('EMPATE')
	elif comp == 2:
		print ('JOGADOR GANHOU')
	else:
		print ('COMPUTADOR GANHOU')
elif jog == 1:
	if comp == 1:
		print('EMPATE')
	elif comp == 0:
		print ('JOGADOR GANHOU')
	else:
		print('COMPUTADOR GANHOU')
elif jog == 2:
	if comp == 2:
		print ('EMPATE')
	elif comp == 0:
		print ('JOGADOR GANHOU')
	else:
		print('COMPUTADOR GANHOU')
else:
	print('OPÇÃO INVÁLIDA')
print('=-'*15)
print('Você escolheu {}'.format(itens[jog]))
print('O computador escolheu {}'.format(itens[comp]))