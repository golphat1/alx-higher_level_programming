#!/usr/bin/node
/*
 * script that searches the second biggest integer in the list of arguments.
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */
function findSecondLargest (arr) {
  if (arr.length <= 1) {
    return 0;
  }

  const largest = Math.max(...arr);
  let secondLargest = Math.min(...arr);

  for (const num of arr) {
    if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }

  return secondLargest;
}

const args = process.argv.slice(2).map(arg => parseInt(arg, 10));
const secondLargest = findSecondLargest(args);

console.log(secondLargest);
