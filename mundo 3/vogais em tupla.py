print("###" * 20)
print(f"{'LISTAGEM DE VOGAIS':^60}")
print("###" * 20)
print("\n")
print("=-=" * 20)

nomes = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado')

for nome in nomes:
    vogais = ''
    for letra in nome:
        if letra.lower() in 'aeiou':
            vogais += letra.lower() + ' '
    if vogais:
        print(f"Na palavra {nome} temos: {vogais.rstrip()}")


print("=-=" * 20)
print("\n")
print("###" * 20)
