salario = float(input("Qual o salário atual? "))
re = salario+(salario*0.15)
print("O funcionario que recebia R${:.2f} com 15% de aumento vai receber R${:.2f}".format(salario, re))
