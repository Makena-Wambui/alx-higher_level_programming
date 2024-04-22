#!/usr/bin/node

/*
 * Write a script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * You have to define a function with this prototype: function add(a, b)
 */

const cliArgs = process.argv;
const first = Number(cliArgs[2]);
const second = Number(cliArgs[3]);
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(first, second);
