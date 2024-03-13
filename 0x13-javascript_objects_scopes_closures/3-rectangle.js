#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      let block = 'X';
      for (let w = 1; w < this.width; ++w) {
        block += 'X';
      }
      for (let h = 0; h < this.height; ++h) {
        console.log(block);
      }
    }
  }
}

module.exports = Rectangle;
