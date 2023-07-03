from random import randint
from time import sleep
megasena = []
print("=-="*10)
print(f"{'Jogo da megasena':^30}")
print("=-="*10)

palpites = int(input("Quantos jogos serão jogados? "))

print(f"=-=-= Sorteando {palpites} jogos =-=-=")
for c in range(0,palpites):
  megasena = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),
              randint(1,60),randint(1,60)]
  megasena.sort()

  sleep(1)
  print(megasena)
sleep(1)
print("=-=" * 10)
print(f"{'< Boa sorte! >':^30}")
print("=-=" * 10)