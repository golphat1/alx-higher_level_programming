#!/usr/bin/node
/*
 * script that prints a square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use a loop (while, for, etc.)
 */
const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing size');
} else {
  number = parseInt(args);
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
