#!/usr/bin/node
const numOfArg = process.argv.length;
if (numOfArg === 2) {
  console.log('No argument');
} else if (numOfArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
