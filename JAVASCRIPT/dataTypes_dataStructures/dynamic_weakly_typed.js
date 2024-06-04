#!/usr/bin/node
// JS is a dynamic language.
// It has dynamic types.
// And is dynamically typed.
// Variables are not directly associated with values of a particular type.
// Variables can be assigned and reassigned values of any type.

let foo = 20; // foo is a number
foo = "School"; // foo is now a string
foo = false; // foo is now a boolean.
console.log(typeof foo);

// it is also a weakly typed language.
// this means instead of throwing type errors, JS allows implicit type conversion,
// when an operation involves mismatched types

const boo = 30; // boo is a number
const result = boo + '1';
// boo will be coerced to a string so it can be concatenated with the other operand.
console.log(result);
