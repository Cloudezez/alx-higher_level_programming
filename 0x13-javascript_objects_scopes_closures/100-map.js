#!/usr/bin/node
const { list } = require('./100-data');

// Compute the new list with each value multiplied by its index
const newList = list.map((value, index) => value * index);

// Print the original list
console.log(list);

// Print the new list
console.log(newList);

