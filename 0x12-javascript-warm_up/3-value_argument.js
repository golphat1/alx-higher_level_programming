#!/usr/bin/node
/*
 * script that prints the first argument passed to it:
 * If no arguments are passed to the script, print “No argument”
 */
const args = process.argv[2];
if (!args) {
  console.log('No argument');
} else {
  console.log(args);
}
