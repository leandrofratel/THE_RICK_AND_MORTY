## Extrair dados RAW e converter em parquet

import json
import pandas as pd

from pathlib import Path

CAMINHO_RAW = Path("../data/raw/characters")
CAMINHO_SILVER = Path("../data/silver")

print(CAMINHO_RAW)

def extrair_personagens():
    """ Extrai todos os arquivos json da pasta RAW e concatena em um arquivo unico """
    todos_registros = []
    arquivos = sorted(CAMINHO_RAW.glob("*.json"))
    print(f"{len(arquivos)} arquivos encontrados")

    ## Lê cada arquivo json e imprime o nome na tela
    for arquivo in arquivos:
        print(f"lendo: {arquivo.name}")

        with open(arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        ## Converte todos os registros em data frame.
        todos_registros.extend(dados["results"])

    df = pd.DataFrame(todos_registros)
    print(f"{len(df)} registros carregados")
    
    return df

def extrair_personagens():
    pass

def extrair_localizacoes():
    pass

def salvar_parquet(df):
    """ Salva os arquivos concatenados em uma tabela em parquet """
    
    ## Verifica se a pasta de destino existe
    CAMINHO_SILVER.mkdir(parents=True, exist_ok=True)

    arquivo_saida = CAMINHO_SILVER / "characters.parquet"
    df.to_parquet(arquivo_saida, index=False)
    print(f"Arquivo salo em: {arquivo_saida}")

if __name__ == "__main__":
    ## Execução do script
    df = extrair_personagens()
    salvar_parquet(df)