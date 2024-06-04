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

#variavel de fonte
est1 = ("Verdana", 20, 'bold')


(Label(esquerda_frame,text="Frame Esquerdo").pack(expand=True,fill='both')) #
(Label(direita_frame, background='lightblue',text="Escolha seu candidato").pack(expand=True,fill='both'))

#declarando botões
botao1 = Button(esquerda_frame, text='Anula', bd=10, bg='grey', font=est1)
botao2 = Button(esquerda_frame, text='Branco', bd=10, bg='white', font=est1)
botao3 = Button(esquerda_frame, text='Confirma', bd=10, bg='green', fg='white', font=est1 )

#definição dos botões / posicionamento
botao1.pack(expand=True, fill='both')
botao2.pack(expand=True, fill='both')
botao3.pack(expand=True, fill='both')

janela.mainloop()