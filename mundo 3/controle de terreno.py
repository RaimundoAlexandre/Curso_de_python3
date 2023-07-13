from time import sleep


def contagem():
    print("=-=" * 10)
    print("Contagem de 1 a 10 de 1 em 1")
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.2)
    print("FIM")


def regressiva():
    print("=-=" * 10)
    print("Contagem de 10 a 0 de 2 em 2")
    for c in range(10, 0, -2):
        print(c, end=' ')
        sleep(0.2)
    print("FIM")


def C_usuario(i, f, p):
    print("=-=" * 10)
    if p < 0:
        p *= p
    if p == 0:
        p += 1
    print(f"Contagem de {i} ate {f} de {p} em {p}")
    if i > f:
        p = (-p)
        f -= 1
    elif i < f:
        f += 1
    for c in range(i, f, p):
        print(c, end=' ')
        sleep(0.2)
    print("FIM")


contagem()
regressiva()
print("Agora é a sua vez de escolher a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
C_usuario(i, f, p)
