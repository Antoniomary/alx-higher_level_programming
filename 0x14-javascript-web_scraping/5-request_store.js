#!/usr/bin/node

const ac = process.argv.length;
if (ac === 4) {
  const request = require('request');
  const url = process.argv[2];
  const filename = process.argv[3];
  request(url, (error, response, body) => {
    if (error) {
      return;
    }
    if (response && response.statusCode === 200) {
      const fs = require('fs');
      fs.writeFileSync(filename, body, 'utf-8');
    }
  });
}
