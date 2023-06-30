numeros = []

while True:
  numeros.append(int(input("Digite um valor: ")))
  sair = str(input("Quer continuar?[S/N] ")).strip().upper()
  if sair == 'N':
    break

print("=-="*10)
print(f"Os números digitados foram {numeros}")
print("=-="*10)

par = []
impar = []
for c, p in enumerate(numeros):
  if p % 2 == 0:
    par.append(numeros[c])
  else:
    impar.append(numeros[c])
print(f"Os números pares são {par}")
print("=-="*10)
   
print(f"Os numeros impares são {impar}")
print("=-="*10)
