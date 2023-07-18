def leia_int(msg):
    while True:
        try:
            n = int(input(f'{msg}'))
            return n
        except ValueError:
            print("\033[31mErro! Digite um valor inteiro válido\033[m")
        except KeyboardInterrupt:
            print("\nO usuário preferiu não digitar esse número")
            return 0


def linha(tam=42):
    return '-' * 42


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f"\033[33m{c}\033[m - \033[34m{i}\033[m")
        c += 1
    print(linha())
    opc = leia_int('\033[32mSua opção\033[m: ')
    return opc
