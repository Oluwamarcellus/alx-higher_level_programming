#!/usr/bin/node

const argv = process.argv.slice(2);
const request = require('request');
request(argv[0], (error, res, body) => {
  console.log(res.statusCode);
});
