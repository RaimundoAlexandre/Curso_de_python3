time = []
while True:
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
  time.append(jogador.copy())
  
  sair = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
  while not sair in 'SN':
    print("ERRO. Por favor digite apenas S ou N")
    sair = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
  if sair == 'N':
    break
print("=-="*15)
print("Cod ",end='')
for i in jogador.keys():
  print(f"{i:<15}",end='')
print()
print("---"*15)
for k, v in enumerate(time):
  print(f" {k:>3} ",end='')
  for d in v.values():
    print(f"{str(d):<15}",end='')
  print()
print("---"*15)
while True:
  busca = int(input("Mostrar dados de qual jogaro? (999 para parar) "))
  if busca == 999:
    break
  if busca >= len(time):
    print(f"ERRO. Não existe jogador com o codigo {busca}!")
  else:
    print(f"Levantamento do jogador {time[busca]['nome']}:")
    for i, g in enumerate(time[busca]['gols']):
      print(f"   No jogo {i+1} fes {g} gols.")
  print("---"*15)
print("<<< VOLTE SEMPRE >>>")
