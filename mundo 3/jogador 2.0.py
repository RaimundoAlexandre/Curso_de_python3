jogador = {}

jogador['nome'] = str(input("Nomes: ")).strip().capitalize()
partidas = int(input(f"Quantas Partidas o {jogador['nome']} jogou? "))
gols = []
total = 0

for c in range(0, partidas):
  g = int(input(f"Quantos gols na partida {c} "))
  gols.append(g)
  total += g
  jogador['gols'] = gols

jogador['total'] = total

print("=-="*10)
print(jogador)
print("=-="*10)

for k, v in jogador.items():
  print(f"O campo {k} tem valor {v}")
print("=-="*10)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas")

for i, v in enumerate(gols):
  print(f"Na partida {i}, fez {v} gols")
  
print(f"Total de {total} gols")
