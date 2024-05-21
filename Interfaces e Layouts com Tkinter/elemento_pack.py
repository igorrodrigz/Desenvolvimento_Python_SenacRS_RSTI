from tkinter import *

janela = Tk()
janela.title("Layouts - Pack, Trabalhando com seções")
janela.geometry("600x400")
#elementos/widgets
texto1 = Label(janela, text="texto1", background='red')
texto2 = Label(janela, text="texto2", background='blue')

#posicionando
texto1.pack() """texto.pack(side='left')"""
texto2.pack() """texto2.pack(side='bottom')"""

#expansão
#posicionando
#texto1.pack(side='left', expand=True,fill='both')
#texto2.pack(side='bottom')

janela.mainloop()