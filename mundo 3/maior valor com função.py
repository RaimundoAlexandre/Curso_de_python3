from time import sleep
from rich import print


def maior(*num):
    print("[blue]=-=[/]" * 10)
    print("Analisando os valores passados...")
    for c in num:
        print(f"[green]{c}[/]", end=' ')
        sleep(0.3)
    print()
    print(f"Foram informados {len(num)} valores ao todo")
    v = max(num)
    print(f"O maior valor informado foi {v}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
