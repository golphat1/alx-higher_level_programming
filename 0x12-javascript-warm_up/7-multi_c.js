#!/usr/bin/node
/*
 * script that prints x times “C is fun”
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
 * You can use only two console.log
 * You must use a loop (while, for, etc.)
 */
const args = process.argv[2];
if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  let x = parseInt(args);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
