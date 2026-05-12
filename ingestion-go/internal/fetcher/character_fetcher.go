package fetcher

import (
	"github.com/leandro/rickmorty-ingestion/internal/client"
	"github.com/leandro/rickmorty-ingestion/internal/models"
)

func FetchCharacters(url string) (*models.CharacterResponse, error) {
	var response models.CharacterResponse

	err := client.GetJSON(url, &response)
	if err != nil {
		return nil, err
	}

	return &response, nil
}