#!/usr/bin/node
const arg = process.argv;
let parsed;
try {
  parsed = parseInt(arg[2]);
  if (isNaN(parsed)) throw new Error('Missing number of occurrences');
  for (let i = 0; i < parsed; i++) console.log('C is fun');
} catch (e) {
  console.log(e.message);
}
