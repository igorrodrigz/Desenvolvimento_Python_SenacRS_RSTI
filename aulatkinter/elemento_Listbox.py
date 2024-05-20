from tkinter import *

def coleta():
    respAnimal = listboxAnimais.get(ACTIVE)
    print(respAnimal)

janela = Tk()

janela.title("Aprendendo Listbox")
janela.geometry("600x600")

#Criação dos widgets
listaOpcoes = ["Cachorro", "gato", "Pato"]
listboxAnimais = Listbox(janela)
for i in listaOpcoes:
    listboxAnimais.insert(END, i)

enviar = Button(janela, text="Enviar", command=coleta, font=('Verdana', 25))

#posicionamentos
listboxAnimais.pack()
enviar.pack()

janela.mainloop()