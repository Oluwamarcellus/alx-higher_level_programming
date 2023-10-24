#!/usr/bin/node

const argv = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(argv[0], argv[1], 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
