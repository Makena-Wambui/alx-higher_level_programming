#!/usr/bin/node

// Represents textual data.
// Each element in the string occupies a position in the string.
// First element => index 0.
// Second element => index 1, etc..
// Length of a string is the number of UTF-16 code units in it.
// May not correspond to the actual number of Unicode characters.
// Are immutable.
// Once created, they can not be modified.
// You can use string methods to create new strings based on the content of the current string.
// substring() to create a substring of the original.
const myString = "Holberton";
console.log(myString.substring(1, 3));

console.log(myString.substring(2));

// Concatenate two strings using concatenation operator -> '+' or concat().

const str = "School";

const newStr = myString + ' ' + str;
console.log(newStr);

const str1 = "Hello";
const str2 = "World";
console.log(str1.concat(' ', str2));
console.log(str2.concat(', ', str1));

// Beware of "stringly-typing" your code!
// May be tempting to use strings to rep complex data.
// 	Short term benefits of this:
// 		Easy to build complex strings with concatenation.
// 		Strings easy to debug - what is printed is what is in the string.
// 		They are also the common denominator of alot of APIs e.g input fields, local storage values so tempting to only work with strings.
// 		It is possible to represent any data structure in a string.
// 		But this is not always a good idea.
// 		Eg with a separator, one can emulate a list;
// 		But an array would be more suitable.
// Creates an unnecessary maintenance burden
const emulate_list = "Apples, bananas, pears, avovadoes";
console.log(typeof emulate_list);

// Array much better
const myArray = [ 'Apples', 'bananas', 'kiwi', 'pineapple' ];
console.log(typeof myArray);

// When representing complex data, parse strings, and use the appropriate abstraction.
