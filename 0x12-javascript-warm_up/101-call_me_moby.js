#!/usr/bin/node
/*
 * Write a function that executes x times a function.
 *
 * The function must be visible from outside
 * Prototype: function (x, theFunction)
 * You are not allowed to use var
 */

exports.callMeMoby = function (x, theFunction) {
  // executes theFUnction x times
  for (let i = 1; i <= x; i++) {
    theFunction();
  }
};
