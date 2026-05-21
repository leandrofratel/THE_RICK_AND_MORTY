import pandas as pd
from pathlib import Path


CAMINHO_SILVER = Path("../data/silver")


def transformar_personagens():
    arquivo = CAMINHO_SILVER / "characters.parquet"
    arquivo_locations = CAMINHO_SILVER / "locations.parquet"
    arquivo_episodes = CAMINHO_SILVER / "episodes.parquet"

    df = pd.read_parquet(arquivo)
    df_locations = pd.read_parquet(arquivo_locations)
    df_episodes = pd.read_parquet(arquivo_episodes)

    # flatten
    df["origin_name"] = df["origin"].apply(lambda x: x["name"])
    df["location_name"] = df["location"].apply(lambda x: x["name"])
    df["episode_count"] = df["episode"].apply(len)

    # primeiro episódio
    df["first_episode_id"] = df["episode"].apply(
        lambda x: int(x[0].split("/")[-1])
    )

    # último episódio
    df["last_episode_id"] = df["episode"].apply(
        lambda x: int(x[-1].split("/")[-1])
    )

    mapa_episodios = dict(
        zip(df_episodes["id"], df_episodes["name"])
    )

    df["first_episode_name"] = df["first_episode_id"].map(
        mapa_episodios
    )

    df["last_episode_name"] = df["last_episode_id"].map(
        mapa_episodios
    )

    # imagem local
    df["image_path"] = df["id"].apply(
        lambda x: f"../data/images/{x}.jpeg"
    )

    # join dimensões
    mapa_dimensoes = dict(
        zip(df_locations["name"], df_locations["dimension"])
    )

    df["origin_dimension"] = df["origin_name"].map(
        mapa_dimensoes
    )

    df["current_dimension"] = df["location_name"].map(
        mapa_dimensoes
    )

    # remover colunas antigas
    df.drop(
        columns=[
            "origin",
            "location",
            "episode",
            "url",
            "created",
        ],
        inplace=True
    )

    df.to_parquet(arquivo, index=False)
    print("Characters enriquecido")


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

    df["air_date"] = pd.to_datetime(df["air_date"])
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