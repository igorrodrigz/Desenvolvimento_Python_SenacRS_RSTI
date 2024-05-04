from pillow import Image

# nome do arquivo  (foto.png) e  (local da imagem)
img = Image.open(r"foto.png") #depositando imagem em variável

img.show() #abrir foto no computador

==================================================
# Coletando informações da imagem
img = Image.open(r"foto.png")

print(img.mode) #formado de cores
print(img.size) #tamanho de imagem
print(img.format) #formato da imagem

==================================================
# Rotacionando a imagem
img = Image.open(r"img.png")

angle = 40 #criando angulo
r_img = img.rotate(angle) #usando função rotate(angulo)

r_img.show() 

==================================================
# Invertendo a imagem
img = Image.open(r"foto.png")

flip_img = img.transpose(Image.FLIP_TOP_BOTTOM) #flip vertical(cima-baixo)
flip_img = img.transpose(Image.FLIP_LEFT_RIGHT) #flip horizontal(esquerda-direita)

flip_img.show()

==================================================
# Escalando a imagem
img = Image.open(r"foto.png")

size = (40, 40) #declarando tamanho
r_img = img.resize(size) #redimensionando foto em tamanho previamente declarado

r_img.show()

==================================================
# Salvando a imagem
img = Image.open(r"foto.png")

size = (40, 40)
r_img = img.resize(size)
r_img.save("fotoReduzida.png") #salvando foto (nome do arquivo e formato)
img2 = Image.open(r"fotoReduzida.png") #armazenando imagem redimensionada para teste

img2.show()

==================================================
# Alterando qualidade das imagens
imagem_path = "foto.png"
image_file = Image.open(image_path)

image_file.save("foto.png", quality=95) #salvando na qualidade original, qualidade 95% (considerada original entre 95 e 100)
image_file.save("foto2.png", quality=25) #alterando a qualidade da imagem, qualidade 25%
image_file.save("foto3.png", quality=1) #alterando a qualidade da imagem, qualidade 1%

==================================================
# Encontrando diferenças em imagens
#a resolução e tamanho precisam ser iguais para funcionar 
img1 = Image.open('imagem1.png')
img2 = Image.open('imagem2.png')

diff = ImageChops.difference(img1, img2) #armazenando em variável, as duas imagens comparadas na função "difference"

diff.show() #mostrando o resultado na tela

==================================================
# Mesclar imagens
img1 = Image.open(r"imagem1.png")
img2 = Image.open(r"imagem2.png")

Image.Image.paste(img1, img2, (0, 0)) #insere a imagem2 na imagem1 (ordenando em seguida a posição da imagem1 onde a imagem2 será inserida(posição 0,0 (canto superior esquerdo)

img1.show()

==================================================
# Melhorando o Sharpness
imagem = Image.open(r"foto.png")

imagem.show() #abrindo imagem para comparação visual
atual_acuidade = ImageEnhance.Sharpness(image) #diferenciando os pontos proximos da imagem
nova_acuidade = 10 #declarando a nova visibilidade
img_sharpnada = atual_acuidade.Enhance(nova_acuidade) #inserindo a nova visibilidade na imagem melhorando a visualização dos pontos próximos da imagem

img_sharpnada.show()

==================================================
# Adicionando blur a imagens
img = Image.open(r"foto.png")

img1 = img.filter(ImageFilter.BoxBlur(4)) #adicionando filtro de blur na imagem

img1.show()

================================================= 
# Adicioando blur (efeito miopia)
img = Image.open(r"foto.png")

img1 = img.filter(ImageFilter.BLUR)

img1.show()

=================================================
# Inserindo textos em imagens
img = Image.open(r"foto.png")

figura1 = ImageDraw.Draw(img) #cria uma figura 2D 
figura1.text((28,36),"Texto a ser inserido!", fill=(255, 0, 0)) #insere na figura (na posição (x,y), o texto, na cor (255,0,0) vermelha)

img.show()

==================================================
# Inserindo textos em imagens (estilizar texto)
img = Image.open(r"foto.png")

figura1 = ImageDraw.Draw(img)
Fonte = ImageFont.truetype('FreeMono.ttf', 65) #declarando  ('o nome da fonte' e tamanho) e armazenando em variável Fonte
figura1.text((10,10), "Belo Mustang!", font=Fonte, fill=(255,0,0)) #inserindo na figura (posicionada 10, 10), o texto, com a fonte declarada, preenchido na cor (vermelha)

img.show()
