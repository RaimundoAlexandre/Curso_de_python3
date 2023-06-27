n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
print("=-="*10)
maior = 0
while True:
  menu = int(input("""  [1]Soma
  [2]Multiplicar
  [3]maior
  [4]Novos valores
  [5]sair\n"""))
  if menu == 1:
    print(f"{n1} + {n2} = {n1 + n2}")
    print("=-="*10)
  elif menu == 2:
    print(f"{n1} x {n2} = {n1 * n2}")
    print("=-="*10)
  elif menu == 3:
    if n1 >= n2:
      maior = n1
      print(f"O maior valor é {maior}")
      print("=-="*10)
    else:
      maior = n2
      print(f"O maior valor é {maior}")
      print("=-="*10)
  elif menu == 4:
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    print("=-="*10)
  elif menu == 5:
    break
  else:
    print("Valor invalido! \nTente novamente")
print("FIM")
