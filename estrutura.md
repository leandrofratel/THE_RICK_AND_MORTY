rick-and-morty-data-platform/
│
├── ingestion-go/
│   ├── cmd/
│   ├── internal/
│   │   ├── client/
│   │   ├── fetcher/
│   │   ├── writer/
│   │   └── models/
│   └── main.go
│
├── transformation-python/
│   ├── notebooks/
│   ├── src/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│
├── sql/
│   ├── ddl.sql
│   └── views.sql
│
├── powerbi/
│   └── dashboard.pbix
│
├── data/
│   ├── raw/
│   ├── silver/
│   └── gold/
│
├── docker-compose.yml
└── README.md