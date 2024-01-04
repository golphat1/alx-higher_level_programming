#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node script.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the content of the file in utf-8
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    // Print the error object if an error occurs during reading
    console.error(error);
  } else {
    // Print the file's content
    console.log(data);
  }
});
