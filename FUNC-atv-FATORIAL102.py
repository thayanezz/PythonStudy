from math import factorial
def fatorial(f, show = False):             #No entanto, na definição da função, show está sendo definido como False por padrão.
                                           # Isso significa que, se você não passar um valor explicitamente para show na chamada da função,
                                           # ele assumirá o valor padrão de False.
    '''

    :param f: NUMERO A SER FATORADO
    :param show: SE DESEJA MOSTRAR A OPERAÇÃO FATORIAL
    :return: RETORNA O RESULTADO DA OPERAÇÃO FATORIAL
    '''
    fat = 1
    for c in range(f, 0, -1):
        if show:
            print(f"{c}", end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat *= c
    return fat

print(fatorial(5, show= True))