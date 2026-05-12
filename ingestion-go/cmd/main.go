package main

import (
	"fmt"
	"time"

	"github.com/leandro/rickmorty-ingestion/internal/fetcher"
	"github.com/leandro/rickmorty-ingestion/internal/writer"
)

func main() {
	url := "https://rickandmortyapi.com/api/character"
	page := 1

	for url != "" {
		fmt.Println("Buscando página:", page)

		resp, err := fetcher.FetchCharacters(url)
		if err != nil {
			panic(err)
		}

		filename := fmt.Sprintf(
			"../data/raw/character_page_%d.json",

			page,
		)

		err = writer.Save(filename, resp)
		if err != nil {
			panic(err)
		}

		// adiciona um delay
		time.Sleep(500 * time.Millisecond)

		if resp.Info.Next == nil {
			break
		}

		url = *resp.Info.Next
		page++
	}

	fmt.Println("Ingestão de dados concluida!")
}
