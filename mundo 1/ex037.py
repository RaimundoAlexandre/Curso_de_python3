n = int(input("Digite um número inteiro: "))
print("Digite em qual base deseja converter\n"
                 "[1] para Binário\n"
                 "[2] para Octal\n"
                 "[3] para Hexadecimal")
base = int(input("Digite sua escolha: "))
if base == 1:
    print(f"{n} Convertido em Bninario é {bin(n)[2:]}")
elif base == 2:
    print(f"{n} convertido para Octal é {oct(n)[2:]}")
elif base == 3:
    print(f"{n} convertido para Hexadecimal é {hex(n)[2:]}")
else:
    print("Valor invalido!!")
