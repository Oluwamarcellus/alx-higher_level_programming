#!/usr/bin/node

const argv = process.argv.slice(2);
const request = require('request');
request.get(argv[0]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
