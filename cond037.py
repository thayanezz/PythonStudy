num= int(input('Digite um número: '))
op= input('Escolha umas das bases para conversão:\n[ 0 ] Converter para BINÁRIO\n[ 1 ] Converter para OCTAL\n[ 2 ] Converter para HEXADECIMAL')
opção= int(input('Digite sua opção: '))
if opção == 0:
	print('{}'.format(bin(num)))
elif opção == 1:
	print  ('{}'.format(octa(num)))
elif opção == 3:
	print ('{}'.format(hexa(num)))
else:
	print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')