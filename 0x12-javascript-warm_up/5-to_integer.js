#!/usr/bin/node
/*
 * Write a script that prints My number: <int>
 * if the first argument can be converted to an integer.
 * If the argument can’t be converted to an integer, print “Not a number”
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You are not allowed to use try/catch
 */

// Use the isNaN function
// Returns true if value to be tested is NOt A NUmber.
// Otherwise false
const cliArgs = process.argv;
if (cliArgs[2] === undefined || isNaN(cliArgs[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(cliArgs[2]));
}
