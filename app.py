from rembg import remove
from PIL import Image

while True:
    try:
        imagem = input('Informe o nome da imagem com a extensão ou Enter para encerrar: ')
        if imagem != '':
            nova_imagem = f'nova_{imagem}.png'
            entrada = Image.open(imagem)
            saida = remove(entrada)
            saida.save(nova_imagem)
            continue
        else:
            ...
    except Exception as e:
        print(f'Não foi possível remover o fundo da imagem. {e}.')
    finally:
        break