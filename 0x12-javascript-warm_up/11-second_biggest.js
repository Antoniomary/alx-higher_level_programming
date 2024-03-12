#!/usr/bin/node
process.argv = process.argv.slice(2);
let ac = process.argv.length;
let max = 0;
let secondMax = 0;
if (ac > 1) {
  for (let i = 0; i < ac;) {
    process.argv[i] = Number(process.argv[i]);
    if (String(process.argv[i]) === 'NaN') {
      process.argv[i] = process.argv[ac - 1];
      ac -= 1;
    } else {
      ++i;
    }
  }
  max = process.argv[0];                                                secondMax = max;
  for (let i = 0; i < ac; ++i) {
    if (String(secondMax) === 'NaN') {                                      secondMax = process.argv[i];
    }                                                                     if (process.argv[i] > max) {
      secondMax = max;
      max = process.argv[i];
    } else if (process.argv[i] < max) {
      secondMax = process.argv[i];
    }
  }
  if (ac <= 1) {
    secondMax = NaN;
  }
}
console.log(secondMax);
