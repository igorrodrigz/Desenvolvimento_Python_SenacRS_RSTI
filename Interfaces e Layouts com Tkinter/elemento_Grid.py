from tkinter import *

janela = Tk()
janela.title('Layouts - Grids. Trabalhando com linhas e colunas')
janela.geometry('600x800')


#configurando colunas
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=1)
#configurando linhas
janela.rowconfigure(0,weight=1)
janela.rowconfigure(1, weight=1)
janela.rowconfigure(1,weight=1)

#botão
botãoPlay = Button(janela, text="play")

#posicionamento
texto1 = Label(janela, text='absurdo', background='green')
texto2 = Label(janela, text='absurdo', background='red')
texto3 = Label(janela, text='absurdo', background='blue')

texto1.grid(row=0, column=0, sticky='nsew', columnspan=1)
texto2.grid(row=0, column=1, sticky='nsew', columnspan=1)
texto3.grid(row=0, column=2, sticky='nsew', columnspan=1)

botãoPlay.grid(row=1,column=1, sticky='nsew', command='play')

janela.mainloop()