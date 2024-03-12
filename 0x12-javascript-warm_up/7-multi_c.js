#!/usr/bin/node
const ac = process.argv.length;
let output = 'Missing number of occurrences';
if (ac >= 3) {
  if (String(Number(process.argv[2])) !== 'NaN') {
    const n = parseInt(Number(process.argv[2]));
    output = 'C is fun';
    for (let i = 0; i < n; ++i) {
      console.log(output);
    }
  }
} else {
  console.log(output);
}
