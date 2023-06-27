num = float(input("Qual a distancia da sua viagem em Km? "))

if num <= 200:
    print("Sua passagem vai custar R${:.2f}".format(num * 0.50))
else:
    print("Sua viagem vai custar R${:.2f}".format(num * 0.45))
