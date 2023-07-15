from math import factorial


def fatorial(f, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param f: o numero a ser calculado.
    :param show: (Opicional) Mostra ou não a conta.
    :return: o fatorial de um numero f.
    """
    if show == False:
        fa = factorial(f)
        return fa
    else:
        for c in range(f, -1, -1):
            if c > 1:
                print(f"{c}", end=' x ')
            else:
                print(f"{c}", end=' = ')
                break
        fa = factorial(f)
        return fa


n = int(input("Digite um valor para saber seu fatorial: "))

resul = fatorial(n, show=True)
print(resul)
