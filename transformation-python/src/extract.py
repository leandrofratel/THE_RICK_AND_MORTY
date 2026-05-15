from pathlib import Path
import json
import pandas as pd


CAMINHO_RAW = Path("../data/raw")
CAMINHO_SILVER = Path("../data/silver")


def extrair_json(pasta):
    todos_registros = []

    caminho = CAMINHO_RAW / pasta
    arquivos = sorted(caminho.glob("*.json"))

    print(f"{len(arquivos)} arquivos encontrados em {pasta}")

    for arquivo in arquivos:
        print(f"Lendo: {arquivo.name}")

        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        todos_registros.extend(dados["results"])

    df = pd.DataFrame(todos_registros)

    print(f"{len(df)} registros carregados")

    return df


def salvar_parquet(df, nome_arquivo):
    CAMINHO_SILVER.mkdir(parents=True, exist_ok=True)

    arquivo_saida = CAMINHO_SILVER / nome_arquivo

    df.to_parquet(arquivo_saida, index=False)

    print(f"Arquivo salvo em: {arquivo_saida}")


def extrair_personagens():
    df = extrair_json("characters")
    salvar_parquet(df, "characters.parquet")


def extrair_localizacoes():
    df = extrair_json("locations")
    salvar_parquet(df, "locations.parquet")


def extrair_episodios():
    df = extrair_json("episodes")
    salvar_parquet(df, "episodes.parquet")


if __name__ == "__main__":
    extrair_personagens()
    extrair_localizacoes()
    extrair_episodios()