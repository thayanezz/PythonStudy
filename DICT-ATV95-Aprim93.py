jogadores= dict()
partidas= list()
futebol= list()

while True:
    jogadores.clear()
    jogadores['nome']=str(input('Qual o nome do jogador? '))
    totpart= int(input('Quantas partidas ele jogou? '))
    for c in range(0,totpart):
        partidas.append(int(input(f'Quantos gols ele fez na partida {c+1}? ')))
    resp= str(input("Quer continuar? [S/N]")).upper()[0]
    if resp in 'N':
        break
    print()
    futebol.append(jogadores.copy())
print('=-'*30)
print('COD NOME           GOLS             TOTAL')
for p in futebol:
    for i,v in p:
        print(f'')
    print(f'')