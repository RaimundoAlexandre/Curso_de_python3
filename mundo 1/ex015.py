dias = float(input("Quantos dias de aluguel? "))
km = float(input("Quantos Km rodados? "))
print("Você ficou {} dias com o carro e rodou {}Km total a pagar R${:.2f}".format(dias, km, dias*60+km*0.15))
