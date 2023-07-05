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
"""
valor = int(input("Digite um valor: "))
n1 = 0
n2 = 1
print(f'{n1} {n2}',end=' ')
for c in range(3, valor+1):
  f = n1 + n2
  print(f"{f}",end=' ')
  n1 = n2
  n2 = f
  
"""