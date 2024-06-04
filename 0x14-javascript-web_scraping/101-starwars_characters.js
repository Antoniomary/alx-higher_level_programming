#!/usr/bin/node

const ac = process.argv.length;
const request = require('request');
if (ac === 3) {
  const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  request({ url: api, json: true }, (error, response, body) => {
    if (error) {
      return;
    }
    getName(0, body.characters);
  });
}

const getName = (index, characters) => {
  if (index >= characters.length) return;
  request({ url: characters[index], json: true }, (error, response, body) => {
    if (error) console.error('Error');
    else console.log(body.name);
    getName(++index, characters);
  });
};
