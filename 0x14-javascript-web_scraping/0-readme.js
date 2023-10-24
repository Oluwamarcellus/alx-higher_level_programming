#!/usr/bin/node

const argv = process.argv.slice(2);
const fs = require('fs');
fs.readFile(argv[0], 'utf-8', (error, data) => {
  if (!error) {
    console.log(data);
  }
});
