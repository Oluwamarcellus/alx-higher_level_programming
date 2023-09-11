#!/usr/bin/node
const arg = process.argv[2];
const parsed = parseInt(arg);
if (isNaN(parsed)) {
  console.log('Missing size');
} else {
  let strn = '';
  for (let i = 0; i < parsed; i++) {
    if (i > 0) strn += '\n';
    for (let j = 0; j < parsed; j++) {
      strn += 'X';
    }
  }
  console.log(strn);
}
