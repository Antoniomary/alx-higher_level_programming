#!/usr/bin/node
const len = process.argv.length;
let output = 'Not a number';

if (len >= 3) {
  output = Number(process.argv[2]);
  if (String(output) === 'NaN') {
    output = 'Not a number';
  } else {
    output = 'My number: ' + parseInt(output);
  }
}

console.log(output);
