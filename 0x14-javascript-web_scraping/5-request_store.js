#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);

request.get(args[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(args[1], body, function (err, res) {
      if (err) console.log('error', err);
    });
  }
});
