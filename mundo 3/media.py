aluno = []

while True:
  nome = str(input("Nome do aluno: ")).strip().capitalize()
  n1 = float(input("Primeiro nota: "))
  n2 = float(input("Segunda nota: "))
  aluno.append([nome,[n1,n2]])
  sair = str(input("Quer continuar?[S/N]")).strip().upper()
  if sair == 'N':
    break

print("=-=" * 10)
print(f"{'No.':<4}{'NOME':<10}{'MÉDIA':>6}")
print("---" * 10)
cont = 0
for c in aluno:
    print(f"{cont:<3} {aluno[cont][0]:<10} {(aluno[cont][1][0] + aluno[cont][1][1]) / 2:<10.2f}")
    cont += 1
print("=-=" * 10)

while True:
    notas = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
    if notas == 999:
        break
    else:
        print(f"Notas de {aluno[notas][0]} são {aluno[notas][1]}")

print("FIM")
