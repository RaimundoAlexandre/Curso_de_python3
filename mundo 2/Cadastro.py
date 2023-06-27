from time import sleep
print("###### Cadastro ######\n")
m = 0
f = 0
cont = 0
while True:
  sexo = str(input("Qual seu sexo?[M/F] ")).strip().upper()
  if sexo in 'MF':
    try:
      idade = int(input("Qual sua idade?: "))
    except ValueError:
      print("Entrada invalida: a idade deve ser um valor numérico.")
    sair = str(input("Quer continuar?[S/N]\n")).strip().upper()[0]
    if idade > 18:
      cont += 1
    if sexo == 'M':
      m += 1
    if sexo == 'F':
      if idade < 20:
        f += 1
    if sair in 'SN':
      if sair == 'N':
        break
    else:
      print("Entreda invalida: digite [N] pra sair ou [S] para continuar")
print("###### FIM do programa ######\n")
print(f"A quantidade de pessoas com mais de 18 anos é {cont}")
print(f"Foram cadastrados {m} homems")
print(f"A quantidade de mulheres com menos de 20 anos é  {f}")
sleep(10)
