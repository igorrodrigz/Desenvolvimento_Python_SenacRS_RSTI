from tkinter import *

janela = Tk()
janela.title('Layout - trabalhando com frames')
janela.geometry('800x800')

#declarando frames
esquerda_frame = Frame(janela)
direita_frame = Frame(janela)

#posição dos frames
esquerda_frame.place(x=0, y=0, relwidth=0.3, relheight=1) #posicionamento inicial e relacional%
direita_frame.place(relx=0.3,y=0,relwidth=0.7,relheight=1) #posicionamento inicial e relacional%


(Label(esquerda_frame, background='red',text="Frame Esquerdo").pack(expand=True,fill='both')) #
(Label(direita_frame, background='lightblue',text="Frame Direito").pack(expand=True,fill='both'))

#declarando botões
botao1 = Button(esquerda_frame, text='Botão 1')
botao2 = Button(esquerda_frame, text='Botão 2')
botao3 = Button(esquerda_frame, text='Botão 3')

#definição dos botões / posicionamento
botao1.pack(expand=True, fill='both')
botao2.pack(expand=True, fill='both')
botao3.pack(expand=True, fill='both')

janela.mainloop()