#!/usr/bin/node

// We will need to use Rectangle.
const Rectangle = require('./4-rectangle');

// Write a class Square that defines a square and inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // call the superclass constructor using super()
    super(size, size);
  }
}

module.exports = Square;
