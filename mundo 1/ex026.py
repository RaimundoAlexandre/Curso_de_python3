nome = str(input("Digite uma frase: ")).strip().upper()
print("A letra 'A' aparece {} vezes".format(nome.count('A')))
print("A primeira letra 'A' apareceu na posição {}".format(nome.find('A')+1))
print("A ultima letra 'A' Apareceu na posição {}".format(nome.rfind('A')+1))
