#!/usr/bin/node
let len = 0;
let output = 'No argument';
for (const arg of process.argv) {
  len++;
  if (len === 3) {
    output = arg;
    break;
  }
}

console.log(output);
