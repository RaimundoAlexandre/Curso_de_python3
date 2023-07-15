from rich import print


def leiaInt(msg):
    while True:
        print("[blue]==[/]"*20)
        try:
            n = int(input(msg))
            return n
            break
        except ValueError:
            print("[red]ERRO! Digite um número inteiro válido[/]")


n = leiaInt('Digite um número: ')
print(f"[green]Você acabou de digitar[/] {n}")
