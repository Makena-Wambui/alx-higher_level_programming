#!/usr/bin/node

// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence

// Let's import data from 101-data.js
// Then extract dict property is from the imported module and assign to the variable myDict.
const myDict = require('./101-data').dict;

// Initialize an empty object
const myResult = {};

// This line creates an arraY containing all the keys (property names) from the dict object
const myDictKeys = Object.keys(myDict);

// This line creates an array containing all the values (property values) from the dict object
const myDictValues = Object.values(myDict);

let a;

// This loop iterates over the myDictValues array
for (let i = 0; i < myDictValues.length; i++) {
  // For each value, it performs the following steps:
  // Creates an empty array inside myResult with the key as the stringified version of myDictValues
  myResult[JSON.stringify(myDictValues[i])] = [];

  // Filters the keys to find those whose corresponding value matches the current value:
  a = myDictKeys.filter(key => myDict[key] === myDictValues[i]);

  // For each matched key, pushes it into the array associated with the current value
  a.forEach(item => myResult[JSON.stringify(myDictValues[i])].push(item));
}

// myResult object now contains keys (stringified values) and arrays of matching keys.
// Each key in myResult corresponds to a unique value from the original dict
console.log(myResult);
