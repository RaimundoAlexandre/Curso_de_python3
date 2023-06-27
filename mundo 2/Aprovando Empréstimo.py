from time import sleep

print("-=-" * 10)
print("Responda as perguntas para prosseguir com seu empréstimo")
print("-=-" * 10)

# Solicita informações ao usuário
ep = float(input("Qual o valor da casa? R$"))
sa = float(input("Qual o seu salário? R$"))
anos = int(input("Em quantos anos deseja pagar? "))

print("Calculando.....")
sleep(2)
print("-=-" * 10)

# Calcula a prestação mensal
pres = ep / (anos * 12)

# Verifica se a prestação excede 30% do salário
if pres > (sa * (30/100)):
    print("Empréstimo Negado!!")
    print("-=-" * 10)
else:
    print(f"Com um empréstimo de R${ep:.2f}, você vai pagar R${pres:.2f} por mês.")
    print("-=-" * 10)
