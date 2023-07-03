"""
numeros = []

for c in range(1, 8):
  dado = int(input(f"Digite {c}° valor: "))
  if dado % 2 == 0:
    numeros.insert(0, dado)
  else:
    numeros.insert(1, dado)

impar = []
par = []

for p in numeros:
  if p % 2 == 0:
    par.append(p)
  else:
    impar.append(p)
  
impar.sort()
par.sort()

print(numeros)
print(f"Os números pares são {par}")
print(f"Os números impares são {impar}")

"""
numeros = [[],[]]

for c in range(1, 8):
  dado = int(input(f"Digite {c}° valor: "))
  if dado % 2 == 0:
    numeros[0].append(dado)
  else:
    numeros[1].append(dado)
    
numeros[0].sort()
numeros[1].sort()

print(f"Os pares são {numeros[0]}")
print(f"Os ímpares são {numeros[1]}")
