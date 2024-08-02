#!/usr/bin/node
let count = 0; // Initialize a counter variable

function logMe(item) {
  console.log(`${count}: ${item}`);
  count++; // Increment the counter
}

exports.logMe = logMe;

