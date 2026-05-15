import pandas as pd
from pathlib import Path

CAMINHO_SILVER = Path("../data/silver")

def transformar_personagens():
    arquivo = CAMINHO_SILVER / "characters.parquet"
    df = pd.read_parquet(arquivo)

    # flatten origin
    df["origin_name"] = df["origin"].apply(lambda x: x["name"])

    # flatten location
    df["location_name"] = df["location"].apply(lambda x: x["name"])

    # quantidade de episodios
    df["episode_count"] = df["episode"].apply(len)

    # caminho local da imagem
    df["imagem_path"] = df["id"].apply(
        lambda x: f"../data/images{x}.jpeg"
    )

    # remover colunas antigas
    df.drop(
        columns=[
            "origin",
            "location",
            "episode",
            "url",
            "created",
        ], inplace=True
    )

    # sobrescreve
    df.to_parquet(arquivo, index=False)

    print("\n\n Transformação Concluída\n\n")

def transformar_episodios():
    pass

def transformar_localizacoes():
    pass

if __name__=="__main__":
    transformar_personagens()