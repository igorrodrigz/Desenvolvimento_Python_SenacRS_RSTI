from tkinter import *

def coleta():
    parcelamento = coletaValue.get()
    print(parcelamento)

janela = Tk()

janela.title("Aprendendo Listbox")
janela.geometry("600x600")

#coletamento
coletaValue= StringVar()

#Criação dos widgets
opcao1 = Radiobutton(janela, text="x1 Parcelas", value="1", font=('Verdana', 25),variable=coletaValue)
opcao2 = Radiobutton(janela, text="x2 Parcelas", value="2", font=('Verdana', 25),variable=coletaValue)
enviar = Button(janela, text="Enviar", command=coleta, font=('Verdana', 25))

#posicionamentos
opcao1.pack()
opcao2.pack()
enviar.pack()

janela.mainloop()