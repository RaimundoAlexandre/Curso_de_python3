from random import randint
num = randint(1, 10)
palpites = 1
print("Tente adivinhar qual número o computador sorteou\nDigite apenas número inteiros de 1 a 10")
print("###"*10)
while True:
  player = int(input("Digite um número: "))
  if player == num:
    print("Parabenz você acertou!!!")
    break
  elif player != num:
    print("Você errou tente de novo")
    print("###"*10)
    palpites += 1
print(f"Foram necessarios {palpites} palpites para conseguir")
