#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(`/api/people/${characterId}/`)) {
          count++;
        }
      });
    });

    console.log(count);
  }
});

