#!/usr/bin/node
const list = require('./100-data').list;
// print the original list
console.log(list);
// A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
const newList = list.map((x, i) => x * i);

// print new list
console.log(newList);
