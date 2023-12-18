print('-'*25)
print('CADASTRO DE PESSOAS')
print('-'*25)
quant= quantm = quantf=  0
while True:
	idade= int(input('Qual a idade: '))
	sexo= input('Sexo: [M/F] ').upper().strip()
	print('-'*25)
	conti= input('Quer continuar? [S/N] ').upper().strip()
	print('-'*25)
	if idade > 18:
		quant+= 1
	if sexo == 'M':
		quantm+= 1
	if sexo == 'F':
		if  idade < 20:
			quantf+= 1
	if conti == 'N':
		break
print('-'*20)
print(f'A quantidade de pessoas que têm mais de 18 anos é de {quant} pessoas.')
print(f'A quantidade de homens cadastrados é de {quantm} homens.')
print(f'A quantidade de mulheres menores de 20 anos é de {quantf} mulheres.')