def jogador(n= '<desconhecido>', g= 0):
        print(f"O jogador {n} fez {g} gols no campeonato.")


# PROGRAMA PRINCIPAL
nome = str(input("Nome do jogador: "))
gols = str(input("Número de gols: "))

if gols.isnumeric():          # pergunta se o valor é número ou não
    gols = int(gols)          # retorna True ou False
else:
    gols = 0
if nome.strip() == '':
    jogador(g = gols)
else:
    jogador(nome, gols)
