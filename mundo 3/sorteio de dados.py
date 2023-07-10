from random import randint
from time import sleep

jogadores = {}
for c in range(1, 5):
  jogadores[f"jogador {c}"] = randint(1, 6)

for k, v in jogadores.items():
  print(f"O {k} tirou {v}")
  sleep(1)
print("=-="*10)

classificacoes = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

for i, (jogador, pontos) in enumerate(classificacoes, start=1):
    print(f"{i}° lugar {jogador} com {pontos} pontos")
    sleep(1)
  
    sleep(1)
print("=-="*10)
  