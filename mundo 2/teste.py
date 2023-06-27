"""soma = 0
cont = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c
            cont += 1
        
print(f"a soma entre os {cont} é {soma}")
"""
################################
"""
n = int(input("Digite um número para ver sua tabuada de multiplicação: "))
for c in range(1, 11):
    print("=-="*5)
    print(f"{n} * {c} = {n * c}")
print("=-="*5)
"""
###########################
"""
termo = int(input("Digite o valor do primeiro termo: "))
ra = int(input("Digite o valor da razão: "))
cont = 0
for c in range(termo, 500, ra):
    cont += 1
    print(c)
    if cont >= 10:
        break
"""
###############################
"""
print("Identificador de número primo")
n = int(input("Digite um número inteiro: "))

# Verifica se o número é maior que 1 e se é divisível por algum número além de 1 e ele próprio
if n > 1:
    for c in range(2, n):
        if n % c == 0:
            print(f"\033[31mO número {n} não é um número primo!\033[m]")
            break
        else:
            print(f"\033[33mO número {n} é um número primo!\033[m")
            break
else:
    print(f"\033[31mO número {n} não é um número primo!\033[m]")

"""
#############################
"""
frase = input("Digite uma frase para saber se é um palindromo: ").strip().split().upper()
frase = ''.join(frase)
frase_espelhada = frase[::-1]
if frase_espelhada == frase:
    print('é um palindromo')
else:
    print('não é um palindromo')
"""
"""
from datetime import datetime

ano_atual = datetime.now().year
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input("Digite o seu ano de nascimento: "))
    soma = ano_atual - ano
    if soma >= 21:
        maior += 1
    else:
        menor += 1
print(f"{maior} são maiores de idade e {menor} são menores de idade")
"""
"""
a = 0
b = 0

for c in range(0, 5):
    peso = float(input("Digite seu peso: "))
    if c == 0:
        a = peso
        b = peso
    else:
        if peso > a:
            a = peso
        elif peso < b:
            b = peso

print(f"O maior peso registrado foi {a}")
print(f"O menor peso registrado foi {b}")
"""
"""
soma = 0
h = 0
m = 0
for c in range(0, 4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [H] para masculino [M] para feminino: ").strip().upper()
    soma += idade
    if sexo == 'H':
        if idade > h:
            h = idade
            hn = nome
    else:
        if idade < 20:
                m  += 1
       

print(f"A media de idade é {soma/4}")
print(f"O homem mais velho é {hn}")
print(f"A quantidade de mulheres com menos de 20 anos é {m}")
"""
