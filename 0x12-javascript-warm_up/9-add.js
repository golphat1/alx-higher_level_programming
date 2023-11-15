#!/usr/bin/node
/*
 * script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 */

// Use process.argv[index] directly instead of assigning to variables
const firstArg = process.argv[2];
const secondArg = process.argv[3];

function add(a, b) {
  // Checks if either argument is not provided or is not a number
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    // Use parseInt with a radix to ensure correct parsing
    const number1 = parseInt(a, 10);
    const number2 = parseInt(b, 10);

    // Checks if the parsed values are valid integers
    if (!isNaN(number1) && !isNaN(number2)) {
      const addition = number1 + number2;
      console.log(addition);
    } else {
      console.log('Invalid integers');
    }
  }
}

// Call the function with the command line arguments
add(firstArg, secondArg);
