nome = str(input("Digite o seu nome: ")).strip()

print(nome.lower())
print(nome.upper())
nome2 = nome.split()
print("O seu nome ao todo tem", len(''.join(nome2)), "letras") # "- nome.count(' ')" assim é mais curto
print("O seu primeiro nome tem", len(nome.split()[0]), "letras") # nome.find(' ') outra forma de fazer
