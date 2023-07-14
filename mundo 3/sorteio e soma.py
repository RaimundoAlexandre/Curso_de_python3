from random import randint
from time import sleep
from rich import print


def sorteia():
    lst = []
    print("Sorteando 5 valores da lista: ", end='', flush=True)
    sleep(0.3)
    for c in range(0, 5):
        n = randint(1, 10)
        print(f"[blue]{n}[/]", end=' ')
        sleep(0.5)
        lst.append(n)
    print("PRONTO!")
    return lst


def soma_par(lst):
    print(f"Somando os valores pares de {lst}, temos", end=' ', flush=True)
    sleep(0.3)
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(soma)


lista = sorteia()
soma_par(lista)
