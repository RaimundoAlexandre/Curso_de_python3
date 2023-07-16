

def dobro(n, f=False):
    """
    Retorna o dobro do valor passado como parâmetro.

    :param n: Valor numérico.
    :param f: (Opcional) Se True, formata o valor como uma string de moeda.
    :return: Dobro do valor.
    """
    n *= 2
    if f:
        return moeda(n)
    else:
        return n


def metade(n, f=False):
    """
    Retorna a metade do valor passado como parâmetro.

    :param n: Valor numérico.
    :param f: (Opcional) Se True, formata o valor como uma string de moeda.
    :return: Metade do valor.
    """
    n /= 2
    if f:
        return moeda(n)
    else:
        return n


def aumentar(n1, n2, f=False):
    """
    Aumenta o valor passado como primeiro parâmetro em uma porcentagem específica.

    :param n1: Valor numérico.
    :param n2: Porcentagem de aumento.
    :param f: (Opcional) Se True, formata o valor como uma string de moeda.
    :return: Valor aumentado.
    """
    n1 += (n1 * (n2 / 100))
    if f:
        return moeda(n1)
    else:
        return n1


def diminuir(n1, n2, f=False):
    """
    Diminui o valor passado como primeiro parâmetro em uma porcentagem específica.

    :param n1: Valor numérico.
    :param n2: Porcentagem de diminuição.
    :param f: (Opcional) Se True, formata o valor como uma string de moeda.
    :return: Valor diminuído.
    """
    n1 -= (n1 * (n2 / 100))
    if f:
        return moeda(n1)
    else:
        return n1


def moeda(n):
    """
    Formata o valor numérico como uma string de moeda.

    :param n: Valor numérico.
    :return: Valor formatado como uma string de moeda.
    """
    r = f'R${n:.2f}'.replace('.', ',')
    return r


def resumo(v, n1, n2):
    print("--" * 16)
    print('        RESUMO DO VALOR')
    print("--" * 16)
    print(f"Analisando:         {moeda(v)}")
    print(f"Dobro do preço:     {dobro(v, True)}")
    print(f"Metade do preço:    {metade(v, True)}")
    print(f"{n1}% de aumento:     {aumentar(v, n1, True)}")
    print(f"{n2}% de redução:     {diminuir(v, n2, True)}")
    print("--" * 16)
