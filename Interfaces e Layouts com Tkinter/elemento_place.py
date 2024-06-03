from tkinter import *

janela = Tk()
janela.title("layout - Place")
janela.geometry("600x600")

texto1 = Label(janela, text="Place teste", background='Spring green', font=50)

texto1.place(relx=0.5, rely=0.5, width=100, height=100, anchor='center')

janela.mainloop()