dados=dict()
dados['nome']=str(input('Qual o nome do aluno a ser cadastrado? '))
dados['média']=float(input('Qual a média do aluno? '))
print('=-' * 30)

if  dados['média'] <= 5:
    dados['situação']='REPROVADO'
elif 5 < dados['média'] < 7:
    dados['situação']='RECUPERAÇÃO'
else:
    dados['situação']='APROVADO'

print(f'A situação do aluno {dados["nome"]} é {dados["situação"]}')
print(f'Sua média nessa disciplina é {dados["média"]}')
