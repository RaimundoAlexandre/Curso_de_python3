cor = (
    '\033[m',  # 0 sem cor
    '\033[0;30m',  # 1 vermelho
    '\033[0;30;42m',  # 2 verde
    '\033[0;30;43m',  # 3 amarelo
    '\033[0;30;44m',  # 4 azul
    '\033[0;30;45m',  # 5 roxo
    '\033[0;30;46m',  # 6 ciano
    '\033[7;30m'  # 7 branco (fundo)
)


def leiaDinheiro(a):
    while True:
        try:
            b = str(input(f'{a}')).strip().replace(',', '.')
            if b.isalpha() or b == '':
                print(f'{cor[1]}ERRO! "{b}" não é um valor valido{cor[0]}')
            else:
                return float(b)
        except ValueError:
            print(f'{cor[1]}ERRO! Digite um valor valido{cor[0]}')
