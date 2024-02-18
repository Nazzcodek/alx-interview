#!/usr/bin/node
const axios = require('axios');
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${process.argv[2]}/`;

async function fetchFilmCharacters(url) {
  try {
    const response = await axios.get(url);
    const characters = response.data.characters;

    if (characters && characters.length >  0) {
      await fetchCharacterNames(characters);
    }
  } catch (error) {
    console.error(error);
  }
}

async function fetchCharacterNames(characters) {
  for (const characterUrl of characters) {
    try {
      const response = await axios.get(characterUrl);
      console.log(response.data.name);
    } catch (error) {
      console.error('error:', error);
    }
  }
}

fetchFilmCharacters(urlMovie);
