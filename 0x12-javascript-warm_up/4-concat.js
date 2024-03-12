#!/usr/bin/node
const len = process.argv.length;
let firstArg = 'undefined';
let secondArg = 'undefined';
if (len >= 3) {
  firstArg = process.argv[2];
}
if (len >= 4) {
  secondArg = process.argv[3];
}
console.log(firstArg + ' is ' + secondArg);
