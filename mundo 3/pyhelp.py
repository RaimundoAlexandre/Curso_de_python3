# -- coding: utf-8 --
from time import sleep

c = (
    '\033[m',          # 0 sem cor
    '\033[0;30;41m',   # 1 vermelho
    '\033[0;30;42m',   # 2 verde
    '\033[0;30;43m',   # 3 amarelo
    '\033[0;30;44m',   # 4 azul
    '\033[0;30;45m',   # 5 roxo
    '\033[0;30;46m',   # 6 ciano
    '\033[7;30m'       # 7 branco (fundo)
)


def titulo(texto, cor=0):
    tamanho = len(texto) + 4
    print(c[cor], end='')
    print("~" * tamanho)
    print(f"  {texto}  ")
    print("~" * tamanho)
    print(c[0], end='')


def pyhelp(v):
    titulo(f"Acessando o manual do comando '{v}'", 4)
    print(c[0])
    print(c[7], end='')
    help(v)
    print(c[0], end='')
    sleep(2)


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    n = input("Função ou biblioteca: ").strip().lower()
    if n == 'fim':
        titulo('ATE LOGO', 1)
        break
    pyhelp(n)
