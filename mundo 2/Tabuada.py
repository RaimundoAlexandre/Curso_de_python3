print("###"*10)
print("  Tabuada de multiplicação")
print("###"*10)
while True:
  n = int(input("Digite um número para ver sua tabuada: "))
  print("=-="*10)
  if n == 0:
    break
  for c in range(1, 11):
    print(f"{n} x {c:<2} = {n*c}")
  print("=-="*10)
print("FIM")
