from random import choice

a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segund aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")

lista = [a, b, c, d]

print("O aluno escolhido foi {}".format(choice(lista)))
