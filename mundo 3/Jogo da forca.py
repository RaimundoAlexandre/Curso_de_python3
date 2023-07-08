from random import randint
from time import sleep

print("###" * 20)
print(f"{'JOGO DA FORCA':^60}")
print("###" * 20)
print("\n")
print("=-=" * 20)

nomes = ['Cachorro', 'Programar', 'Estudar', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Video game']

# Loop principal do jogo
while len(nomes) > 0:
    print(f"Vou sortear uma dessas palavras {nomes}\nTente adivinhar qual palavra foi sorteada")
    print("=-="*20)
    indice = randint(0, len(nomes) - 1)
    p = nomes[indice]
    nomes.pop(indice)

    quantP = len(p)
    cont = 15
    print(f"Você tem {cont} chances")

    print(f"Dica: é uma palavra de {len(p)} letras")
    print("---" * 20)

    while True:
        if cont == 0:
            print("Você não tem mais tentativas. Você Perdeu.")
            break
        jogador = str(input("Tente adivinhar: ")).strip().lower()
        cont -= 1
        print("---" * 20)
        if jogador in p.lower():
            quantP -= 1
            print("Você acertou!")
            print("Qual a próxima letra?")
            print("---" * 20)
            if quantP == 0:
                print("Você venceu!! Parabéns!")
                break
        else:
            print(f"Você errou. Restam {cont} chances. Tente novamente.")
            print("---" * 20)

    print(f"A palavra sorteada foi: {p.capitalize()}")

    # Pergunta ao jogador se deseja jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (S/N): ").strip().upper()
    if jogar_novamente != 'S':
        break

print("Obrigado por jogar! Até a próxima.")
