from random import randint
from time import sleep
from operator import itemgetter
dado= dict()
dado['jogador 1']= randint(1,6)
dado['jogador 2']= randint(1,6)
dado['jogador 3']= randint(1,6)
dado['jogador 4']= randint(1,6)
print('Valores sorteados: ')
c=1
for k, v in dado.items():
    print(f'{k} tirou {v} nos dados')
    sleep(1)
ranking= dict( sorted(dado.items(), key=lambda item:item[1], reverse=True))
for k, v in ranking.items():
    print(f'{c}o. lugar: {k} com {v}.')
    c+=1



