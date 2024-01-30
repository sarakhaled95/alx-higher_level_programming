#!/usr/bin/node
// a script that display the status code of a GET request.
const request = require('request');
const process = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/';
const episodeNum = process.argv[2];

request(url + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const jsonObj = JSON.parse(body);
    console.log(jsonObj.title);
  }
});
