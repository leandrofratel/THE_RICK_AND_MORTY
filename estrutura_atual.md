THE_RICK_AND_MORTY/
│
├── ingestion-go/                         # camada de ingestão (Go)
│   ├── cmd/
│   │   └── main.go                      # ponto de entrada
│   │
│   ├── internal/
│   │   ├── client/                      # cliente HTTP
│   │   ├── fetcher/                     # lógica de leitura da API
│   │   ├── writer/                      # gravação dos arquivos raw
│   │   └── models/                      # structs/modelos
│   │
│   └── go.mod
│
├── transformation-python/               # transformação (Python)
│   ├── .venv/
│   ├── src/
│   │   ├── extract.py                   # raw -> parquet
│   │   ├── transform.py                 # flatten + limpeza
│   │   └── download_images.py           # download das imagens
│   │
│   ├── pyproject.toml
│   └── uv.lock
│
├── data/
│   │
│   ├── raw/                             # Bronze
│   │   ├── characters/
│   │   │   ├── page_1.json
│   │   │   └── ...
│   │   │
│   │   ├── locations/
│   │   │   ├── page_1.json
│   │   │   └── ...
│   │   │
│   │   └── episodes/
│   │       ├── page_1.json
│   │       └── ...
│   │
│   ├── silver/                          # Silver
│   │   ├── characters.parquet
│   │   ├── locations.parquet
│   │   └── episodes.parquet
│   │
│   └── images/
│       ├── 1.jpeg
│       ├── 2.jpeg
│       └── ...
│
├── docs/                                # (ainda vazio)
│   └── architecture.md
│
└── README.md                            # (a construir)