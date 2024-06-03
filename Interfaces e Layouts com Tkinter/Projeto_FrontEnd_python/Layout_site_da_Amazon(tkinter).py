from tkinter import *

janela = Tk()
janela.title('Layout tkinter - Site Amazon')
janela.geometry("1280x720")
janela.minsize(1280,720)

topBar = Frame(janela)
barraPesquisa = Frame(topBar)
topBar.columnconfigure(0,weight=1)
topBar.columnconfigure(1,weight=1)
topBar.columnconfigure(2,weight=7)
topBar.columnconfigure(3,weight=1)
topBar.columnconfigure(4,weight=1)
topBar.columnconfigure(5,weight=1)
topBar.rowconfigure(0,weight=1)
topBar.grid(row=0,column=0,sticky='nsew')

#Label(topBar, text="1", background='red').grid(row=0, column=0,sticky='snew')
#Label(topBar, text="2", background='green').grid(row=0, column=1,sticky='snew')
#Label(topBar, text="3", background='blue').grid(row=0, column=2,sticky='snew')
#Label(topBar, text="4", background='purple').grid(row=0,column=3,sticky='snew')
#Label(topBar, text="5", background='pink').grid(row=0,column=4,sticky='snew')
#Label(topBar, text="6", background='yellow').grid(row=0,column=5,sticky='snew')
Label(topBar, text="Amazon.com.br",font=("",15), fg='white',bg='black').grid(row=0,column=0,sticky='nsew')
Label(topBar, text="Enviar Uruguaiana-RS",font=("",15), fg='white',bg='black').grid(row=0,column=1,sticky='nsew')


#quebra para a barra de Pesquisa

barraPesquisa.grid(row=0,column=2,sticky='nsew')
Label(barraPesquisa,text="Todos", font=("",15),bg='Gray').pack(expand=True,fill='both',side='left')
Entry(barraPesquisa, font=("", 15), fg='gray').pack(expand=True, fill='both', side='left')
Button(barraPesquisa, text="Pesquisar",font=("",15), bg='orange').pack(expand=True,fill='both', side='left')

#Continuação topbar
Label(topBar, text="Olá Igor,\n Contas e Listas", font=("",15), fg='white',bg='black').grid(row=0,column=3,sticky='nsew')
Label(topBar, text="Devoluções", font=("",15), fg='white',bg='black').grid(row=0,column=4,sticky='nsew')
Label(topBar, text="Carrinho", font=("",15), fg='white',bg='black').grid(row=0,column=5,sticky='nsew')
janela.mainloop()