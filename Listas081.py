t= 0
lista= []
while True:
	n= lista.append(int(input('Digite um número: ')))
	cont= input('Quer continuar? [S/N] ').upper().strip()
	t+=1
	
	if cont == 'N':
		break
print(lista)
print(f'O total de valores em lista é {t}')
lista.sort(reverse= True)
print(lista)

if 5 in lista:
	print(f'O número 5 está na lista')
else:
	print('O número 5 não está na lista')
