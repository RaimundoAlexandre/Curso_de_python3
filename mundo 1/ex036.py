from time import sleep
print("-=-"*10)
print("Responda as Perguntas para prosseguir com seu empréstimo")
print("-=-"*10)
ep = float(input("Qual o valor da casa? R$"))
sa = float(input("Qual o seu salário? R$"))
anos = int(input("Em quantos anos deseja pagar? "))

print("Calculando.....")
sleep(2)
print("-=-"*10)
pres = ep / (anos * 12)
if pres > (sa * (30/100)):
    print("Empréstimo Negado!!")
    print("-=-" * 10)
else:
    print(f"Com um empréstimo de R${ep:.2f} você vai pagar R${pres:.2f} ")
    print("-=-"*10)
