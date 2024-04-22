#!/usr/bin/node

/*
 * Write a script that searches the second biggest integer in the list of arguments.
 * You can assume all arguments can be converted to integers.
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */

const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  // use slice to remove the node and filename
  const myArgs = args.slice(2);
  // sort in descending order
  const sorted = myArgs.sort(function (a, b) { return b - a; });
  const secondBiggest = sorted[1];
  console.log(secondBiggest);
}
