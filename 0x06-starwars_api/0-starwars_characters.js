#!/usr/bin/node
const request = require('request');
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${process.argv[2]}/`;

request(urlMovie, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  if (characters && characters.length >  0) {
    characters.forEach(function(characterUrl, index) {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('Error:', error);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  } else {
    console.log('No characters found for this movie.');
  }
});

