a = int(input("Digite um número: "))
b = int(input("Digite outr número: "))
c = int(input("Digite mais um número: "))
menor = a
# Verifica o menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verifica o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior número é {} e o menor foi {}".format(maior, menor))
