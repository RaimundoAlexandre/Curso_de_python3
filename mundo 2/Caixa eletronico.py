print("##### Banco Dev #####\n")
#celudas de 50, 20, 10 e 1
valor = int(input("Quanto deseja sacaR$ "))
total = valor
cedula = 50
cont = 0
print(f"O valor sacado foi R${valor}")
while True:
  if total >= cedula:
     total -= cedula
     cont += 1
  else:
    if cont > 0:
      print(f"Sera entrege em {cont} dedulas de R${cedula}")
    if cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    cont = 0
    if total == 0:
      break
