#!/usr/bin/node
/*
 * script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
 * script must import dict from the file 101-data.js
 */
const data = require('./101-data');
const dict = data.dict;

const invertedDict = {};

for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const occurrence = dict[key];

    if (!invertedDict[occurrence]) {
      invertedDict[occurrence] = [];
    }

    invertedDict[occurrence].push(key);
  }
}

console.log(invertedDict);
