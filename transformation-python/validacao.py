import pandas as pd
from pathlib import Path


fact = "../data/gold/fact_character_episode.parquet"
dim_1 = "../data/gold/dim_character.parquet"
dim_2 = "../data/gold/dim_location.parquet"
dim_3 = "../data/gold/dim_episode.parquet"


def validacao_parquet(caminho):
    df = pd.read_parquet(caminho)

    nome_arquivo = Path(caminho).name

    print("=" * 50)
    print(f"Tabela: {nome_arquivo}")
    print("=" * 50)

    print(f"\n{'=' * 15} Shape {'=' * 15}")
    print(df.shape)

    print(f"\n{'=' * 15} Head {'=' * 15}")
    print(df.head())

    print(f"\n{'=' * 15} Info {'=' * 15}")
    df.info()

    print(f"\n{'=' * 15} Valores nulos {'=' * 15}")
    print(df.isnull().sum())

    print(f"\n{'=' * 15} Duplicados {'=' * 15}")
    print(df.duplicated().sum())

    print("\n")


if __name__ == "__main__":
    # validacao_parquet(fact)
    # validacao_parquet(dim_1)
    # validacao_parquet(dim_2)
    validacao_parquet(dim_3)