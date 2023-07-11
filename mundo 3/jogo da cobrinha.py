import tkinter as tk
import random

# Configurações da janela
largura, altura = 800, 600
tamanho_celula = 20

# Configurações da cobra
posicao_cabeca = [2, 4]
cobra = [[2, 4], [2, 3], [2, 2]]
ultima_posicao = 'r'

# Configurações da maçã
maca = [5, 5]

def desenhar_cobra():
    for segmento in cobra:
        x, y = segmento[0] * tamanho_celula, segmento[1] * tamanho_celula
        canvas.create_rectangle(x, y, x + tamanho_celula, y + tamanho_celula, fill='green')

def desenhar_maca():
    x, y = maca[0] * tamanho_celula, maca[1] * tamanho_celula
    canvas.create_oval(x, y, x + tamanho_celula, y + tamanho_celula, fill='red')

def movimentar_cobra():
    global ultima_posicao

    if ultima_posicao == 'r':
        posicao_cabeca[0] += 1
    elif ultima_posicao == 'l':
        posicao_cabeca[0] -= 1
    elif ultima_posicao == 'u':
        posicao_cabeca[1] -= 1
    elif ultima_posicao == 'd':
        posicao_cabeca[1] += 1

    # Atualiza a posição da cobra
    cobra.insert(0, list(posicao_cabeca))
    cobra.pop()

    # Verifica se a cobra atingiu a borda
    if posicao_cabeca[0] == 0 or posicao_cabeca[0] >= largura // tamanho_celula or posicao_cabeca[1] == 0 or posicao_cabeca[1] >= altura // tamanho_celula:
        return False

    # Verifica se a cobra comeu a maçã
    if posicao_cabeca == maca:
        cobra.append(list(cobra[-1]))
        maca[0] = random.randint(1, largura // tamanho_celula - 1)
        maca[1] = random.randint(1, altura // tamanho_celula - 1)

    return True

def atualizar():
    canvas.delete("all")
    if movimentar_cobra():
        desenhar_cobra()
        desenhar_maca()
    else:
        canvas.create_text(largura // 2, altura // 2, text="Game Over", fill="white", font=("Arial", 24))
        return

    janela.after(200, atualizar)  # 200ms de intervalo entre os frames

def definir_direcao(event):
    global ultima_posicao

    if event.keysym == 'Right' and ultima_posicao != 'l':
        ultima_posicao = 'r'
    elif event.keysym == 'Left' and ultima_posicao != 'r':
        ultima_posicao = 'l'
    elif event.keysym == 'Up' and ultima_posicao != 'd':
        ultima_posicao = 'u'
    elif event.keysym == 'Down' and ultima_posicao != 'u':
        ultima_posicao = 'd'

janela = tk.Tk()
janela.title("Jogo da Cobrinha")

canvas = tk.Canvas(janela, width=largura, height=altura, bg='black')
canvas.pack()

janela.bind("<KeyPress>", definir_direcao)
canvas.focus_set()

atualizar()

janela.mainloop()
