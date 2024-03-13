#!/usr/bin/node
const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      if (this.width && this.height) {
        let block = c;
        for (let w = 1; w < this.width; ++w) {
          block += c;
        }
        for (let h = 0; h < this.height; ++h) {
          console.log(block);
        }
      }
    }
  }
}

module.exports = Square;
