#!/usr/bin/node
const ac = process.argv.length;
if (ac >= 3) {
  let num = Number(process.argv[2]);
  if (String(num) !== 'NaN') {
    num = parseInt(num);
    if (num <= 1) {
      console.log(NaN);
    } else {
      console.log(factorial(num));
    }
  } else {
    console.log(NaN);
  }
} else {
  console.log(NaN);
}

/**
 * computes the factorial of a number.
 * @param {number} n
 * @return {number} the factorial of n.
 */
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
