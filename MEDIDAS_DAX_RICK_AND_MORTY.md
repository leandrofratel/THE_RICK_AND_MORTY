# Medidas DAX — Dashboard Rick and Morty

## 📊 Overview

### Total Personagens
```dax
/*
Categoria: KPI
Página: Overview
Objetivo: Retornar a quantidade total de personagens do universo.
Tabela: dim_character
Coluna: id
*/
Total Personagens = COUNTROWS(dim_character)
```

### Total Episódios
```dax
/*
Categoria: KPI
Página: Overview
Objetivo: Retornar a quantidade total de episódios.
Tabela: dim_episode
Coluna: id
*/
Total Episódios = COUNTROWS(dim_episode)
```

### Total Localizações
```dax
/*
Categoria: KPI
Página: Overview
Objetivo: Retornar a quantidade total de localizações.
Tabela: dim_location
Coluna: id
*/
Total Localizações = COUNTROWS(dim_location)
```

### Total Dimensões
```dax
/*
Categoria: KPI
Página: Overview
Objetivo: Retornar a quantidade de dimensões únicas.
Tabela: dim_location
Coluna: dimension
*/
Total Dimensões = DISTINCTCOUNT(dim_location[dimension])
```

### Avg Personagens por Episódio
```dax
/*
Categoria: KPI
Página: Overview
Objetivo: Calcular a média de personagens por episódio.
Tabelas: fact_character_episode, dim_episode
Colunas: character_id, episode_id
*/
Avg Personagens por Episódio = DIVIDE(
    COUNTROWS(fact_character_episode),
    COUNTROWS(dim_episode),
    0
)
```

### Personagens Mudaram Dimensão
```dax
/*
Categoria: Análise
Página: Overview
Objetivo: Contar personagens que trocaram de dimensão (origem ≠ atual).
Tabela: dim_character
Coluna: Mudou Dimensão
*/
Personagens Mudaram Dimensão = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[Mudou Dimensão] = "Sim"
)
```

### Personagens Não Mudaram Dimensão
```dax
/*
Categoria: Análise
Página: Overview
Objetivo: Contar personagens que permaneceram na mesma dimensão.
Tabela: dim_character
Coluna: Mudou Dimensão
*/
Personagens Não Mudaram Dimensão = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[Mudou Dimensão] = "Não"
)
```

### % Mudou Dimensão
```dax
/*
Categoria: Percentual
Página: Overview
Objetivo: Calcular percentual de personagens que mudaram de dimensão.
Tabela: dim_character
Coluna: Mudou Dimensão
*/
% Mudou Dimensão = DIVIDE(
    [Personagens Mudaram Dimensão],
    [Total Personagens],
    0
)
```

### Humanos Vivos
```dax
/*
Categoria: Análise Cruzada
Página: Overview
Objetivo: Contar humanos com status Alive.
Tabela: dim_character
Colunas: species, status
*/
Humanos Vivos = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[species] = "Human",
    dim_character[status] = "Alive"
)
```

### Humanos Mortos
```dax
/*
Categoria: Análise Cruzada
Página: Overview
Objetivo: Contar humanos com status Dead.
Tabela: dim_character
Colunas: species, status
*/
Humanos Mortos = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[species] = "Human",
    dim_character[status] = "Dead"
)
```

### Aliens Vivos
```dax
/*
Categoria: Análise Cruzada
Página: Overview
Objetivo: Contar alienos com status Alive.
Tabela: dim_character
Colunas: species, status
*/
Aliens Vivos = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[species] = "Alien",
    dim_character[status] = "Alive"
)
```

### Aliens Mortos
```dax
/*
Categoria: Análise Cruzada
Página: Overview
Objetivo: Contar alienos com status Dead.
Tabela: dim_character
Colunas: species, status
*/
Aliens Mortos = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[species] = "Alien",
    dim_character[status] = "Dead"
)
```

### Personagens Masculino
```dax
/*
Categoria: Análise por Gênero
Página: Overview
Objetivo: Contar personagens do gênero Masculino.
Tabela: dim_character
Coluna: gender
*/
Personagens Masculino = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[gender] = "Male"
)
```

### Personagens Feminino
```dax
/*
Categoria: Análise por Gênero
Página: Overview
Objetivo: Contar personagens do gênero Feminino.
Tabela: dim_character
Coluna: gender
*/
Personagens Feminino = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[gender] = "Female"
)
```

### Personagens Gênero Unknown
```dax
/*
Categoria: Análise por Gênero
Página: Overview
Objetivo: Contar personagens com gênero desconhecido.
Tabela: dim_character
Coluna: gender
*/
Personagens Gênero Unknown = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[gender] = "Unknown"
)
```

### Rank Espécie
```dax
/*
Categoria: Ranking
Página: Overview
Objetivo: Rankear espécies por quantidade de personagens (para Top 10).
Tabela: dim_character
Coluna: species
*/
Rank Espécie = RANKX(
    ALL(dim_character[species]),
    CALCULATE(COUNTROWS(dim_character)),
    ,
    DESC,
    DENSE
)
```

