comando = 0
while comando != "":
    nomeArquivo = ("escrita.txt")
    comando = int(input("""Você deseja adicionar ou substituir:
    [1] O elemento deverá ser escrito 
    [2] O elemento deverá ser lido
    """))

    if comando == 1:
        print("modo de gravação: ")
        with open("Escrita de Arquivos/escrita.txt", "w") as arquivo:
            gravacao = input("Insira o nome do jogo .:")
            arquivo.write(input(f"{gravacao}\n"))

    else:
        with open("Escrita de Arquivos/escrita.txt", 'r') as arquivo:
            bloco = arquivo.read()
            print(bloco)