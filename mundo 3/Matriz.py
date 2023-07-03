matriz = []

for c in range(0, 9):
  dado = int(input(f"Digite {c}° valor: "))
  matriz.append([dado])

for c in range(0,3):
  print(f"{matriz[c]}",end='')
print()

for c in range(3,6):
  print(f"{matriz[c]}",end='')
print()

for c in range(6,9):
  print(f"{matriz[c]}",end='')