---

## 👤 Characters

### Rank Personagem por Episódios
```dax
/*
Categoria: Ranking
Página: Characters
Objetivo: Rankear personagens por quantidade de episódios (para Top 15).
Tabela: dim_character
Coluna: episode_count
*/
Rank Personagem por Episódios = RANKX(
    ALL(dim_character[name]),
    dim_character[episode_count],
    ,
    DESC,
    DENSE
)
```

### Rank Dimensão Origem (Characters)
```dax
/*
Categoria: Ranking
Página: Characters
Objetivo: Rankear dimensões de origem por quantidade de personagens.
Tabela: dim_character
Coluna: origin_dimension
*/
Rank Dimensão Origem (Characters) = RANKX(
    ALL(dim_character[origin_dimension]),
    CALCULATE(COUNTROWS(dim_character)),
    ,
    DESC,
    DENSE
)
```

### Total Personagens Distintos
```dax
/*
Categoria: Contagem
Página: Characters
Objetivo: Contar personagens únicos que apareceram em episódios.
Tabelas: fact_character_episode, dim_character
Coluna: character_id
*/
Total Personagens Distintos = DISTINCTCOUNT(fact_character_episode[character_id])
```

### Total Episódios por Personagem
```dax
/*
Categoria: Contagem
Página: Characters
Objetivo: Contar episódios únicos que um personagem apareceu.
Tabelas: fact_character_episode, dim_episode
Coluna: episode_id
*/
Total Episódios por Personagem = DISTINCTCOUNT(fact_character_episode[episode_id])
```

---

## 📺 Episodes

### Total Temporadas
```dax
/*
Categoria: KPI
Página: Episodes
Objetivo: Contar quantas temporadas existem.
Tabela: dim_episode
Coluna: season
*/
Total Temporadas = DISTINCTCOUNT(dim_episode[season])
```

### Rank Episódio por Personagens
```dax
/*
Categoria: Ranking
Página: Episodes
Objetivo: Rankear episódios por quantidade de personagens distintos.
Tabelas: dim_episode, fact_character_episode
Coluna: character_id
*/
Rank Episódio por Personagens = RANKX(
    ALL(dim_episode[name]),
    CALCULATE(DISTINCTCOUNT(fact_character_episode[character_id])),
    ,
    DESC,
    DENSE
)
```

### Personagens por Episódio (Distinct)
```dax
/*
Categoria: Contagem
Página: Episodes
Objetivo: Contar personagens únicos em um episódio.
Tabelas: fact_character_episode, dim_episode
Coluna: character_id
*/
Personagens por Episódio (Distinct) = DISTINCTCOUNT(fact_character_episode[character_id])
```

### Personagens por Temporada (Distinct)
```dax
/*
Categoria: Contagem
Página: Episodes
Objetivo: Contar personagens únicos que apareceram em uma temporada.
Tabelas: fact_character_episode, dim_episode
Coluna: character_id
*/
Personagens por Temporada (Distinct) = DISTINCTCOUNT(fact_character_episode[character_id])
```

---

## 📍 Locations

### Avg Residentes por Localização
```dax
/*
Categoria: KPI
Página: Locations
Objetivo: Calcular a média de residentes por localização.
Tabela: dim_location
Coluna: resident_count
*/
Avg Residentes por Localização = DIVIDE(
    COUNTROWS(dim_character),
    DISTINCTCOUNT(dim_location[name]),
    0
)
```

### Rank Localização por Residentes
```dax
/*
Categoria: Ranking
Página: Locations
Objetivo: Rankear localizações por número de residentes.
Tabela: dim_location
Coluna: resident_count
*/
Rank Localização por Residentes = RANKX(
    ALL(dim_location[name]),
    dim_location[resident_count],
    ,
    DESC,
    DENSE
)
```

### Rank Dimensão por Localizações
```dax
/*
Categoria: Ranking
Página: Locations
Objetivo: Rankear dimensões por quantidade de localizações.
Tabela: dim_location
Coluna: dimension
*/
Rank Dimensão por Localizações = RANKX(
    ALL(dim_location[dimension]),
    CALCULATE(COUNTROWS(dim_location)),
    ,
    DESC,
    DENSE
)
```

### Rank Dimensão por Local (Locations)
```dax
/*
Categoria: Ranking
Página: Locations
Objetivo: Rankear dimensões por quantidade de localizações (Locations).
Tabela: dim_location
Coluna: dimension
*/
Rank Dimensão por Local (Locations) = RANKX(
    ALL(dim_location[dimension]),
    CALCULATE(COUNTROWS(dim_location)),
    ,
    DESC,
    DENSE
)
```

