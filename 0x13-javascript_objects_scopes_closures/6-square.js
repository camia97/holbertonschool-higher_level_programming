#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let line = '';
      for (let i = 0; i < this.width; i++) {
        line += 'C';
      }
      for (let j = 0; j < this.height; j++) {
        console.log(line);
      }
    }
  }
}
module.exports = Square;
