from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.geometry("700x350")

janelaLogin = Frame(janelaPrincipal)
janelaHome = Frame(janelaPrincipal)

def troca_home():
    janelaHome.pack(fill='both', expand=True)
    janelaLogin.pack_forget()

Entry(janelaLogin, text="Usuario: ").pack(pady=20)
Entry(janelaLogin, text="Senha: ").pack(pady=20)
Button(janelaLogin, text="Logar", command=troca_home).pack()

Label(janelaHome, text="To dentro da Homepage").pack(pady=20)

janelaLogin.pack(expand = True, fill='both')

janelaPrincipal.mainloop()