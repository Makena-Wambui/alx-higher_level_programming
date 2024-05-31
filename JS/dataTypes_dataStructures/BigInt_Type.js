#!/usr/bin/node

// A numeric primitive in JS
// Can represent integers with arbitrary magnitude.
// You can safely store and operate on large integers even beyond Number.MAX_SAFE_INTEGER for numbers.
// A BigInt is created by appending n to an integer's end
// Or by calling the BigInt() function.

console.log(Number.MAX_SAFE_INTEGER);

const n = BigInt(Number.MAX_SAFE_INTEGER);
console.log(n);
console.log(n + 1n);
console.log(n + 2n);

console.log(n + 1n === n + 2n);

console.log(Number.MAX_SAFE_INTEGER + 1);
console.log(Number.MAX_SAFE_INTEGER + 2);
console.log(Number.MAX_SAFE_INTEGER + 3);
console.log(Number.MAX_SAFE_INTEGER + 4);

console.log(Number.MAX_SAFE_INTEGER + 1 === Number.MAX_SAFE_INTEGER + 2);

// You can use most operators to work with BigInt except >>> -> unsigned right shift.
// A BigInt is not strictly equal to a Number of the same mathematical value, but loosely so.
// BigInt values are nether always more precise nor always less precise than numbers.
// BigInts can not rep fractional numbers.
// But can rep large integers more accurately.
// They are not mutually substitutable.
// A typeError exception is thrown if BigInts are mixed with reg numbers in arithmetic expressions,
// or if implicitly converted to each other.
