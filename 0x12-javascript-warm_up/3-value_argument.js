#!/usr/bin/node

/*
 * script that prints the first argument passed to it:
 * If no arguments are passed to the script, print “No argument”
 */
if (process.argv[2] !== undefined) {
	console.log(process.argv[2]);
} else {
	console.log("No argument");
}
