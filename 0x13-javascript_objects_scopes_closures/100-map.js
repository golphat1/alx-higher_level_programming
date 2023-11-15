#!/usr/bin/node
/*
 * script that imports an array and computes a new array.
 * script must import list from the file 100-data.js
 * use a map
 * A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
 * Print both the initial list and the new list
 */
const data = require('./100-data');
const list = data.list;

const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
