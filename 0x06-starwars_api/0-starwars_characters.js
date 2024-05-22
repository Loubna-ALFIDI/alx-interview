#!/usr/bin/node

const request = require('request');

// Function to fetch characters for a given movie ID
function fetchStarWarsCharacters (movieId) {
  const baseUrl = 'https://swapi.dev/api';
  const filmUrl = `${baseUrl}/films/${movieId}/`;

  request(filmUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error(`An error occurred: ${error.message}`);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Failed to fetch movie data: ${response.statusCode}`);
      return;
    }

    const characterUrls = body.characters;

    // Fetch and print each character's name
    characterUrls.forEach(url => {
      request(url, { json: true }, (error, response, body) => {
        if (error) {
          console.error(`An error occurred: ${error.message}`);
          return;
        }

        if (response.statusCode !== 200) {
          console.error(`Failed to fetch character data: ${response.statusCode}`);
          return;
        }

        console.log(body.name);
      });
    });
  });
}

// Ensure the script is called with the correct number of arguments
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Fetch and print the characters for the specified movie
fetchStarWarsCharacters(movieId);
