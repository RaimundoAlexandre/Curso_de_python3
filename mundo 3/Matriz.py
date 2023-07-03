"""
matriz = []

for c in range(0, 9):
  dado = int(input(f"Digite {c}° valor: "))
  matriz.append([dado])

for c in range(0,3):
  print(f"{matriz[c]:^5}",end='')
print()

for c in range(3,6):
  print(f"{matriz[c]:^5}",end='')
print()

for c in range(6,9):
  print(f"{matriz[c]:^5}",end='')

"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para a  posiçãp {l} {c}: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
