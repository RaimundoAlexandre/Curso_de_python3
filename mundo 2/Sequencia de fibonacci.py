n = int(input('Digite um número: '))
a, b = 0, 1
while a < n:
  print(a, end=' ↦ ')
  a, b = b, a+b
print(n)
"""
n = int(input("Valor: "))
f = 0
n1 = 0
n2 = 1
cont = 1
while cont <=n:
  print(f,end=' ')
  n1 = n2
  n2 = f
  f = n1 + n2
  cont += 1
"""