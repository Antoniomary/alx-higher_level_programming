#!/usr/bin/node

const ac = process.argv.length;
if (ac === 3) {
  const request = require('request');
  request(process.argv[2], (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }
    console.log(`code: ${response.statusCode}`);
  });
}
