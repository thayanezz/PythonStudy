from datetime import datetime           #PODE IMPORTAR DENTRO DA FUNÇÃO (ECONOMIZA MEMÓRIA)


def voto(v):
    idade = datetime.now().year - v
    falta= 18 - idade
    if 16 <= idade < 18 or idade > 70:
        print(f"Com {idade} anos o voto é FACULTATIVO!")
    elif idade < 16:
        print(f"Com {idade} anos o voto não é permitido!"
              f"\nFaltam {falta} anos para ser obrigatório.")
    else:
        print(f"Com {idade} anos o voto é OBRIGATÓRIO!")


ano= int(input("Qual o ano do seu nascimento? "))
voto(ano)