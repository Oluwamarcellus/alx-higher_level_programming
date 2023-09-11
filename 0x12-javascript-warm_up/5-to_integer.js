#!/usr/bin/node
const firstArg = process.argv[2];
const parsed = parseInt(firstArg);
if (isNaN(parsed) === true) {
  console.log('Not a number');
} else {
  console.log('My number:', parsed);
}
