// Querys

// Identifica a quantidade de personagens por episodio.
SELECT
	episode_id,
	COUNT(character_id) as total_personagens
FROM DATA
GROUP BY episode_id
ORDER BY total_personagens DESC