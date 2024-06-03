from tkinter import *

janela = Tk()
janela.title("Layout tkinter - Calculadora")
janela.geometry("360x440")
janela.minsize(360,440)
janela.maxsize(360,440)

coletaCalculo = StringVar()

recente3 = Label(janela, text="720/2 = 360")
recente2 = Label(janela, text="720/2 = 360")
recente1 = Label(janela, text="720/2 = 360")
calculo = Entry(janela, textvariable=coletaCalculo)

#Configurando as linhas e colunas do Frame teclas
teclas = Frame(janela)
teclas.rowconfigure(0, weight=1)
teclas.rowconfigure(1, weight=1)
teclas.rowconfigure(2, weight=1)
teclas.rowconfigure(3, weight=1)
teclas.rowconfigure(4, weight=1)
teclas.columnconfigure(0, weight=1)
teclas.columnconfigure(1, weight=1)
teclas.columnconfigure(2, weight=1)
teclas.columnconfigure(3, weight=1)
teclas.columnconfigure(4, weight=1)

#posicionamento dos widgets
recente3.place(x=0,y=0, relwidth=1.0,relheight=0.1)
recente2.place(x=0,rely=0.1, relwidth=1.0, relheight=0.1)
recente1.place(x=0,rely=0.2, relwidth=1.0, relheight=0.1)
calculo.place(x=0,rely=0.3, relwidth=1.0, relheight=0.123)
teclas.place(x=0,rely=0.425, relwidth=1.0, relheight=0.5)

#posicionamento dos botoes do Frame
Button(teclas, text="<-", command="",background="red").grid(row=0,column=0, sticky='nsew')
Button(teclas, text="(", command="",background="red").grid(row=0,column=1, sticky='nsew')
Button(teclas, text=")", command="",background="red").grid(row=0,column=2, sticky='nsew')
Button(teclas, text="mod", command="",background="red").grid(row=0,column=3, sticky='nsew')
Button(teclas, text="n", command="",background="red").grid(row=0,column=4, sticky='nsew')

Button(teclas, text="7", command="",background="red").grid(row=1,column=0, sticky='nsew')
Button(teclas, text="8", command="",background="red").grid(row=1,column=1, sticky='nsew')
Button(teclas, text="9", command="",background="red").grid(row=1,column=2, sticky='nsew')
Button(teclas, text="+", command="",background="red").grid(row=1,column=3, sticky='nsew')
Button(teclas, text="√", command="",background="red").grid(row=1,column=4, sticky='nsew')

Button(teclas, text="4", command="",background="red").grid(row=2,column=0, sticky='nsew')
Button(teclas, text="5", command="",background="red").grid(row=2,column=1, sticky='nsew')
Button(teclas, text="6", command="",background="red").grid(row=2,column=2, sticky='nsew')
Button(teclas, text="x", command="",background="red").grid(row=2,column=3, sticky='nsew')
Button(teclas, text="x²", command="",background="red").grid(row=2,column=4, sticky='nsew')

Button(teclas, text="1", command="",background="red").grid(row=3,column=0, sticky='nsew')
Button(teclas, text="2", command="",background="red").grid(row=3,column=1, sticky='nsew')
Button(teclas, text="3", command="",background="red").grid(row=3,column=2, sticky='nsew')
Button(teclas, text="-", command="",background="red").grid(row=3,column=3, sticky='nsew')
Button(teclas, text="=", command="",background="red").grid(row=3,column=4, sticky='nsew')

Button(teclas, text="0", command="",background="red").grid(row=4,column=0, sticky='nsew')
Button(teclas, text=",", command="",background="red").grid(row=4,column=0, sticky='nsew')
Button(teclas, text="0", command="",background="red").grid(row=4,column=0, sticky='nsew')
Button(teclas, text="0", command="",background="red").grid(row=4,column=0, sticky='nsew')





janela.mainloop()