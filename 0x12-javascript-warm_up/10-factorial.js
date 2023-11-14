#!/usr/bin/node

/*
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 */
function factorial (n) {
	if (n < 0) {
		return (-1);
	}
	if (n === 0 || isNaN(n)) {
		return (1);
	}
	return (n * factorial (n - 1));
}

console.log(factorial(Number(process.argv[2])));
