galera = list()
dado = list()

for c in range(0, 5):
  dado.append(str(input("Nome: ")))
  dado.append(int(input("Idade: ")))
  galera.append(dado[:])
  dado.clear()

maior = menor = 0
for p in galera:
  if p[1] >= 21:
    print(f"{p[0]} é maior de idade e tem {p[1]} anos")
    maior += 1
  else:
    print(f"{p[0]} é menor de idade e tem {p[1]} anos")
    menor += 1
print(f"Temos {maior} maiores de idade e {menor} menores de idade")