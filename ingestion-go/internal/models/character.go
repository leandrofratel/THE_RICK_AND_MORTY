/*
Models: -- Contrato de dados --

Camada responsável por definir os dados que a API vai
receber e retornar e manipular internamente.

*/

package models

type CharacterResponse struct {
	Info    Info        `json:"info"`
	Results []Character `json:"results"`
}

type Info struct {
	Count int     `json:"count"`
	Pages int     `json:"pages"`
	Next  *string `json:"next"`
	Prev  *string `json:"prev"`
}

type Character struct {
	ID      int    `json:"id"`
	Name    string `json:"name"`
	Status  string `json:"status"`
	Species string `json:"species"`
	Gender  string `json:"gender"`
}
