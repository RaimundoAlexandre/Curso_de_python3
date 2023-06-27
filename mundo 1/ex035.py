print("\033[0;34mDigite 3 números para saber se é possível formar um triangulho\033[m")
r1 = float(input("Digite o primeiro número: "))
r2 = float(input("Digite o segundo número: "))
r3 = float(input("Digite o terceiro número: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("è possível formar um triangulo!")
else:
    print("Não é possível formar um triangulo")
