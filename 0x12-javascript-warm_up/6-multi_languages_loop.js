#!/usr/bin/node

/*
 * script that prints 3 lines: but by using an array of string and a loop
 * The first line: “C is fun”
 * The second line: “Python is cool”
 * The third line: “JavaScript is amazing”
 */
const languages = ["C is fun", "Python is cool", "JavaScript is amazing"];

for (let i = 0; i < languages.length; i++) {
    console.log(languages[i]);
}
