#Listas são mutáveis
lanche= ['cenoura', 'batata', 'macarrão','maxixe']
print(lanche)

#Adiciona elemento no final da lista
lanche.append('arroz')
lanche.append('feijão')
print(lanche)

#Adiciona em qualquer lugar que pedir
lanche.insert(0,'cachorro-quente')
print(lanche)

#Deletar um item específico
del lanche[1] #é uma declaração que pode até remover uma lista inteira
print(lanche)

removido= lanche.pop() #quando vazio remove o último
print(removido)

#usando if para não dar erro
lanche.append('pizza')
print(lanche)
if 'pizza' in lanche:
    lanche.remove('pizza')

#criar uma lista com números
valores= list(range(0,10))
print(valores)

#ordena do valor menor para o maior
desor= [9,4,7,2,0,3,8,2]
print(desor)
desor.sort()
print(desor)

#ordena do maior para o menor
desor.sort(reverse=True)
print(desor)

len(desor)

#copiando uma lista
a= [3,6,2,9,7,5]
print(a)

b=a[:] #copia os valores de 'a'
b[3]=8 #troca um número na posição 3 por 8
print(b)

#criar uma lista com for inserindo valores pelo usuário

nomes= list()
for c in range(1,2):
    nomes.append(input('Qual o nome que deve ser cadastrado? '))
print(nomes)

#Usando for para determinar a posiçao de um nome

for c,v in enumerate(nomes):
    print(f'Na posição {c} encontrei o nome {v}')


#lista dentro da lista

dados=list()
pessoas=list()

for c in range(0,4):
    dados.append(input('Qual o seu nome? '))
    dados.append(int(input("Qual a sua idade? ")))
    dados.append(input('Qual a sua profissão? '))
    pessoas.append(dados[:])
    dados.clear() #apaga a lista dados e deixa sóa de pessoas
print(pessoas)

#mostra o que está dentro de uma lista em outra lista
print(pessoas[1][2])