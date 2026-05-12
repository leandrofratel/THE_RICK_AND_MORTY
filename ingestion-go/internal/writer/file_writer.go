/*
Salva qualquer dado em um arquivo JSON com formatação identada
*/

package writer

import (
	"encoding/json"
	"os"
)

func Save(path string, data interface{}) error {
	file, err := os.Create(path)
	if err != nil {
		return nil
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	encoder.SetIndent("", " ")

	return encoder.Encode(data)

}
