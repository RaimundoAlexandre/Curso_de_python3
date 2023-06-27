preco = float(input("Qual o valor do produto? R$"))
print("O produto que valia R${:.2f} com com 5% de descont vale R$ {:.2f}".format(preco, preco - (preco * 5/100)))
