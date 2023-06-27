from random import randint
from time import sleep

print("Vamos jogar Jokenpô!")

# Solicita a escolha do jogador
player = input("Escolha:\n"
               "[0] Para pedra\n"
               "[1] Para papel\n"
               "[2] Para tesoura\n").strip()

# Gera a escolha aleatória do computador
pc = randint(0, 2)

print("=-=" * 5)
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Po")
print("=-=" * 5)
sleep(1)

# Verifica as escolhas e determina o vencedor
if player == '0':
    print("Você escolheu pedra")
    if pc == 0:
        print("Computador escolheu pedra, empate")
    elif pc == 2:
        print("Computador escolheu tesoura, você venceu")
    elif pc == 1:
        print("Computador escolheu papel, você perdeu")
elif player == '1':
    print("Você escolheu papel")
    if pc == 0:
        print("Computador escolheu pedra, você venceu")
    elif pc == 2:
        print("Computador escolheu tesoura, você perdeu")
    elif pc == 1:
        print("Computador escolheu papel, empate")
elif player == '2':
    print("Você escolheu tesoura")
    if pc == 0:
        print("Computador escolheu pedra, você perdeu")
    elif pc == 2:
        print("Computador escolheu tesoura, empate")
    elif pc == 1:
        print("Computador escolheu papel, você venceu")
else:
    print("Opção inválida. Escolha uma opção válida (0, 1, 2).")
