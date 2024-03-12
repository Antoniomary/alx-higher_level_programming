#!/usr/bin/node
const ac = process.argv.length;
let output = 'Missing size';
if (ac >= 3) {
  if (String(Number(process.argv[2])) !== 'NaN') {
    const n = parseInt(Number(process.argv[2]));
    if (n > 0) {
      output = 'X';
      for (let i = 1; i < n; ++i) {
        output += 'X';
      }
      for (let i = 0; i < n; ++i) {
        console.log(output);
      }
    }
  } else {
    console.log(output);
  }
} else {
  console.log(output);
}
