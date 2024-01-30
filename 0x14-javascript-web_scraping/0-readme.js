#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');
const process = require('process');

const args = process.argv.slice(2);

fs.readFile(args[0], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
