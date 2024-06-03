from tkinter import *

janela = Tk()
janela.title('Layout - trabalhando com frames')
janela.geometry('800x800')

#declarando frames
esquerda_frame = Frame(janela)
direita_frame = Frame(janela)
frameDisclaimer = Frame(esquerda_frame)

#posição dos frames
esquerda_frame.place(x=0, y=0, relwidth=0.3, relheight=1) #posicionamento inicial e relacional%
direita_frame.place(relx=0.3,y=0,relwidth=0.7,relheight=1) #posicionamento inicial e relacional%
Disclaimer = Label(frameDisclaimer, text ="desenvolvido por Igor")

#Espaços com cores dentro dos frames
(Label(esquerda_frame, background='red',text="Frame Esquerdo").pack(expand=True,fill='both')) # Espaço vazio Vermelho
(Label(direita_frame, background='lightblue',text="Frame Direito").pack(expand=True,fill='both'))

#declarando botões
botao1 = Button(esquerda_frame, text='Botão 1')
botao2 = Button(esquerda_frame, text='Botão 2')


#definição dos botões / posicionamento
botao1.pack(expand=True, fill='both')
botao2.pack(expand=True, fill='both')


frameDisclaimer.pack() #posicionamento do frame novo ao final do frame 1
Disclaimer.grid(row=0,column=0, sticky='nsew') #posicionamento do disclaimer dentro do frame novo

janela.mainloop()