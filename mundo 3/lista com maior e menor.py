valores = []

for c in range(0,5):
  valores.append(int(input("Digite os valores: ")))

for c, v in enumerate(valores):
  print(f"na posição {c} encontrei {v}")
print(f"O maior valor encontrado foi {max(valores)}")
print(f"O menor valor encontrado foi {min(valores)}")
print("FIM")
