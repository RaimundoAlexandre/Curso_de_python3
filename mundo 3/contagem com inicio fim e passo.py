from time import sleep
from rich import print


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print("[green]=-=[/]" * 10)
    print(f"Contagem de {i} ate {f} de {p} em {p}")
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=' ', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ', flush=True)
            sleep(0.5)
            cont -= p
    print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("[green]=-=[/]" * 10)
print("Agora é a sua vez de escolher a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim:    "))
p = int(input("Passo:  "))
contador(i, f, p)
