#!/usr/bin/node
const argList = process.argv;
if (!argList[2]) {
  console.log('No argument');
} else {
  argList.forEach((arg, index) => {
    if (index > 1) console.log(arg);
  });
}
