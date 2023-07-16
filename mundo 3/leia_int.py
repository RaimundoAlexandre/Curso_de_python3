from rich import print


def leiaInt(msg):
    while True:
        print("[blue]==[/]"*20)
        try:
            a = int(input(msg))
            return a
            break
        except ValueError:
            print("[red]ERRO! Digite um número inteiro válido[/]")


n = leiaInt('Digite um número: ')
print(f"[green]Você acabou de digitar[/] {n}")
