#!/usr/bin/node
const argList = process.argv;
if (argList.length - 2 === 0) {
  console.log('No argument');
} else {
  argList.forEach((arg, index) => {
    if (index > 1) console.log(arg);
  });
}
