import pandas as pd
from pathlib import Path


CAMINHO_SILVER = Path("../data/silver")


def transformar_personagens():
    arquivo = CAMINHO_SILVER / "characters.parquet"
    df = pd.read_parquet(arquivo)

    df["origin_name"] = df["origin"].apply(lambda x: x["name"])
    df["location_name"] = df["location"].apply(lambda x: x["name"])
    df["episode_count"] = df["episode"].apply(len)
    df["image_path"] = df["id"].apply(
        lambda x: f"../data/images/{x}.jpeg"
    )

    df.drop(
        columns=["origin", "location", "episode", "url", "created"],
        inplace=True
    )

    df.to_parquet(arquivo, index=False)

    print("Characters transformado")


def transformar_localizacoes():
    arquivo = CAMINHO_SILVER / "locations.parquet"
    df = pd.read_parquet(arquivo)

    df["resident_count"] = df["residents"].apply(len)

    df.drop(
        columns=["residents", "url", "created"],
        inplace=True
    )

    df.to_parquet(arquivo, index=False)

    print("Locations transformado")


def transformar_episodios():
    arquivo = CAMINHO_SILVER / "episodes.parquet"
    df = pd.read_parquet(arquivo)

    df["character_count"] = df["characters"].apply(len)

    df["season"] = df["episode"].str[1:3].astype(int)
    df["episode_number"] = df["episode"].str[4:6].astype(int)

    df.drop(
        columns=["characters", "episode", "url", "created"],
        inplace=True
    )

    df.to_parquet(arquivo, index=False)

    print("Episodes transformado")


if __name__ == "__main__":
    transformar_personagens()
    transformar_localizacoes()
    transformar_episodios()