#!/usr/bin/node

// this function will print the number of that argument passed to the logMe function followed by the argument itsef.
// let us declare a variable number initialized to 0 to represent the first argument

let number = 0;
exports.logMe = function (item) {
  console.log(number + ': ' + item);
  // increment number for next argument.
  number++;
};
