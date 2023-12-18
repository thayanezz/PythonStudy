import re

file = open('TextoCourseraSUM.txt.txt', 'r')
contents= file.read()
search= re.findall (r'\d+', contents)
numint= [int(num) for num in search]
soma= sum(numint)
print(f'A soma total é de {soma}')

for num in search:
    inteiro= int(num)
    print(num)