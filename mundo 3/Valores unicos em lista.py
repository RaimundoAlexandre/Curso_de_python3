numeros = []
while True:
  num = int(input("Digite um valor: "))

  if num not in numeros:
    numeros.append(num)
    print("Valor adicionado com sucesso")
  else:
    print("Valor duplicado não vou adicionar")

  sair = str(input("Quer continuar?[S/N] ")).strip().upper()
  if sair == 'N':
    break
  
print("=-="*10)
print(sorted(numeros))
