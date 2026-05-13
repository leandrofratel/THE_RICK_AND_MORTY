package fetcher

import (
	"github.com/leandro/rickmorty-ingestion/internal/client"
	"github.com/leandro/rickmorty-ingestion/internal/models"
)

func FetchResource(url string) (*models.ApiResponse, error) {
	var response models.ApiResponse

	err := client.GetJSON(url, &response)
	if err != nil {
		return nil, err
	}

	return &response, nil
}