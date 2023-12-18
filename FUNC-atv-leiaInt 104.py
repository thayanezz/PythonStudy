def leiaInt(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            ok = True
        else:
            print(f"\033[0;34mERRO! DIGITE UM NÚMERO VÁLIDO: \033[m")
        if ok:
            break
    return n

n= leiaInt('Digite um número: ')
print(f"Você acabou de digitar o número {n}")


