from tkinter import *

def coleta():
	senhaResp = entradaTexto.get()
	if senhaResp != "batatinhafrita123":
		#Senha errada
		retornoSenha["text"] = "Senha incorreta"
		retornoSenha["background"] = "red"
	else:
		#Senha certa
		retornoSenha["text"] = "Senha correta"
		retornoSenha["background"] = "green"

janela = Tk()

janela.title("Aprendendo Tkinter")
janela.geometry("600x600")

#Criação dos widgets
textoSenha = Label(janela, text="Senha: ", font=('Verdana',25))
entradaTexto = Entry(janela, show="*",width=15, font=('Verdana',25))
enviar = Button(janela, text="Enviar", command=coleta, font=('Verdana',25), background='red')
retornoSenha = Label(janela, text="", font=('Verdana',25))

#Posicionamentos
textoSenha.pack()
entradaTexto.pack()
enviar.pack()
retornoSenha.pack()

janela.mainloop()
