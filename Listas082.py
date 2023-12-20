lista= []
listapar= []
listaimpar=[]
while True:
	num= int(input('Digite um número: '))
	lista.append(num)
	cont= str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
	if num % 2 == 0:
		listapar.append(num)
		listapar.sort()
	else:
		listaimpar.append(num)
		listapar.sort()
	if cont in 'Nn':
		break

print(lista)
print(f'Os números Pares são {listapar}')
print(f'Os números Ímpares são {listaimpar}')