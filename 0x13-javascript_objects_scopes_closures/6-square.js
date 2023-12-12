#!/usr/bin/node

const supSquare = require('./5-square.js');
class Square extends supSquare {
  charPrint (c) {
    if (c == null) {
      c = 'X';
    }
    for (let j = 0; j < this.width; j++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
