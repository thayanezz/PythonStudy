#USA {} OU dict=()

dados={'nome':'Pedro', 'idade':25, 'profissão': 'advogado'}
print(dados)
print(dados['nome'])

#adicionar key com valor
dados['curso']= 'direito'
print(dados)

#deletar uma key
del dados['idade']
print(dados)

#retornar coisas específicas
print(dados.keys())
print(dados.values())
print(dados.items())

#usando for
for k,v in dados.items():
    print(f'A chave {k} tem o valor de {v}')

#Dicionário dentro de uma lista (o dicionário vai ser um elemento da lista)
nome=dict()
estado= dict()
brasil=list()
for c in range(0,3):
    estado['UF']=str(input('Qual o seu estado de origem? '))
    estado['sigla']= str(input('Qual a sigla do seu estado? '))
    brasil.append(estado.copy())
print(brasil)
print(brasil[0])