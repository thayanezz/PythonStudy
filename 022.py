frase= input('Digite seu nome')
#frase= (frase.upper())
#print ('Seu nome é {}.'.format(frase))
print ('Seu nome em maiúsculas é {}.'.format(frase.upper()))

#frase= (frase.lower())
print ('Seu nome é {}.'.format(frase.lower()))

#semesp= (frase.replace(' ', ''))
#carac= len(semesp)
print ('Seu nome tem {} caracteres.'.format(len(frase)- frase.count(' ')))

#nomecomp= (frase.split()[0])
#prim= (len(nomecomp))
print ('Seu primeiro nome tem {} letras.'.format(frase.find(' ')))

#Pode ser também

separa= frase.split()
print ('Seu segundo nome tem {} letras.'.format(len(separa[1])))