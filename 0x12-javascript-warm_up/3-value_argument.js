#!/usr/bin/node
/*
 * Write a script that prints the first argument passed to it.
 * If no arguments are passed to the script, print “No argument”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You are not allowed to use length
 */

// process.argv returns an array
// use that array and the bracket notation to access arguments
// passed to the script.
// the first item in that array is path to interpreter
// second item - path to file
// other items - CLI args.

const cliArgs = process.argv;
if (cliArgs[2] === undefined) {
  console.log('No argument');
} else {
  console.log(cliArgs[2]);
}
