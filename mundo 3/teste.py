from tkinter import *

janela = Tk()
janela.geometry("300x400+200+200")
janela.title("Calculadora")



saida = Label(janela, text='testeteste')
saida.place(x=100,y=150)

btSoma = Button(janela,width=10, text='+')
btSoma.place(x=100, y=100)




janela.mainloop()