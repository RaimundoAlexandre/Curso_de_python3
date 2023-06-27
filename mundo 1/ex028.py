from random import randint

num = randint(1, 3)
player = int(input("Tente Adivinhar que número de 1 a 3 o PC sorteou: "))
print("=-="*10)

if player == num:
    print('Parabenz você venceu !!')
else:
    print('que pena você perdeu ')
print("=-="*10)
