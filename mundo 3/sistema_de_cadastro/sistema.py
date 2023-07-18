from time import sleep
from lib.arquivo import *
from lib.interface import *

arq = 'dados.txt'

if not arquivo_exite(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sitema'])
    if resposta == 1:
        ler_arquivo(arq)
        sleep(2)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input("Nome: ")).strip()
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print("\033[36mSaindo do sistema", end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.', end='')
        sleep(1)
        print('.\033[m', end='')
        sleep(1)
        break
    else:
        print("\033[31mERRO! opção invalida\033[m")
        sleep(2)
