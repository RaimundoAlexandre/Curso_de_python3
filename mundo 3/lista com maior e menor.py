valores = []

for c in range(0,5):
  valores.append(int(input("Digite os valores: ")))
print("=-="*10)

for c, v in enumerate(valores):
  print(f"na posição {c} encontrei {v}")

print("=-="*10)
maior = max(valores)
print(f"O maior valor encontrado foi {maior} na posição",end=' ')
for c , p in enumerate(valores):
  if p == maior:
    print(c,end='... ')
print("")

menor = min(valores)
print(f"O menor valor encontrado foi {menor} na posição",end=' ')
for c , p in enumerate(valores):
  if p == menor:
    print(c,end='... ')
print("")
print("=-="*10)

print("FIM")
