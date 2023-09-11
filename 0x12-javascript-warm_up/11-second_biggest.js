#!/usr/bin/node
let argv = process.argv;
let secBig = 0;
let biggest = 0;

if (argv.length - 2 <= 1) secBig = 0;
else {
  argv = argv.slice(2, argv.length);
  argv.forEach((arg) => {
    if (parseInt(arg) > biggest) {
      secBig = biggest;
      biggest = parseInt(arg);
    }
  });
}

console.log(secBig);
