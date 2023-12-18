fut= dict()
partidas= list()
fut['nome']=str(input('Qual o nome do jogador? '))
totpart= int (input('Quantas partidas ele jogou? '))

for c in range(0,totpart):
    partidas.append(int(input(f'Quantos gols ele fez na partida {c+1}? ')))
fut['golspart']= partidas[:]
fut['totalgols']= sum(partidas)

print('=-'*30)
print(fut)
print('=-'*30)
for k,v in fut.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*30)

print(f'O jogador {fut["nome"]} jogou {totpart} partidas')
for i, v in enumerate(fut['golspart']):
    print(f"Na partida {i+1}, fez {v} gols")

