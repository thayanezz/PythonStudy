def maior(* num):
    print('Analisando os valores passados: ')
    maior= menor = tot = 0
    for c in num:
        if c > maior:
            maior = c
        tot+= 1
    print(f'Ao todo foram informados {tot} números e entre esses {num} o maior valor é {maior}.')

maior(-1, 4, 6, -7)
maior(2, 4, 8)
maior(0)