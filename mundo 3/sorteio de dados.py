from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
lista = [jogadores.copy()]

print(f"O Jogador1 tirou {jogadores['jogador1']}")
sleep(1)
print(f"O Jogador2 tirou {jogadores['jogador2']}")
sleep(1)
print(f"O Jogador3 tirou {jogadores['jogador3']}")
sleep(1)
print(f"O Jogador4 tirou {jogadores['jogador4']}")
sleep(1)

for jogador in lista:
    for nome, valor in jogador.items():
        if valor == 6:
            print(f"O jogador {nome} ficou em primeiro")
        elif valor == 5:
            print(f"O jogador {nome} ficou em segundo")
        elif valor == 4:
            print(f"O jogador {nome} ficou em terceiro")
        elif valor == 3:
            print(f"O jogador {nome} ficou em quarto")
        elif valor == 2:
            print(f"O jogador {nome} ficou em quinto")
        elif valor == 1:
            print(f"O jogador {nome} ficou em sexto")
