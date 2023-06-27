print("##### Calculadora #####\n")
while True:
  n1 = float(input("Digite o primeiro número: "))
  n2 = float(input("Digite o segundo número: "))
  print("Escolha uma das seguintes opções")
  menu = int(input("[1]Somar\n[2]Multiplica\n[3]maior\n[4]Novos valores\n[5]Saior: "))
  print("=-="*10)
  if menu == 1:
    print(f"{n1} + {n2} = {n1+n2}")
  elif menu == 2:
    print(f"{n1} x {n2} = {n1*n2}")
  elif menu == 3:
    if n1 > n2:
      print(f"O maior valor é {n1}")
    else:
      print(f"O maior valor é {n2}")
  elif menu == 5:
    break
