#!/usr/bin/node
// This function calculates the factorial of a number n

function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
	  return 1;
  } else {
	  const result = n * factorial(n - 1);
	  return result;
  }
}

const args = process.argv;
const myVar = Number(args[2]);
console.log(factorial(myVar));
