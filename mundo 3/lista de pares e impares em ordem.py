valores = []

for c in range(0,7):
  num = int(input("Digite um valor: "))
  valores.append(num)

par = []
impar = []

for c in valores:
  if c % 2 == 0:
    par.append(c)
  else:
    impar.append(c)

par.sort()
impar.sort()

print("=-="*10)
print(f"Os valores pares são {par}")
print(f"Os valores pares são {impar}")