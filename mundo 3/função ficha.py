def ficha(n='', g=0):
    """
    -> Verifica a ficha de um jogador e
    analisa se foi digitado um nome, mostra na tela o nome e
    a quantidade de gols do jogador.
    :param n: nome do jogador, vazio como padrão
    :param g: quantidade de gols do jogador, zero como padrão
    :return: sem retorno
    """
    if n == '':
        nick = "<desconhecido>"
    else:
        nick = n

    print(f"O jogador {nick} fez {g} gol(s) no campeonato.")


nome = ''
try:
    nome = str(input("Nome do jogador: ")).strip().capitalize()
    gols = int(input("Número de gols: "))
    ficha(nome, gols)
except ValueError:
    ficha(nome)
# ============== outra forma ===============================
# nome = str(input("Nome do jogador: ")).strip().capitalize()
# gols = int(input("Número de gols: "))
# if gols.isdigit():
#     gols = int(gols)
#     ficha(nome, gols)
# else:
#     ficha(nome)
