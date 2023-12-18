pessoas= dict()
galera=list()
soma = media= 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input("Nome a ser cadastado: ")).upper()
    while True:
        pessoas['sexo']= str(input('Sexo: [F/M] ')).upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('Por favor, tente novamente.')
    pessoas['idade']=int(input('Idade: '))
    soma+= pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp= str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Por favor, tente novamente.')
    if resp =='N':
        break
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas')
print('=-'*30)
media= soma/ len(galera)
print(f'B) A média de idade entre eles é {media:5.2f} anos')
print('=-'*30)
print(f'C) As mulheres cadastradas foram ', end= '')
for p in galera:
    if p['sexo']== 'F':
        print(f'{p["nome"]} ', end='')
print()
print('=-'*30)
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] > media:
        print('       ', end='')
        for k,v in p.items():
            print(f' {k} = {v} ', end='')
        print()
print(galera)