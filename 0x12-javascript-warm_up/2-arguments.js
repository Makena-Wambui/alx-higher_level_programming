#!/usr/bin/node
/*
 * Write a script that prints a message depending of the number of argument
 * passed.
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found"
 * Otherwise, print “Arguments found”
 */

// process.argv returns an array
// use that array and the length property and conditionals
// the first item in that array is path to interpreter
// second item - path to file
// other items - CLI args.

const cliArgs = process.argv;
if (cliArgs.length === 2) {
  console.log('No argument');
} else if (cliArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
