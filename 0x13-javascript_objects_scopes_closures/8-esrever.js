#!/usr/bin/node

// Write a function that returns the reversed version of a list
// You are not allow to use the built-in method reverse
exports.esrever = function (list) {
  // declare an empty array
  const reversedArray = [];
  let a;
  // use a for loop to iterate backwards from the last index
  for (a = list.length - 1; a >= 0; a--) {
    // use push to append values to the array
    reversedArray.push(list[a]);
  }
  return reversedArray;
};
