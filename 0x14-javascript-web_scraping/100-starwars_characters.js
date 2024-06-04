#!/usr/bin/node

const ac = process.argv.length;
if (ac === 3) {
  const request = require('request');
  const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
  request({ url: api, json: true }, (error, response, body) => {
    if (error) {
      return;
    }
    for (const person of body.characters) {
      request({ url: person, json: true }, (error, response, body1) => {
        if (error) console.error('Error');
        else console.log(body1.name);
      });
    }
  });
}
