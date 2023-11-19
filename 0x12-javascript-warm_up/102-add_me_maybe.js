#!/usr/bin/node
/*
 * a function that increments and calls a function.
 * The function must be visible from outside
 * Prototype: function (number, theFunction)
 */
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}

module.exports = {
  addMeMaybe
};
