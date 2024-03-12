#!/usr/bin/node

/**
 * adds 2 integers.
 * @param {first number} a
 * @param {second number} b
 * @return {number}
 */
function add (a, b) {
  return a + b;
}

const ac = process.argv.length;
let firstArg = NaN;
let secondArg = NaN;
if (ac === 4) {
  firstArg = Number(process.argv[2]);
  secondArg = Number(process.argv[3]);
}
console.log(add(firstArg, secondArg));
