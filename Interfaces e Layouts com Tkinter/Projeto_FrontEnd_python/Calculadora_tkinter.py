from tkinter import *

janela = Tk()
janela.title("Layout Tkinter")
janela.geometry("360x440")
janela.minsize(360,440)
janela.maxsize(360,440)

def insereTexto(texto):
      temp = coletaCalculo.get()
      if texto == '<-':
            temp = temp[:-1]
            coletaCalculo.set(temp)
      else:
            temp = coletaCalculo.get() + texto
            coletaCalculo.set(temp)

coletaCalculo = StringVar()

recente3 = Label(janela, text="720/2 = 360")
recente2 = Label(janela, text="720/2 = 360")
recente1 = Label(janela, text="720/2 = 360")
calculo = Entry(janela, textvariable=coletaCalculo)

# * Configurando as linhas e colunas do Frame teclas
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

# * Posicionamento dos widgets
recente3.place(x=0,y=0, relwidth=1.0,relheight=0.1)
recente2.place(x=0,rely=0.1, relwidth=1.0,relheight=0.1)
recente1.place(x=0,rely=0.2, relwidth=1.0,relheight=0.1)
calculo.place(x=0,rely=0.3, relwidth=1.0,relheight=0.125)
teclas.place(x=0,rely=0.425, relwidth=1.0,relheight=0.5)

# * Posicionando os botões do Frame
# ? Primeira Linha teclas
Button(teclas, text="<-", background="red", fg="white",
command=lambda: insereTexto('<-')).grid(
      row=0,column=0, sticky="nsew")
Button(teclas, text="(", background="black", fg="white",
command=lambda: insereTexto('(')).grid(
      row=0,column=1, sticky="nsew")
Button(teclas, text=")", background="black", fg="white",
command=lambda: insereTexto(')')).grid(
      row=0,column=2, sticky="nsew")
Button(teclas, text="mod", background="black", fg="white",
command=lambda: insereTexto('mod')).grid(
      row=0,column=3, sticky="nsew")
Button(teclas, text="n", background="black", fg="white",
command=lambda: insereTexto('n')).grid(
      row=0,column=4, sticky="nsew")
# ? Segunda Linha teclas
Button(teclas, text="7", bg="black", fg="white",
command=lambda: insereTexto('7')).grid(
      row=1,column=0, sticky="nsew")
Button(teclas, text="8", bg="black", fg="white",
command=lambda: insereTexto('8')).grid(
      row=1,column=1, sticky="nsew")
Button(teclas, text="9", bg="black", fg="white",
command=lambda: insereTexto('9')).grid(
      row=1,column=2, sticky="nsew")
Button(teclas, text="/", bg="black", fg="white",
command=lambda: insereTexto('/')).grid(
      row=1,column=3, sticky="nsew")
Button(teclas, text="√", bg="black", fg="white",
command=lambda: insereTexto('√')).grid(
      row=1,column=4, sticky="nsew")
# ? Terceira Linha teclas
Button(teclas, text="4", bg="black", fg="white",
command=lambda: insereTexto('4')).grid(
      row=2,column=0, sticky="nsew")
Button(teclas, text="5", bg="black", fg="white",
command=lambda: insereTexto('5')).grid(
      row=2,column=1, sticky="nsew")
Button(teclas, text="6", bg="black", fg="white",
command=lambda: insereTexto('6')).grid(
      row=2,column=2, sticky="nsew")
Button(teclas, text="x", bg="black", fg="white",
command=lambda: insereTexto('x')).grid(
      row=2,column=3, sticky="nsew")
Button(teclas, text="x²", bg="black", fg="white",
command=lambda: insereTexto('x²')).grid(
      row=2,column=4, sticky="nsew")
# ? Quarta Linha teclas
Button(teclas, text="1", bg="black", fg="white",
command=lambda: insereTexto('1')).grid(
      row=3,column=0, sticky="nsew")
Button(teclas, text="2", bg="black", fg="white",
command=lambda: insereTexto('2')).grid(
      row=3,column=1, sticky="nsew")
Button(teclas, text="3", bg="black", fg="white",
command=lambda: insereTexto('3')).grid(
      row=3,column=2, sticky="nsew")
Button(teclas, text="-", bg="black", fg="white",
command=lambda: insereTexto('-')).grid(
      row=3,column=3, sticky="nsew")
Button(teclas, text="=", bg="green", fg="white",
command=lambda: insereTexto('=')).grid(
      row=3,column=4, sticky="nsew", rowspan=2)
# ? Quinta Linha teclas
Button(teclas, text="0", bg="black", fg="white",
command=lambda: insereTexto('0')).grid(row=4,column=0, sticky="nsew")
Button(teclas, text=",", bg="black", fg="white",
command=lambda: insereTexto(',')).grid(row=4,column=1, sticky="nsew")
Button(teclas, text="%", bg="black", fg="white",
command=lambda: insereTexto('%')).grid(row=4,column=2, sticky="nsew")
Button(teclas, text="+", bg="black", fg="white",
command=lambda: insereTexto('+')).grid(row=4,column=3, sticky="nsew")



janela.mainloop()
