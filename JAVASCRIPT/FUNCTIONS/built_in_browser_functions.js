#!/usr/bin/node

// These are functions built into the browser.
// For ex, when manipulating a text string:

const str = "I am a girl";

// the replace() string function takes a source string and a target string, and replaces the source string with the target string, and returns the newly formed string.
const newStr = str.replace("girl", "boy");
console.log(newStr);


// Array Manipulation
const myArr = ["I", "love", "my", "son."];
// The join() function takes an array,
// joins all the array items together into a single string,
// then return the new string.

const newArr = myArr.join(" ");
console.log(newArr);


// Generating a random number
// The random function generates a random number btwn 0 and up to but not including 1, and returns that number.
const num = Math.random();
console.log(num);

// JS has many built in functions.
// They allow you to do useful things without having to write all the code yourself.
// Some of the code you are calling when you invoke(run, execute) a built in browser function could not be written in JS.
// Many of these functions are calling parts of the background browser code -> written largely in low level system lang like C++,
// and not web languages like JS.
// Some built in browser functions are not part of the core JS Language.
// Some are part of browser APIs -> which build on top of the default language so as to provide more functionality.


// Functions vs Methods.
// methods -> are functions that are part of objects.
//
// Custom functions -> functions defined in our code, not in the browser.
// They have a custom name -> ()
//
// Functions can contain whatever code you like.
// You can call other functions from inside other functions.


// Invoking Functions.
// -------------------
// To actually use a function after it has been defined, you have to run or invoke it.
// To do this, include the name of the function in your code elsewhere, followed by ().

hello(); // calling a function before we define it -> hoisting.

function hello() {
	console.log("Hello!");
}


// Creating a function -> function declaration
// Always hoisted -> you can call the function above the function definition, and it will work fine
//
//
//
// Function parameters
// ------------------------
// Some functions require parameters to be specified when invoked.
// These are values that need to be included in the ().
// The function needs these values/parameters to do its job properly.
//
// Parameters/arguments/attributes.
//
// Example: the browsers built in Math.random() function does not need any parameters.
const m = Math.random();
console.log(m);

// the browser's built in replace() string function needs two parameters -> substring to find in the main string, and the substring that replaces that string.
// When you specify multiple parameters, separate them by commas.
const s = "My name is Megan";
const s1 = s.replace("Megan", "Alice");
console.log(s1);

// Optional parameters.
// Sometimes parameters are optional.
// They dont have to be specified.
// If you dont specify them,
// the function adopts some kind of default behavior.
// For ex: the array join() function parameter is optional
const w = ["I", "have", "a", "crush", "on", "Danson"];

const w1 = w.join(" ");

// if no parameter is included, that specifies a joining or delimiting character, a comma is used by default.
const w2 = w.join();

console.log(w1);
console.log(w2);

// Default parameters
// -------------------
// If you want your function to support optional parameters,
// you can specify default values. -> add = after the parameter's name,
// followed by the default value.
// For ex:
function hi(name = "Jake") {
	console.log(`Hello, ${name}.`);
}

hi();
hi("Danson");
