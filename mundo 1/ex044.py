print(f"\033[0;34m{' Aracati Usados ':=^40}\033[m")
valor = float(input("Digite o valor do produto em R$: "))

# Solicita a forma de pagamento ao usuário
condi = str(input("Escolha a forma de pagamento:\n"
                  "1 para pagamento à vista em dinheiro/cheque com 10% de desconto\n"
                  "2 para pagamento à vista no cartão com 5% de desconto\n"
                  "3 para pagar em até 2x no cartão sem desconto\n"
                  "4 para pagar em 3x ou mais no cartão com 20% de juros: ")).strip()

# Calcula os valores com desconto e juros
desconto10 = valor - (valor * 10/100)
desconto5 = valor - (valor * 5/100)
juros20 = valor + (valor * 20/100)

# Verifica a forma de pagamento escolhida
if condi == '1':
    # Exibe o valor a ser pago com 10% de desconto
    print(f"O preço do produto é R$ {valor:.2f} e com 10% de desconto você vai pagar R$ {desconto10:.2f}")
elif condi == '2':
    # Exibe o valor a ser pago com 5% de desconto
    print(f"O preço do produto é R$ {valor:.2f} e com 5% de desconto você vai pagar R$ {desconto5:.2f}")
elif condi == '3':
    # Exibe a mensagem de pagamento em até 2x no cartão sem desconto
    print(f"O preço do produto é R$ {valor:.2f} e você pode pagar em até 2x no cartão sem desconto")
elif condi == '4':
    # Exibe o valor a ser pago com 20% de juros
    print(f"O preço do produto é R$ {valor:.2f} e com 20% de juros você vai pagar R$ {juros20:.2f}")
else:
    # Exibe uma mensagem de opção inválida se a opção digitada for diferente de 1, 2, 3 ou 4
    print("Opção inválida. Por favor, escolha uma opção válida.")
