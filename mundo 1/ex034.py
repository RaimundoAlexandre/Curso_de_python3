num = float(input("Qual o salário do funcionário? "))

if num > 1250:
    num += num*10/100
    print("O funcionário vai receber R${:.2f} com 10% de aumento".format(num))
elif num <= 1250:
    num += num * 15 / 100
    print("O funcionário vai receber R${:.2f} com 15% de aumento".format(num))
