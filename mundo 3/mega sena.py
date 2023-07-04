from random import randint
from time import sleep

megasena = []
print("=-=" * 10)
print(f"{'Jogo da megasena':^30}")
print("=-=" * 10)

palpites = int(input("Quantos jogos serão jogados? "))

print(f"=-=-= Sorteando {palpites} jogos =-=-=")
for c in range(palpites):
    megasena = []
    while len(megasena) < 6:
        numero = randint(1, 60)
        if numero not in megasena:
            megasena.append(numero)
    megasena.sort()

    sleep(1)
    print(megasena)

sleep(1)
print("=-=" * 10)
print(f"{'< Boa sorte! >':^30}")
print("=-=" * 10)
