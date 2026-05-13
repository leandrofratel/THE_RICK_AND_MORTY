package main

import (
	"fmt"
	"time"

	"github.com/leandro/rickmorty-ingestion/internal/fetcher"
	"github.com/leandro/rickmorty-ingestion/internal/writer"
)

func ingest(resource string) {
	url := fmt.Sprintf(
		"https://rickandmortyapi.com/api/%s",
		resource,
	)

	page := 1

	for url != "" {
		fmt.Printf(
			"Buscando %s - página: %d\n",
			resource,
			page,
		)

		resp, err := fetcher.FetchResource(url)
		if err != nil {
			panic(err)
		}

		filename := fmt.Sprintf(
			"../data/raw/%ss/page_%d.json",
			resource,
			page,
		)

		err = writer.Save(filename, resp)
		if err != nil {
			panic(err)
		}

		if resp.Info.Next == nil {
			break
		}

		url = *resp.Info.Next
		page++

		time.Sleep(500 * time.Millisecond)
	}

	fmt.Printf("\n%s concluído\n\n", resource)
}

func main() {
	resources := []string{
		"character",
		"location",
		"episode",
	}

	for _, resource := range resources {
		ingest(resource)
	}

	fmt.Println("Ingestão finalizada")
}