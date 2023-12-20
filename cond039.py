from datetime import date
'''print('=-'*15)
print ('\033[1;33mAlistamento Obrigatório\033[m')
print('=-'*15)
idade = int(input('Qual é a sua idade?'))
idade1= 18-idade
idade2= idade -18
if idade < 18:
	print ('Ainda não está na hora de você se alistar no Exército Brasileiro. Ainda faltam \033[1;32m{} anos\033[m para você se alistar.Talvez na próxima!'.format(idade1))
elif idade == 18:
	print('É a hora de você se alistar! Vá para uma base mais próxima')
else:
	print('Já se passaram \033[31m{} anos\033[m do seu alistamento'.format(idade2))'''
	
#outra forma

atual= date.today().year
nasc= int(input('Ano de nascimento: '))
idade= atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade ==18:
	print('Você tem que se alistar IMEDIATAMENTE')
elif 