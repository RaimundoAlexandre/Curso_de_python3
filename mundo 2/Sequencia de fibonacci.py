n = int(input('Digite um número: '))
a, b = 0, 1
while a < n:
  print(a, end=' ↦ ')
  a, b = b, a+b
print(n)
