#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
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

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const exch = this.width;
    this.width = this.hight;
    this.hight = exch;
  }

}
module.exports = Rectangle;
