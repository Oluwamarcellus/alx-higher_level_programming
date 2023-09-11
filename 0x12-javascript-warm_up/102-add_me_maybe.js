#!/usr/bin/node
exports.addMeMaybe = function (x, func) {
  x++;
  func(x);
};
