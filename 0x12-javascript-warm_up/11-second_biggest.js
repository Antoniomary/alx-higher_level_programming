#!/usr/bin/node
process.argv = process.argv.slice(2);
const ac = process.argv.length;
let secondMax = 0;
if (ac > 1) {
  process.argv = process.argv.map(Number);
  process.argv.sort();
  secondMax = process.argv[ac - 2];
}
console.log(secondMax);
