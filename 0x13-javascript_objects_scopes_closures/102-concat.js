#!/usr/bin/node
const av = process.argv.slice(2);
const ac = av.length;
if (ac === 3) {
  const fs = require('fs');
  try {
    const contentA = fs.readFileSync(av[0], 'utf8').trim();
    const contentB = fs.readFileSync(av[1], 'utf8').trim();
    fs.writeFileSync(av[2], contentA + '\n');
    fs.appendFileSync(av[2], contentB + '\n');
  } catch (err) {
    console.log('An Error occured');
  }
}
