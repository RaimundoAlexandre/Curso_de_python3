print("\033[0;34mDigite 3 números para saber se é possível formar um triângulo\033[m")
r1, r2, r3 = map(float, input("Digite os três números separados por espaço: ").split())

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("É possível formar um triângulo!", end=' ')
    if r1 == r2 == r3:
        print("Equilátero")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print("Não é possível formar um triângulo")