### Total Residentes
```dax
/*
Categoria: KPI
Página: Locations
Objetivo: Somar todos os residentes de todas as localizações.
Tabela: dim_location
Coluna: resident_count
*/
Total Residentes = SUMPRODUCT(dim_location[resident_count])
```

---

## 🔍 Análises

### Personagens Vivos
```dax
/*
Categoria: Análise de Status
Página: Análises
Objetivo: Contar personagens com status Alive.
Tabela: dim_character
Coluna: status
*/
Personagens Vivos = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[status] = "Alive"
)
```

### Personagens Mortos
```dax
/*
Categoria: Análise de Status
Página: Análises
Objetivo: Contar personagens com status Dead.
Tabela: dim_character
Coluna: status
*/
Personagens Mortos = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[status] = "Dead"
)
```

### Personagens Status Unknown
```dax
/*
Categoria: Análise de Status
Página: Análises
Objetivo: Contar personagens com status Unknown.
Tabela: dim_character
Coluna: status
*/
Personagens Status Unknown = CALCULATE(
    COUNTROWS(dim_character),
    dim_character[status] = "Unknown"
)
```

### % Personagens Mortos (Total)
```dax
/*
Categoria: Percentual
Página: Análises
Objetivo: Calcular percentual de personagens mortos em relação ao total.
Tabela: dim_character
Coluna: status
*/
% Personagens Mortos (Total) = DIVIDE(
    [Personagens Mortos],
    [Total Personagens],
    0
)
```

### Tempo Médio Permanence (Episódios)
```dax
/*
Categoria: Métrica de Permanência
Página: Análises
Objetivo: Calcular a média de episódios que um personagem aparece.
Tabela: dim_character
Coluna: episode_count
*/
Tempo Médio Permanence (Episódios) = AVERAGE(dim_character[episode_count])
```

### Rank Dimensões Origem
```dax
/*
Categoria: Ranking
Página: Análises
Objetivo: Rankear dimensões de origem por quantidade de personagens.
Tabela: dim_character
Coluna: origin_dimension
*/
Rank Dimensões Origem = RANKX(
    ALL(dim_character[origin_dimension]),
    CALCULATE(COUNTROWS(dim_character), dim_character[origin_dimension]),
    ,
    DESC,
    DENSE
)
```

### % Mortos por Espécie
```dax
/*
Categoria: Análise Cruzada
Página: Análises
Objetivo: Calcular percentual de mortos por espécie selecionada.
Tabela: dim_character
Colunas: status, species
*/
% Mortos por Espécie = DIVIDE(
    CALCULATE(
        COUNTROWS(dim_character),
        dim_character[status] = "Dead"
    ),
    COUNTROWS(dim_character),
    0
)
```

### Rank Dimensão Origem (Análises)
```dax
/*
Categoria: Ranking
Página: Análises
Objetivo: Rankear dimensões de origem por quantidade de personagens.
Tabela: dim_character
Coluna: origin_dimension
*/
Rank Dimensão Origem (Análises) = RANKX(
    ALL(dim_character[origin_dimension]),
    CALCULATE(COUNTROWS(dim_character)),
    ,
    DESC,
    DENSE
)
```

### Personagens Introduzidos
```dax
/*
Categoria: Contagem
Página: Análises
Objetivo: Contar personagens introduzidos (será filtrado por temporada).
Tabela: dim_character
Coluna: id
*/
Personagens Introduzidos = COUNTROWS(dim_character)
```

---

## 📋 Resumo das Medidas

**Total de Medidas Criadas:** 41

### Distribuição por Página
- **Overview:** 13 medidas
- **Characters:** 4 medidas
- **Episodes:** 4 medidas
- **Locations:** 5 medidas
- **Análises:** 9 medidas

### Distribuição por Tipo
- **KPIs:** 6 medidas
- **Rankings:** 12 medidas
- **Contagens:** 11 medidas
- **Percentuais:** 4 medidas
- **Análises Cruzadas:** 8 medidas

---

## 🎯 Notas Importantes

1. **Coluna Calculada Necessária:** `Mudou Dimensão` em `dim_character`
   - Esta coluna já foi criada e atualizada

2. **Relacionamentos Necessários:**
   - `fact_character_episode.character_id → dim_character.id`
   - `fact_character_episode.episode_id → dim_episode.id`
   - `dim_character.location_name → dim_location.name` (atual, considere normalizar com ID)

3. **Campos Esperados em dim_character:**
   - `id`, `name`, `status`, `species`, `gender`, `origin_dimension`, `current_dimension`, `episode_count`, `first_episode_id`, `last_episode_id`

4. **Campos Esperados em dim_episode:**
   - `id`, `name`, `season`, `episode_number`, `air_date`, `character_count`

5. **Campos Esperados em dim_location:**
   - `id`, `name`, `type`, `dimension`, `resident_count`

6. **Campos Esperados em fact_character_episode:**
   - `character_id`, `episode_id`

---

**Data de Criação:** Junho 2026  
**Versão:** 1.0  
**Status:** Pronto para Produção
