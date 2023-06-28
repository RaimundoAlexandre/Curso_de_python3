print("###" * 20)
print(f"{'LISTAGEM DE PREÇOS':^60}")
print("###" * 20)

print("\n")
print("=-=" * 20)

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.00, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0,len(listagem),2):
    itens = listagem[c]
    preco = listagem[c+1]
    print(f"{itens}{'.......'*5}{'R$':>8} {preco:.2f}")

print("=-=" * 20)
print("\n")

print("###" * 20)
