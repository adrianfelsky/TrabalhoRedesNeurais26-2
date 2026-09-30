import os
import shutil
import random
import kagglehub

print("Iniciando o download dos datasets pelo Kagglehub...")
path_ships = kagglehub.dataset_download("vinayakshanawad/ships-dataset")
path_airplanes = kagglehub.dataset_download("joopedrogrippa/airplanes")

# Caminho base dentro do seu repositório local
base_dir = "./dataset"

# 1. Cria a estrutura de pastas vazias
for split in ['treino', 'teste']:
    for cat in ['barco', 'aviao']:
        os.makedirs(os.path.join(base_dir, split, cat), exist_ok=True)

# 2. Função para vasculhar os downloads e separar as imagens
def distribuir_imagens(caminho_origem, categoria, max_imagens=500):
    imagens_encontradas = []
    
    # Procura todas as imagens nas pastas baixadas
    for root, dirs, files in os.walk(caminho_origem):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                imagens_encontradas.append(os.path.join(root, file))
    
    # Embaralha para não pegar imagens sequenciais repetidas
    random.shuffle(imagens_encontradas)
    
    # Limita o número de imagens (GitHub tem limite de tamanho e no Colab fica mais rápido)
    imagens = imagens_encontradas[:max_imagens] 
    print(f"Total de {categoria}s selecionados: {len(imagens)}")
    
    # Define o corte de 80% para treino
    split_idx = int(len(imagens) * 0.8) 
    
    for i, img_path in enumerate(imagens):
        destino_split = 'treino' if i < split_idx else 'teste'
        nome_arquivo = f"{categoria}_{i}.jpg"
        destino_final = os.path.join(base_dir, destino_split, categoria, nome_arquivo)
        
        # Copia da pasta oculta do kagglehub para o seu repositório
        shutil.copy(img_path, destino_final)

print("\nOrganizando as imagens de navios/barcos...")
distribuir_imagens(path_ships, 'barco', max_imagens=600)

print("\nOrganizando as imagens de aviões...")
distribuir_imagens(path_airplanes, 'aviao', max_imagens=600)

print("\nTudo pronto! As imagens estão nas pastas corretas.")
