#!/usr/bin/node

/*
 * script that prints message depending of the number of arguments passed
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found”
 */

const numArguments = process.argv.length - 2; // Subtracting 2 to exclude 'node' and the script filename

// Using a switch statement to print the appropriate message
switch (numArguments) {
  case 0:
    console.log("No argument");
    break;
  case 1:
    console.log("Argument found");
    break;
  default:
    console.log("Arguments found");
    break;
}
