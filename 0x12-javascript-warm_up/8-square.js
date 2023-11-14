#!/usr/bin/node
/*
 * script that prints a square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use a loop (while, for, etc.)
 */
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	const x = Number(process.argv[2]);
	let v = 0;
	while (v < x) {
		console.log('X'.repeat(x));
		v++;
	}
}
