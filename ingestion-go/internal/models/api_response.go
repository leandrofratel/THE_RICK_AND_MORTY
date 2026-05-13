/*
Models: -- Contrato de dados --

Camada responsável por definir os dados que a API vai
receber e retornar e manipular internamente.

*/

package models

type ApiResponse struct {
	Info    Info          `json:"info"`
	Results []interface{} `json:"results"`
}

type Info struct {
	Count int     `json:"count"`
	Pages int     `json:"pages"`
	Next  *string `json:"next"`
	Prev  *string `json:"prev"`
}
