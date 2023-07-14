from rich import print


def escreva(texto):
    tamanho = len(texto) + 4
    print("[red]~[/]" * tamanho)
    print(f"  [blue]{texto}[/]")
    print("[red]~[/]" * tamanho)


escreva('Raimundo Alexandre')
