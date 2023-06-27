carro = float(input("A quantos Km/h esta o seu carro? "))

if carro > 80:
    print("Seu carro esta acima do limite permitido")
    print("Você foi multado em R${:.2f}".format((carro - 80) * 7))
else:
    print("Você esta dentro do limite permitido")
