#!/usr/bin/node

const ac = process.argv.length;
if (ac === 3) {
  const request = require('request');
  const api = process.argv[2];
  request({ url: api, json: true }, (error, response, body) => {
    if (error) console.error(`Error: ${error.message}`);
    else {
      let count = 0;
      const id = '18';
      for (let i = 0; i < body.results.length; ++i) {
        for (const person of body.results[i].characters) {
          if (person.includes(id)) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
