from tkinter import *

janela = Tk()



coletaValue = StringVar()

values = {"RadioButton 1": "1",
          "RadioButton 2": "2",
          "RadioButton 3": "3",
          "RadioButton 4": "4",
          "RadioButton 5": "5"}

for (tDicionario, vDicionario) in values.items():
    Radiobutton(janela, text=tDicionario, variable=coletaValue, value=vDicionario).pack()

enviar = Button(janela, text="Enviar", command=coletaValue, font=('Verdana', 25))

enviar.pack()

janela.mainloop()