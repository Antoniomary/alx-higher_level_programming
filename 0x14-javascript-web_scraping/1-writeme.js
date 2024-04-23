#!/usr/bin/node

const fs = require('fs');
const ac = process.argv.length;
if (ac === 4) {
  fs.writeFileSync(process.argv[2], process.argv[3], 'utf-8');
}
