"""
matriz = []
soma_p = 0
soma_c = 0
for c in range(0, 9):
  dado = int(input(f"Digite {c}° valor: "))
  if c == 3:
    maior = dado
  if c == 4 or c == 5:
    if dado > maior:
      maior = dado
  if c == 2 or c == 5 or c == 8:
    soma_c += dado
  if dado % 2 == 0:
    soma_p += dado
  matriz.append([dado])
print("=-="*10) 

for c in range(0,3):
  print(f"{matriz[c]}",end='')
print()

for c in range(3,6):
  print(f"{matriz[c]}",end='')
print()

for c in range(6,9):
  print(f"{matriz[c]}",end='')
print()
print("=-="*10)

print(f"A soma dos números pares é {soma_p}")
print(f"A somo dos valores da terceira coluna e {soma_c}")
print(f"O maior valor da segunda coluna é {maior}")
"""
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = maior = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um número para a  posiçãp {l} {c}: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]",end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f"A soma dos valores pares é {spar}")

for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valres da terceira coluna é {scol}")

for c in range(0, 3):
    if c == 0:
        mair = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")
