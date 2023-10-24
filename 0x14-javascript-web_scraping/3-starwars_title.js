#!/usr/bin/node

const argv = process.argv.slice(2);
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[0]}`;
request(url, function (err, res, body) {
  console.log(error || JSON.parse(body).title);
});
