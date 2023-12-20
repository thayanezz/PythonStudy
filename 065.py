'''tot= 0
n=1
s= 0
while n != 0:
	n= int(input('Digite um número para saber a sua média (digite 0 para sair): '))
	if n != 0:
		tot+= 1
		s+= n
		media= s/tot
print('A média é {}. '.format(media))
print('Encerrando o programa.')'''

#Outra forma

resp= 'S'
soma = tot = maior= menor= 0
while resp in 'S':
	num= int(input('Digite um número: '))
	soma += num
	tot+= 1
	if tot == 1:
		maior = menor = num
	else:
		if num > maior:
			maior = num
		if num < menor:
			menor= num
	resp= (input('Você quer continuar? S/N')).strip().upper() [0]
media= soma/tot
print('A média é {}'.format(media))
print('O maior é {} e o menor é {}'.format(maior,menor))