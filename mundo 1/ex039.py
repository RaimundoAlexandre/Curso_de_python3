from datetime import date
idade = int(input("Digite o ano de seu nascimento: "))
atual = date.today().year
ano = (atual - idade)
print(f"Quem nasceu em {idade} tem {ano} anos")
if ano == 18:
    print("Esta na hora de se alistar ao cerviço militar")
elif ano < 18:
    print("Você inda vai se alistar!")
    tempo = 18 % ano
    print(f"Falta {tempo} anos para você se alistar")
elif ano > 18:
    tempo = ano % 18
    print("Japassou do tempo de se alistar")
    print(f"Já passou {tempo} ano(s) do prazo para alistamento")

