#!/usr/bin/node

const ac = process.argv.length;
if (ac === 3) {
  const request = require('request');
  const api = process.argv[2];
  request({ url: api, json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    let count = 0;
    const key = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (let i = 0; i < body['results'].length; ++i) {
      if (body['results'][i].characters.includes(key)) {
        count++;
      }
    }
    console.log(count);
  });
}
