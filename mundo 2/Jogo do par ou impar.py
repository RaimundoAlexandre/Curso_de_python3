from time import sleep
from random import randint
print("###"*10)
print("    JOGO do PAR OU IMPAR")
print("###"*10)
c = randint(1, 10)
soma = 0
while True:
  n = int(input("Digite um número: "))
  soma = c + n
  escolha = str(input("Par ou impar [P/I]: ")).strip().upper()
  if escolha in 'PI':
    if escolha == 'P':  
      if soma % 2 == 0:
        print(f"O PC jogou {c} e você {n}. deu PAR")
        print("Voce Ganhou. vamos jogar novamente")
      else:
        print(f"O PC jogou {c} e você {n}. deu IMPAR")
        print("Voce perdeu.")
        break
    elif escolha == 'I':
      if soma % 2 == 1:
        print(f"O PC jogou {c} e você {n}. deu IMPAR")
        print("Voce Ganhou. vamos jogar novamente")
      else:
        print(f"O PC jogou {c} e você {n}. deu PAR")
        print("Voce perdeu.")
        break
  else:
    print("Valor invalido tente novamente")
print("FIM")
sleep(5)
