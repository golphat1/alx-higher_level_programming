#!/usr/bin/node

/*
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 */
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
	console.log('Not a number');
} else {
	console.log('My number: ', parseInt(process.argv[2]));
}
