from pathlib import Path
import pandas as pd
import requests
from time import sleep


## Caminho relativo dos arquivos.
CAMINHO_SILVER = Path("../data/silver")
CAMINHO_IMAGENS = Path("../data/images")

def baixar_imagens():
    """Baixa e armazena as imagens referente a cada personagem"""
    arquivo = CAMINHO_SILVER / "characters.parquet"
    df = pd.read_parquet(arquivo)

    # Cria a pasta para armazenar as imagens (se não houver)
    CAMINHO_IMAGENS.mkdir(parents=True, exist_ok=True)

    for _, linha in df.iterrows():
        personagem_id = linha["id"]
        url_imagem = linha["image"]

        extensao = url_imagem.split(".")[-1]
        nome_arquivo = f"{personagem_id}.{extensao}"

        caminho_saida = CAMINHO_IMAGENS / nome_arquivo

        if caminho_saida.exists():
            continue

        print(f"Baixando: {nome_arquivo}")
        resposta = requests.get(url_imagem)
        sleep(0.3)


        with open(caminho_saida, "wb") as f:
            f.write(resposta.content)
    
    print("Donwload Concluído")


if __name__=="__main__":
    baixar_imagens()