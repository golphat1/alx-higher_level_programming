#!/usr/bin/node

/*
 * script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 * You can use only two console.log
 * You must use a loop (while, for, etc.)
 */
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing number of occurrences');
} else {
	const x = Number(process.argv[2]);
	let v = 0;
	while (v < x) {
		console.log('C is fun');
		v++;
	}
}
