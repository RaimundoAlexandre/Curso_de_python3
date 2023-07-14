from rich import print


def area(a, b):
    c = (a * b)
    print(f"A área de um terreno com {a}[red]x[/]{b} é de {c:.2f}m²")


print("Controle de terrenos")
print("[green]--[/]" * 20)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)
print("[green]--[/]" * 20)
