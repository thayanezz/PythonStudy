nome=str(input("Qual o nome do produto? "))
preço= float(input("Qual o preço desse produto?"))
quant= int(input("Qual a quantidade de produto? "))
tot = preço * quant
if quant <= 10:
    print("Não tem desconto até essa quantidade de produtos.")

elif  10 < quant <= 20:
    desc10 = tot-(tot*0.10)
    print(f"O valor total do produto é {tot:.2f}, mas com o desconto de 10% o valor de {quant} {nome} passa a ser {desc10:.2f}")

elif 20 < quant <=50:
    desc10 = tot-(tot*0.20)
    print(f"O valor total do produto é {tot:.2f}, mas com o desconto de 20% o valor de {quant} {nome} passa a ser {desc10:.2f}")

else:
    desc10 = tot-(tot*0.25)
    print(f"O valor total do produto é {tot:.2f}, mas com o desconto de 25% o valor de {quant} {nome} passa a ser {desc10:.2f}")
