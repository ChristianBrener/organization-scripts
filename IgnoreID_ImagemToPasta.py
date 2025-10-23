import os
import shutil
import re

base_dir = os.path.dirname(os.path.abspath(__file__))

# Extensões aceitas
extensoes = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp')

# remove partes iniciais que sejam só números e separa por espaço, hífen ou underline e separa o primeiro nome
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.lower().endswith(extensoes):
            caminho_arquivo = os.path.join(root, file)
            nome_base = os.path.splitext(os.path.basename(file))[0] 
            partes = re.split(r'[\s_\-]+', nome_base)

            
            while partes and re.fullmatch(r'\d+', partes[0]):
                partes.pop(0)
              
            nome_pasta = partes[0] if partes else "sem_nome"
            pasta_destino = os.path.join(base_dir, nome_pasta)

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            destino_final = os.path.join(pasta_destino, file)
            if os.path.abspath(caminho_arquivo) != os.path.abspath(destino_final):
                shutil.move(caminho_arquivo, destino_final)
                print(f"Movido: {file} → {pasta_destino}")
