#!/usr/bin/node
const PreviousSquare = require('./5-square'); // Rename imported class

class Square extends PreviousSquare {
  charPrint(c) {
    const char = c || 'X'; // Use 'X' if c is undefined
    if (this.width === undefined || this.height === undefined) {
      console.log('');
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;

