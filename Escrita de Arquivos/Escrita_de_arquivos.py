# Escrevendo dados no arquivo no modo "A" adiciona conteúdo ao final do arquivo
nomeArquivo = "escrita.txt"
escrever = open(nomeArquivo, "a")

# Escrever dados no arquivo no modo W
escrever.write("Elemento a ser escrito 2")
escrever.close()

# Estrutura de

with open("escrita.txt", "w") as arquivo:
    arquivo.write("Elemento a ser escrito WWW")