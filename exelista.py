pessoas= list()
dados= list()

while True:
	dados.append(input('Digite um nome: '))
	dados.append(input('Digite a idade: '))
	pessoas.append(dados[:])
	cont= input('Deseja continuar? ').strip().lower()
	dados.clear() #APAGA A LISTA DADOS E DEIXA SÓ A MAIOR 'PESSOAS'#
	if cont in 'Nn':
		break
print(pessoas)
