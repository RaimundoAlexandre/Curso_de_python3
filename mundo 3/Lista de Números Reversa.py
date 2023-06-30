numeros = []

while True:
  numeros.append(int(input("Digite um valor: ")))
  sair = str(input("Quer continuar?[S/N] ")).strip().upper()
  if sair == 'N':
    break
print(f"Foram digitados {len(numeros)} números")
print("=-="*10)

numeros.sort(reverse=True)
print(numeros)
print("=-="*10)

if 5 in numeros:
  print("O número 5 foi encontrado na lista")
else:
  print("O numero 5 não foi encontrado na lista")

print("=-="*10)

