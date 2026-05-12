/*
Client.go

Script responsável por realizar chamadas api. 

*/

package client

import (
	"encoding/json"
	"net/http"
	"fmt"
)

func GetJSON(url string, target interface{}) error {
	resp, err := http.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	// Verifica o statuscode da api
	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("Erro na API: Status %d", resp.StatusCode)
	}

	return json.NewDecoder(resp.Body).Decode(target)
}
