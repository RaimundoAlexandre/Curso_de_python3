nome = str(input("Digite seu nome: ")).strip()
print("Seu primeiro nome é {}".format(nome.split()[0]))
n = nome.split()
print("Seu ultimo nome é {}".format(n[len(n)-1]))
