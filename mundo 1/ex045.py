from random import randint

print("-=-" * 10)
print("Vamos jogar Jokenpô?")
print('Escolha "0" para pedra, "1" para papel, "2" para tesoura')

jogador = int(input("Qual sua escolha? "))  # Jogador faz sua escolha

pc = randint(0, 2)  # O computador escolhe aleatoriamente entre 0, 1 ou 2

print("-=-" * 10)

# Verifica as possibilidades de jogadas e imprime o resultado correspondente

# Empate
if pc == jogador:
    print("Empate")
    
# Jogador escolhe Papel e computador escolhe Pedra
elif pc == 0 and jogador == 1:
    print("Jogador escolheu Papel, computador escolheu Pedra")
    print("Jogador venceu!")

# Jogador escolhe Tesoura e computador escolhe Pedra
elif pc == 0 and jogador == 2:
    print("Jogador escolheu Tesoura, computador escolheu Pedra")
    print("Computador venceu!")

# Jogador escolhe Pedra e computador escolhe Papel
elif pc == 1 and jogador == 0:
    print("Jogador escolheu Pedra, computador escolheu Papel")
    print("Computador venceu!")

# Jogador escolhe Tesoura e computador escolhe Papel
elif pc == 1 and jogador == 2:
    print("Jogador escolheu Tesoura, computador escolheu Papel")
    print("Jogador venceu!")

print("-=-" * 10)
