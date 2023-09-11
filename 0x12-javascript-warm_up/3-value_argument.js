#!/usr/bin/node
const argList = process.argv;
if (argList[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argList[2]);
}
