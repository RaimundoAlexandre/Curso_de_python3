numeros = list(str(input("Digite uma expressão: ")))
if numeros.count('(') == numeros.count(')'):
  print("Sua pexpresão é válida")
else:
  print("Sua expresão esta errada")
