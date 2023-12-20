quant= contador= menor= total =0
barato= ' '
while True:
	nome=str( input('Nome do produto: '))
	preco= float(input('Preço do produto: R$'))
	cont= input('Deseja continuar? [S/N] ').upper().strip()
	contador+=1
	total+= preco
	if preco > 1000:
		quant+= 1
	if contador == 1 or preco < menor:
		menor= preco
		barato = nome
	if cont == 'N':
		break
print (f'Total gasto na sua compra: {total:.2f}')
print(f'Há {quant} produtos que valem mais de R$1000,00.')
print(f'O produto {barato} é o mais barato')
