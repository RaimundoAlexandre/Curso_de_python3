from random import randint
# 3 formas de encontrar o mesmo resultado
"""
n1, n2 = 0, 0
cont = 0
numeros = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

while cont < 5:
    num = numeros[cont]
    if cont == 0:
        n1, n2 = num, num
    if n1 > num:
        n1 = num
    if n2 < num:
        n2 = num
    cont += 1

print(numeros)
print(f"O maior é {n2} e o menor é {n1}")
"""

"""
from random import randint

n1, n2 = 0, 0
numeros = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

cont = 0
while cont < 5:
    num = numeros[cont]

    # Verifica se o número atual é menor que n1 (menor número encontrado)
    if num < n1 or cont == 0:
        n1 = num
    
    # Verifica se o número atual é maior que n2 (maior número encontrado)
    if num > n2 or cont == 0:
        n2 = num
    
    cont += 1

print(numeros)
print(f"O maior número é {n2} e o menor número é {n1}")

"""



numeros = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

n1 = min(numeros)
n2 = max(numeros)

print(numeros)
print(f"O maior número é {n2} e o menor número é {n1}")
