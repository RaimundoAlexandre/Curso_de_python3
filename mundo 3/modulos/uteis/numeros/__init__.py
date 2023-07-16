from math import factorial
from rich import print


def fatorial(f, show=False):
    """
    Calcula o fatorial de um número.

    :param f: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta. O padrão é False.
    :return: O fatorial do número f.
    """
    if show:
        for c in range(f, 0, -1):
            if c > 1:
                print(f"{c}", end='')
                print('[green] x ', end='')
            else:
                print(f"{c}", end='')
                print('[green] = ', end='')
        fa = factorial(f)
        return fa
    else:
        fa = factorial(f)
        return fa
