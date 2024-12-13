from PIL import Image

# Carregar a imagem
def carregar_imagem(caminho):
    return Image.open(caminho).convert("RGB")  # Converter para RGB

# Converter para escala de cinza
def converter_para_cinza(imagem):
    return imagem.convert("L")  # "L" é o modo para escala de cinza

# Converter para binário
def converter_para_binario(imagem_cinza, limiar=128):
    return imagem_cinza.point(lambda p: 255 if p > limiar else 0, mode="1")  # Aplicar o limiar

# Função principal
def main():
    caminho_imagem = "brasil.jpg"  # Substitua pelo caminho da imagem
    imagem = carregar_imagem(caminho_imagem)
    
    # Converter para escala de cinza
    imagem_cinza = converter_para_cinza(imagem)
    imagem_cinza.show()  # Mostrar a imagem em cinza
    imagem_cinza.save("imagem_cinza.jpg")  # Salvar a imagem em cinza
    
    # Converter para binário
    imagem_binaria = converter_para_binario(imagem_cinza)
    imagem_binaria.show()  # Mostrar a imagem binária
    imagem_binaria.save("imagem_binaria.jpg")  # Salvar a imagem binária

# Executar o programa
if __name__ == "__main__":
    main()



