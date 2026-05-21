import json
import pandas as pd
from pathlib import Path

CAMINHO_RAW = Path("../data/raw/characters")
CAMINHO_GOLD = Path("../data/gold")
CAMINHO_SILVER = Path("../data/silver")

def criar_fact_character_episode():
    registros = []
    arquivos = sorted(CAMINHO_RAW.glob("*.json"))

    # printa a quantidade de arquivos
    print(f"{len(arquivos)}")

    for arquivo in arquivos:
        print(f"Lendo: {arquivo.name}")
        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for personagem in dados["results"]:
            character_id = personagem["id"]

            for url in personagem["episode"]:
                episode_id = int(url.split("/")[-1])
                registros.append(
                    {
                        "character_id": character_id,
                        "episode_id": episode_id
                    }
                )
    df = pd.DataFrame(registros)

    arquivo_saida = (CAMINHO_GOLD / "fact_character_episode.parquet")
    df.to_parquet(arquivo_saida, index=False)

    print(f"Arquivo salvo em: {arquivo_saida}")


def criar_dim_character():
    arquivo = CAMINHO_SILVER / "characters.parquet"
    df = pd.read_parquet(arquivo)
    df = df[
        [
            "id",
            "name",
            "status",
            "species",
            "gender",
            "type",
            "origin_name",
            "origin_dimension",
            "location_name",
            "current_dimension",
            "image_path",
            "episode_count",
            "first_episode_name",
            "last_episode_name",
        ]
    ]

    # Adiciona o valor 'Unknown' para as colunas null
    df['origin_dimension'] = df['origin_dimension'].replace("", "unknown").fillna("unknown")
    df['current_dimension'] = df['current_dimension'].replace("", "unknown").fillna("unknown")
    df['type'] = df['type'].replace('', 'unknown').fillna("unknown")

    arquivo_saida = (CAMINHO_GOLD / "dim_character.parquet")
    df.to_parquet(arquivo_saida, index=False)

    print(f"\nArquivo salvo em: {arquivo_saida}\n")


def criar_dim_location():
    arquivo = CAMINHO_SILVER / "locations.parquet"
    df = pd.read_parquet(arquivo)
    df = df[
        [
            "id",
            "name",
            "type",
            "dimension",
            "resident_count",
        ]
    ]

    # Converte primeira letra de cada palavra em Maiuscula
    df["dimension"] = df["dimension"].str.title()

    # Substitui valores pelo 'Unknown Dimension'
    df["dimension"] = df["dimension"].replace({
        "Unknown": "Unknown Dimension",
        "": "Unknown Dimension",
    }).fillna("Unknown Dimension")


    arquivo_saida = (CAMINHO_GOLD / "dim_location.parquet")
    df.to_parquet(arquivo_saida, index=False)

    print(f"\nArquivo salvo em: {arquivo_saida}\n")


def criar_dim_episode():
    arquivo = CAMINHO_SILVER / "episodes.parquet"
    df = pd.read_parquet(arquivo)
    df = df[
        [
            "id",
            "name",
            "air_date",
            "season",
            "episode_number",
            "character_count"
        ]
    ]

    # Formatar coluna de air_data (Quando foi ao ar)
    # Converte para o formato DD/MM/AAAA
    df["air_date"] = pd.to_datetime(df["air_date"]).dt.strftime("%d/%m/%Y")


    arquivo_saida = (CAMINHO_GOLD / "dim_episode.parquet")
    df.to_parquet(arquivo_saida, index=False)
    print(f"\nArquivo salvo em: {arquivo_saida}\n")


if __name__=="__main__":
    # criar_fact_character_episode()
    # criar_dim_character()
    # criar_dim_location()
    criar_dim_episode()
