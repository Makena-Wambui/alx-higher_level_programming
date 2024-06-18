#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // If w or h is equal to 0 or not a positive integer, create an empty object
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  // Create an instance method called print() that prints the rectangle using the character X
  print () {
    let a, b;
    for (a = 0; a < this.height; a++) {
      // initialize an empty string for each row
      let row = '';
      for (b = 0; b < this.width; b++) {
        // add 'X' for each column
        row += 'X';
      }
      // print row
      console.log(row);
    }
  }
}

module.exports = Rectangle;
