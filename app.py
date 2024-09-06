from rembg import remove
from PIL import Image

while True:
    imagem = input('Informe o nome da imagem com a extensão: ')
    if imagem != '':
        nova_imagem = f'nova_{imagem}.png'
        entrada = Image.open(imagem)
        saida = remove(entrada)
        saida.save(nova_imagem)
        continue
    else:
        break