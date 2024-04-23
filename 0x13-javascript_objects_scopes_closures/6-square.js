#!/usr/bin/node

// Write a class Square that defines a square and inherits from Square of 5-square.js

const Square1 = require('./5-square');

class Square extends Square1 {
  // Create an instance method called charPrint(c) that prints the rectangle using the character c
  // If c is undefined, use the character X
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let a, b;
    for (a = 0; a < this.height; a++) {
      let row = '';
      for (b = 0; b < this.width; b++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
