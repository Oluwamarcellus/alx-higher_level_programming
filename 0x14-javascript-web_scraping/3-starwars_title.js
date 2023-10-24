#!/usr/bin/node
const argv = process.argv.slice(2);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[0];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
