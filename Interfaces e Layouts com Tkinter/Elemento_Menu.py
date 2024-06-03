from tkinter import *

janela = Tk()
janela.title("Layout Tkinter")
janela.geometry("360x440")
janela.minsize(360,440)

menuBar= Menu(janela)
arquivo = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Arquivo", menu = arquivo)

arquivo.add_command(label="Novo Arquivo", command=None)
arquivo.add_command(label="Abrir arquivo", command=None)
arquivo.add_command(label="Salvar",command=None)
arquivo.add_separator()
arquivo.add_command(label="Sair", command=janela.destroy)

janela.config(menu=menuBar)
janela.mainloop()