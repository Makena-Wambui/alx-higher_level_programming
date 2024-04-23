#!/usr/bin/node

exports.converter = function (base) {
  // the converter function takes a single argument, base
  // this following function is a  closure defined using a return statement.
  // it takes an argument number.
  return function (number) {
    // this closure converts number to a string using the specified base.
    return number.toString(base);
  };
};
