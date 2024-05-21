from tkinter import *

janela = Tk()

def coleta():
    senhaResp = entradaTexto.get()
    if senhaResp != "batatinhafrita123":
        #senha errada
        retornoSenha["text"] = "Senha incorreta"
        retornoSenha["background"] = "red"
    else:
        #senha correta
        retornoSenha["text"] = "Senha correta"
        retornoSenha["background"] = "green"

janela.title("Aprendendo aulatkinter")
janela.geometry("600x600")
#criar widgtes
textoSenha = Label(janela, text="senha: ", font=('Verdana', 25))
entradaTexto = Entry(janela, show="*", width= 15, font=('Verdana', 25))
enviar = Button(janela, text="Enviar", command=coleta, font=('Verdana, 25'), background='red')
retornoSenha = Label(janela, text="", font=('Verdana', 25))
#posicionamento
textoSenha.pack()
entradaTexto.pack()
enviar.pack()
retornoSenha.pack()

janela.mainloop()