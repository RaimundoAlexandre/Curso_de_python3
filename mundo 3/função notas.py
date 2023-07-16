from rich import print


def notas(*nts, situ=False):
    """
    Calcula estatísticas das notas fornecidas.

    :param nts: Uma sequência de notas.
    :param situ: (opcional) Se True, retorna a situação com base na média.
    :return: Um dicionário com as estatísticas das notas.

    - total: O número total de notas fornecidas.
    - maior: A maior nota.
    - menor: A menor nota.
    - media: A média das notas.
    - situacao (opcional): A situação com base na média (Boa, Razoavel, Ruim).
    """
    print("[blue]=-=[/]" * 10)
    nota = {'total': len(nts), 'maior': max(nts), 'menor': min(nts), 'media': sum(nts) / len(nts)}
    if situ:
        if nota['media'] >= 7:
            nota['situação'] = 'Boa'
        elif 7 > nota['media'] >= 5:
            nota['situação'] = 'Razoavel'
        else:
            nota['situação'] = 'Ruin'
    nota['media'] = float(f"{nota['media']:.2f}")
    return nota


resp = notas(3.5, 10, 6.5, situ=True)
print(resp)
