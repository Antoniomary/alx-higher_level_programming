#!/usr/bin/node

const fs = require('fs');
const ac = process.argv.length;
if (ac === 3)
{
	try {
		console.log(fs.readFileSync(process.argv[2], 'utf-8'));
	} catch (e) {
		console.log(`{ Error: ${e.message}`);
		console.log('    at Error (native)');
		console.log(`  errno: ${e.errno},`);
		console.log(`  code: '${e.code}',`);
		console.log(`  syscall: '${e.syscall}',`);
		console.log(`  path: '${e.path}' }`);
	}
}
