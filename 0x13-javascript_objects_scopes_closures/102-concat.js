#!/usr/bin/node
/*
 * script that concats 2 files.
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */
const fs = require('fs');
const args = process.argv.slice(2);

if (args.length !== 3) {
  console.error('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = args[0];
const file2Path = args[1];
const destinationPath = args[2];

const file1Content = fs.readFileSync(file1Path, 'utf8');
const file2Content = fs.readFileSync(file2Path, 'utf8');

const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(destinationPath, concatenatedContent, 'utf8');
