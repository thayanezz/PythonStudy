saque= float(input('Quanto você irá sacar? R$'))
ced50= ced20= ced10= ced1= 0
while True:
	if saque >= 50:
		saque -= 50
		ced50+= 1
	else:
		if saque >= 20:
			saque -= 20
			ced20 += 1
		else:
			if saque >= 10:
				saque -= 10
				ced10 += 1
			else:
				saque >= 1
				saque -= 1
				ced1 += 1
		if saque == 0:
			break
	
print(f'Você receberá {ced50} notas de R$50,00, {ced20} notas de R$20,00, {ced10} notas de R$10,00 e {ced1} notas de R$1,00.')