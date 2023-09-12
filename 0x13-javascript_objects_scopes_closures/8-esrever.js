#!/usr/bin/node
exports.esrever = function (list) {
  let listEnd = list.length - 1;
  for (let listStart = 0; listStart < listEnd; listStart++, listEnd--) {
    [list[listStart], list[listEnd]] = [list[listEnd], list[listStart]];
  }
  return (list);
};
