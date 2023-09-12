#!/usr/bin/node
const SquareP = require('./5-square');
class Square extends SquareP {
  charPrint (chr = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(chr);
      }
      console.log();
    }
  }
}
module.exports = Square;
