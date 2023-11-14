#!/usr/bin/node

/*
 * script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 */
function add (a, b) {
	const sum = a + b;

	console.log(sum);
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

add(arg1, arg2);
