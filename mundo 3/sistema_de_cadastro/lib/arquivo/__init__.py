from lib.arquivo import *
from lib.interface import *


def arquivo_exite(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False

    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Ouve um erro na criação do arquivo")
    else:
        print("Arquivo criado com sucesso")


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("ERRO! ao ler o arquivo")
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()


def cadastrar(arq, nome='sem nome', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro ao abrir o arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um erro ao abrir o arquivo")
        else:
            print(f"{nome} cadastrado com  sucesso!")
            a.close()
