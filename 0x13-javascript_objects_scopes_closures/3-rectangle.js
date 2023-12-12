#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }
  print () {
    let i = 0;
    while (i < this.width) {
      console.log('X'.repeat(this.height));
      i++;
    }
  }
}
module.exports = Rectangle;
