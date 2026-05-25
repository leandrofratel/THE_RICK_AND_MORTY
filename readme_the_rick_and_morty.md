# THE_RICK_AND_MORTY

![Capa do Projeto](Design_Dash_Rick_and_Morty\Referencias\capa_projeto.jpg)

Projeto end-to-end de **Engenharia de Dados**, **Analytics** e **Análise de Redes Sociais (SNA)** utilizando a API pública do Rick and Morty como fonte de dados.

---

# Objetivo do projeto

Construir um pipeline moderno de dados, cobrindo todas as etapas de um projeto real:

- ingestão de dados via API;
- transformação e enriquecimento;
- modelagem dimensional (Data Warehouse);
- visualização analítica em dashboard;
- análise de relacionamento entre entidades (Social Graph).

Além do resultado técnico, o projeto foi desenvolvido com foco em **aprendizado prático**, **portfólio profissional** e aplicação de boas práticas de Engenharia de Dados.

---

# Arquitetura do projeto

```text
Rick and Morty API
        │
        ▼
Ingestion (Go)
        │
        ▼
RAW / Bronze (JSON)
        │
        ▼
Transformation (Python)
        │
        ▼
Silver (Parquet)
        │
        ▼
Load / Data Warehouse
        │
        ▼
Gold (Star Schema)
        │
        ├── Power BI Dashboard
        │
        └── Social Network Analysis
```

---

# Tecnologias utilizadas

## Ingestão
- Golang
- REST API
- JSON

## Transformação
- Python
- Pandas
- PyArrow
- UV

## Armazenamento
- Parquet
- Arquitetura em camadas (Bronze / Silver / Gold)

## Visualização
- Power BI

## Versionamento
- Git
- GitHub

---

# Fonte de dados

API pública do Rick and Morty:

- Characters
- Episodes
- Locations

Documentação utilizada:
- https://rickandmortyapi.com/documentation

---

# Estrutura do projeto

```text
THE_RICK_AND_MORTY/
│
├── ingestion-go/
│   ├── cmd/
│   │   └── main.go
│   ├── internal/
│   │   ├── client/
│   │   ├── fetcher/
│   │   ├── writer/
│   │   └── models/
│   └── go.mod
│
├── transformation-python/
│   ├── src/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   │   └── validation.py
│   └── pyproject.toml
│
├── data/
│   ├── raw/
│   │   ├── characters/
│   │   ├── episodes/
│   │   └── locations/
│   ├── silver/
│   ├── gold/
│   └── images/
│
└── analysis_checklist.txt
```

---

# Camadas de dados

## Bronze / RAW
Arquivos JSON brutos extraídos diretamente da API.

Exemplo:
- `data/raw/characters/page_1.json`

---

## Silver
Dados tratados e enriquecidos em Parquet.

Tabelas:
- `characters.parquet`
- `episodes.parquet`
- `locations.parquet`

Transformações aplicadas:
- flatten de colunas aninhadas;
- limpeza de valores nulos;
- enriquecimento com dimensões;
- criação de colunas analíticas.

Exemplos:
- `origin_dimension`
- `current_dimension`
- `first_episode_name`
- `last_episode_name`

---

## Gold (Data Warehouse)
Modelagem dimensional em esquema estrela.

### Tabela fato
- `fact_character_episode.parquet`

### Dimensões
- `dim_character.parquet`
- `dim_location.parquet`
- `dim_episode.parquet`

Modelo:

```text
                fact_character_episode
                         |
            -----------------------------
            |                           |
      dim_character               dim_episode
            |
      dim_location
```

---

# Análises planejadas

## Sprint 4 — Dashboard (Power BI)

Páginas planejadas:
- Overview
- Characters
- Episodes
- Locations

Indicadores:
- total de personagens;
- total de episódios;
- personagens por episódio;
- distribuição por espécie;
- distribuição por status;
- localizações por dimensão.

---

## Sprint 5 — Social Network Analysis

Objetivo:
criar uma rede social entre personagens baseada em coocorrência nos episódios.

Perguntas que serão respondidas:
- quais são os personagens mais importantes?
- quais comunidades se formam?
- como a importância muda ao longo da série?

Biblioteca prevista:
- NetworkX

---

# Aprendizados aplicados

Este projeto foi inspirado em duas grandes referências que contribuíram para meu aprendizado:

- estudos de **Golang** através dos conteúdos do **Teo Calvo**;
- conceitos de **Engenharia de Dados** reforçados pelos conteúdos da **Jornada de Dados**, especialmente com **Luciano Vasconcelos**.

---

# Status do projeto

```text
Sprint 1  ✅ Ingestão Go
Sprint 2  ✅ Silver
Sprint 2.5 ✅ Enriquecimento
Sprint 3  ✅ Gold
Sprint 4  ⏳ Dashboard
Sprint 5  ⏳ Social Graph
```

---

# Autor

**Leandro Fratel**  
Projeto desenvolvido para prática, portfólio e consolidação de conhecimentos em Engenharia e Análise de Dados.

