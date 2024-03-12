#!/usr/bin/node
const ac = process.argv.length;
let max = 0;
let secondMax = 0;
if (ac > 3) {
  for (let i = 2; i < ac; ++i) {
    process.argv[i] = Number(process.argv[i]);
  }
  max = process.argv[2];
  secondmax = process.argv[2];
  if (ac === 4) {
    if (max < process.argv[3]) {
      secondMax = max;
    } else {
      secondMax = process.argv[3];
    }
  } else {
    for (let i = 3; i < ac; ++i) {
      if (process.argv[i] > max) {
        secondMax = max;
        max = process.argv[i];
      }
    }
  }
}
console.log(secondMax);
