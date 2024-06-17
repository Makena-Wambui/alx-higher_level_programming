#!/usr/bin/node

/*
 * Write a script that prints two arguments passed to it, in the following
 * format: “ is ”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 */
// concatenate the argument at cliArgs[2] with 'is' and cliArgs[3]
const cliArgs = process.argv;
console.log(cliArgs[2] + ' is ' + cliArgs[3]);
