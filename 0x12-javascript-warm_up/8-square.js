#!/usr/bin/node
/*
 * script that prints a square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use a loop (while, for, etc.)
 */

// Use process.argv[2] directly instead of assigning it to a variable
const args = process.argv[2];

// Checks if args is undefined or not a valid number
if (isNaN(args) || args === undefined) {
  console.log('Missing size');
} else {
  // Declares number using 'let' to avoid potential global scope issues
  let number = parseInt(args);

  // Checks if the conversion resulted in a valid number
  if (isNaN(number)) {
    console.log('Invalid size');
  } else {
    // Uses 'let' to declare the loop variables
    for (let i = 0; i < number; i++) {
      let row = '';
      for (let j = 0; j < number; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
