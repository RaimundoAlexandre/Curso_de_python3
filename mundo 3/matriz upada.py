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
