from time import sleep
from rich import print


def maior(*num):
    """
    -> Analisa os valores passados e
    mostra qual é o maior valor.
    :param num: recebe os valores e os empacota
    :return: sem retorno
    """
    print("[blue]=-=[/]" * 10)
    print("Analisando os valores passados...")
    sleep(2)
    try:
        for c in num:
            print(f"[green]{c}[/]", end=' ', flush=True)
            sleep(0.5)
        print()
        print(f"Foram informados {len(num)} valores ao todo")
        v = max(num)
        print(f"O maior valor informado foi {v}")
    except ValueError:
        print("Valor invalido")


# maior(2, 9, 4, 5, 7, 1)
# maior(4, 7, 0)
# maior(1, 2)
# maior(6)
# maior(0)
help(maior)
