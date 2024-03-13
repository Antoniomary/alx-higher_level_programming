#!/usr/bin/node
const av = process.argv.slice(2);
const ac = av.length;
if (ac >= 3) {
  const fs = require('fs');
  if (fs.existsSync(av[0]) &&
      fs.statSync(av[0]).isFile &&
      fs.existsSync(av[1]) &&
      fs.statSync(av[1]).isFile) {
    const contentA = fs.readFileSync(av[0], 'utf8');
    const contentB = fs.readFileSync(av[1], 'utf8');
    const stream = fs.createWriteStream(av[2]);
    stream.write(contentA);
    stream.write(contentB);
    stream.end()
  }
}
