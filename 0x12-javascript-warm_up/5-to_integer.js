#!/usr/bin/node

/*
 * script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 * If the argument can’t be converted to an integer, print “Not a number”
 */
if (process.argv.length < 3) {
  console.log("Not a number");
} else {
  const inputArgument = process.argv[2];

  const integerValue = parseInt(inputArgument);

  if (!isNaN(integerValue)) {
    console.log("My number:", integerValue);
  } else {
    console.log("Not a number");
  }
}
