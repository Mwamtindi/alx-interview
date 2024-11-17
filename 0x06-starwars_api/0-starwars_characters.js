#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data. Status Code: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Function to fetch and print character names sequentially
  const fetchCharacter = (index) => {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
      fetchCharacter(index + 1); // Proceed to the next character
    });
  };

  fetchCharacter(0); // Start fetching from the first character
});
