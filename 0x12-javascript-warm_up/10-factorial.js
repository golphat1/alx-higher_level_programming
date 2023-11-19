#!/usr/bin/node

/*
 * script that computes and prints a factorial
 * The first argument is integer (argument can be cast as integer) used for computing the factorial
 * Factorial of NaN is 1
 * You must do it recursively
 * You must use a function
 */
const computeFactorial = (n) => {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
};

const inputArgument = process.argv[2];

const n = parseInt(inputArgument);

console.log(computeFactorial(n));
