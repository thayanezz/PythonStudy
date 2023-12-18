from datetime import datetime
dados= dict()
print("=-"*30)
print("CADASTRAMENTO PARA APOSENTADORIA POR TEMPO DE SERVIÇO")
print("=-"*30)
dados['nome']=str(input('Qual é o seu nome? '))
nasc=int(input('Qual o ano do seu nascimento? '))
dados['idade']= datetime.now().year-nasc
dados['sexo']=str(input('Qual o seu sexo? (M/F) ')).strip().upper()
dados['CTPS']=int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] != 0:
    dados['contratação']= int(input('Qual o ano de contratação? '))
    dados['salário']= float(input('Qual o valor do salário? '))
    if dados['sexo'] == 'F':
        dados['aposentadoria']= ((dados['contratação']+30) + dados['idade']) - datetime.now().year
    elif dados['sexo']== 'M':
        dados['aposentadoria'] = ((dados['contratação'] + 35) + dados['idade'])  - datetime.now().year

print('=-'*30)
print("DADOS CADASTRADOS NO SISTEMA")
print("=-"*30)
for k,v in dados.items():
    print(f"   -   {k} = {v}")




