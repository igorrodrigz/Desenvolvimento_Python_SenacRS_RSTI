#Leitura completa do arquivo
#read()
arquivo = open('teste.txt', 'r')
conteudo = arquivo.read()
print(conteudo)

#Leitura parcial do arquivo
#readline()
arquivo = open('teste.txt', 'r')
conteudo = arquivo.readline()

print(conteudo)

#Estrutura de "repetição" das linhas do arquivo
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)

#Vetores com Estruturas de repetição para leitura do arquivo
vetor = []
with open("teste.txt", "r") as arquivo:
    for i in arquivo:
        vetor.append(i)
print(vetor)




