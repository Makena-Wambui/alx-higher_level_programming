#!/usr/bin/node

// primitive values.
// All types except Object define immutable values rep directly at the lowest level of the language.
// All values of these types are known as primitive values.
// All primitive types except null can be tested by the typeof operator
// typeof null => object
// so use === null to test for null.
// All primitive types except null and undefined, have their corresponding object wrapper types,
// which provide useful methods for working with primitive values.
// eg the Number object provides the toExponential() method, etc.
const num = 50;
console.log(num.toExponential());

// When a property is accessed on a primitive value,
// Js automatically wraps the value into the corresponding wrapper object,
// and accesses the property on the object instaed.
// Accessing a property on null or undefined, will throw a type error exception
//
// Null type => null
// Undefined type => undefined.
//
// Undefined => absence of a value.
// Null => absence of an object

console.log(typeof name);

// a return statement with no value returns undefined;
function printSum(num1, num2) {
	const sum = num1 + num2;
	return;
}

// console.log(printSum());
//
// Accessing a non existent object property returns undefined.
console.log(num.extend)

// a variable declaration without initialization initializes the variable to undefined.
let x;
console.log(x);


// null is used much less often.
// most importantly the end of the prototype chain.
// methods that interact with prototypes, like Object.getPrototypeOf(), Object.create() accept/return null instead of undefined.
// null => keyword.
// undefined is a normal identifier that happens to be a global property.
//
//
// Boolean type:
// 		represents a logical entity.
// 		inhabited by two values - true, false
// 		used in conditional operations -> if....else, while, ternary operators.

// Number type:
// 	capable of storing positive floating point numbers from 2 ** -1074 (Number.MIN_VALUE),
// 	To 2 ** 1024 (Number.MAX_VALUE ) -> Infinity.
// 	and negative floating point numbers from -2 ** 1074 to -2 ** 1024.
//
// 	But can only safely store integers in the range -(2 ** 53 - 1) => Number.MIN_SAFE_INTEGER to (2 ** 53 - 1) => Number.MAX_SAFE_INTEGER.
// 	Out of this range, JS can no longer safely represent integers.
// 	Instead they will be represented by a double precision floating point approximation.
// 	Use Number.isSafeInteger() to check if a number is within the range of safe integers.
console.log(Number.isSafeInteger(num));


console.log(Number.MAX_VALUE);

// Numbers outside this range are automatically converted +/-(2 ** -1074, 2 ** 1024)
// Positive values greater than Number.MAX_VALUE are converted to +Infinity
// Positive values smaller than Number.MIN_VALUE are converted to +0
console.log(Number.MIN_VALUE);

// Negative values smaller than -Number.MAX_VALUE are converted to -Infinity
// Negative values greater than -Number.MIN_VALUE are converted to -0.
//
console.log(Number.POSITIVE_INFINITY, Number.NEGATIVE_INFINITY);

// Number type has only one value with multiple representation: 0 => -0, +0
// 0 is an alias for +0
// Almost no difference btwn the two representations.
console.log(+0 === -0);

console.log(42 / +0);
console.log(42 / -0);

// NaN => Not a Number.
// Special kind of number value.
// When the result of an arithmetic operation can not be expressed as a number.
// Only value in Js that is not equal to itself
console.log(NaN === NaN);

