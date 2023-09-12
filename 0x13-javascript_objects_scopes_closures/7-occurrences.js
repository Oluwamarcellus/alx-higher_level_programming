#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach((ele) => {
    if (ele === searchElement) num++;
  });
  return (num);
};
