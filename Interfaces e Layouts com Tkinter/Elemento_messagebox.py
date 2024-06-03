from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Layout Tkinter")
janela.geometry("360x440")
janela.minsize(360,440)

def ShowInfo():
    messagebox.showinfo("Título da janela ( Showinfo)", "Conteúdo dentro da mensagem de showinfo")
def ShowWarning():
    messagebox.showwarning("Título da janela ( Showwarning)", "Conteúdo dentro da mensagem de showwarning")
def ShowError():
    messagebox.showerror("Título da janela ( Showerror)", "Conteúdo dentro da mensagem de showerror")
def MessageBox():
    teste = messagebox.askyesno("Título da janela ( MessageBox)", "Conteúdo dentro da mensagem de messagebox com yes ou no")
    print(teste)

menuBar= Menu(janela)
arquivo = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Arquivo", menu = arquivo)

arquivo.add_command(label="Showinfo", command=ShowInfo)
arquivo.add_command(label="Showwarning", command=ShowWarning)
arquivo.add_command(label="Showerror",command=ShowError)
arquivo.add_command(label="Showinfoask",command=MessageBox)
arquivo.add_separator()
arquivo.add_command(label="Sair", command=janela.destroy)

janela.config(menu=menuBar)


janela.mainloop()