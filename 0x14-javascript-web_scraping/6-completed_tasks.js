#!/usr/bin/node

const ac = process.argv.length;
if (ac === 3) {
  const request = require('request');
  const api = process.argv[2];
  request({ url: api, json: true }, (error, response, body) => {
    if (error) {
      return;
    }
    const result = {};
    for (let i = 0; i < body.length; ++i) {
      if (body[i].completed === true) {
        if (Object.prototype.hasOwnProperty.call(result, body[i].userId)) {
          result[body[i].userId] = result[body[i].userId] + 1;
        } else {
          result[body[i].userId] = 1;
        }
      }
    }
    const len = Object.keys(result).length;
    const key = Object.keys(result);
    for (let i = 0; i < len; ++i) {
      if (i === 0) process.stdout.write('{');
      if (i === 0) process.stdout.write(` '${key[i]}': ${result[i + 1]}`);
      else process.stdout.write(`  '${key[i]}': ${result[i + 1]}`);
      if (i + 1 < len) console.log(',');
      else console.log(' }');
    }
  });
}
