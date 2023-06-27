"""nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
peso = input('Digite seu peso: ')
print('Ola {}, sua idade é {} e seu peso é {}'.format(nome, idade, peso))
"""
"""n = input('qual é o seu nome? ')
print("ola {} prazer em te conhecer".format(n))
"""

"""n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print("A soma entre {} e {} é {}".format(n1, n2, n1 + n2))
"""
"""n = 0
while True:
    cont = 1
    n = int(input('Digite um número: '))
    print('-='*10)
    if n == 0:
        break
    for i in range(1, 11):
        print(f'{n} x {cont:2} = {cont*n}')
        cont += 1

print('FIM')
"""
"""
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

if n1 > n2 and n1 > n3:
    print("O maior valor é {}".format(n1))
else:
    if n2 > n1 and n2 > n3:
        print("O maior valor é {}".format(n2))
    else:
        if n3 > n2 and n3 > n1:
            print("O maior valor é {}".format(n3))
        else:
            if n1 == n2 and n1 == n3:
                print("Todos os valores são iguais")
"""
"""nome = input("Qual seu nome? ")
print("Prazer em te conhecer {:=^20}".format(nome))
"""
"""
#import math
from math import sqrt

num = int(input("Digite um número para saber sua raiz: "))
#raiz = math.sqrt(num)

raiz = sqrt(num)
print("A raiz de {} é {:.3f}".format(num, raiz))
"""
"""
from random import randint
num = randint(1, 10)
print(num)
"""
"""
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
#Opicional use_aliases=True
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
#Opicional use_aliases=True
print(emoji.emojize('Python :snake:', use_aliases=True))
print(emoji.emojize('Python :snake:'))
"""
"""
frase = 'Curso em Vídeo Python'

len(frase) # analisa
frase.count('o') # conta
frase.count('o', 0, 13) # conta do caractere 0 ate o 12 igrando o 13
frase.find('Android') # se aparecer -1 significa que a frase buscada não existe dentro da variavel
'Curso'in frase # pergunta se a palava Curso existe dentro da variavel
frase.replace('Python', 'Android') # subistitui a palavra Python por Android
frase.upper() # torna a frase inteira maiuscula
frase.lower() # deixa a frase em minusculo
frase.capitalize() # deixa tudo em minusculo menos a primeira letra
frase.title() # analisa quantas palavras tem dentro da variavel frase
frase = '   Aprenda Python  '
frase.strip() # remove todos os espaços inuteis
frase.rstrip() # remove apenas os ultimos espaços
frase.lstrip() # remove apenas os espaços da direita
frase = 'Curso em Vídeo Python'
frase.split() # cria uma divisão entre os espaços
'-'.join(frase) # diferente do split o join junta a palavra que foi separada pelo split
"""
#frase = 'Curso em Vídeo Python'
"""print(frase[::2]) # escreve do inicio ao fim pulando de 2 em 2"""

#print(frase.upper().count('O')) # joga tudo pra maiusculo e depois conta quantos O maiusculo tem

"""from PySimpleGUI import PySimpleGUI as sg
# tela de login

sg.theme('Reddit')

layout = [
    [sg.Txt('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'alex' and valores['senha'] == '123456':
            print('Bem vindo')
"""