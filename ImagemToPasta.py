import os
import shutil
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

# Extensões de imagem aceitas
extensoes = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

#Separa as Imagens em pastas com base no primeiro nome
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(extensoes):
            caminho_arquivo = os.path.join(root, file)
            nome_base = os.path.basename(file)
            
            # separa antes de espaço, hífen ou underline
            nome_pasta = re.split(r'[\s_\-]+', nome_base)[0]
            pasta_destino = os.path.join(base_dir, nome_pasta)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            destino_final = os.path.join(pasta_destino, file)
            if os.path.abspath(caminho_arquivo) != os.path.abspath(destino_final):
                shutil.move(caminho_arquivo, destino_final)
                print(f"Movido: {file} → {pasta_destino}")
