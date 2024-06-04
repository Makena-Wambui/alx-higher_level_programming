#!/usr/bin/node

// 
// Js is a weakly typed language.
// Means that you can use a value of one type, where another type is expected,and JS will convert it to the right type for you
//
// Coercion Rules:
// ----------------
// Primitive Coercion
// --------------------:
// This process is used where a primitive value is expected,
// but there is no strong preference for what the actual type should be.
// A string, a Number, a BigInt are equally acceptable.
// Example:
//
// Date(): when it receives one argument that is not a Date instance:
// 	strings -> date strings
// 	numbers -> timestamps

// Passing a Date Instance:
const newDate = new Date(2020, 5, 4); // June 4h 2020
console.log(newDate);

// Passing A Date String
// Pass a date string in a format recognizable by the Date Constructor.
// Most common formats include ISO 8601 date strings, and other variations.

const dateString = "2020-06-03T21:00:00.000Z";
const myDate = new Date(dateString);
console.log(myDate);

// Receiving a single number argument rep the number of miliseconds since January 1, 1970, 00:00:00 UTC.
// or multiple number arguments rep year, month, day, etc.
//Example: Single number representing the time stamp.
const timeStamp = 1727913600000; // corresponds to Oct 3, 2024
const date = new Date(timeStamp);
console.log(date);

// Multiple numbers rep year, month, day, hour, minutesecond, milisecond
const year = 2024;
const month = 05; // Months are 0 indexed so this will be June.
const day = 11;
const hour = 22;
const minute = 36;
const second = 56;

const d = new Date(year, month, day, hour, minute, second);
console.log(d);


// the + operator
// if one operand is a string, string concatenation is performed.
// Otherwise numeric addition is performed.

let result = '5' + 50;
console.log(result);

result = 5 + 50;
console.log(result);

// == operator
// If one operand is a primitive while the other is an object, the object is converted to a primitive value with no preferred type.
// Example:
let n;
const obj = {};

console.log(n == obj);

// primitive coercion does not do any conversion if the value is already a primitive.
// objects are converted to primitives by calling its [@@toPrimitive](),valueOf() and toString() methods in that order.
// Primitive conversion calls valueOf() before toString(), which is similar to the behavior of number coercion, but different from string coercion.
//
// [@@toPrimitive]() if present must return a primitive.
// If it returns an object, a TypeError is thrown.
// For valueOf() & toString(), if one returns an object, the return value is ignored, and the other's return value is used instead.
// If neither is present;
// Or neither returns a primitive,
// a TypeError is thrown.
//
// Example:
console.log({} + []); // [object object]
//
//
// {} and [] both do not have a [@@toPrimitive]() method.
// Both inherit valueOf() from Object.prototype.valueOf, which returns the object itself.
// This value is ignored.
//
// toString is called instead.
// {}.toString() returns "[object Object]"
// [].toString() returns ""
// So their result is their concatenation: "[object Object]"
//
//
//
// the [@@toPrimitive]() method always takes precedence when doing conversion to any primitive type.
// Primitive conversion behaves like number conversion, since valueOf() is called in priority.
// objects with custom [@@toPrimitive]() can choose to return any primitive.
// Date and symbol objects are the only built in objects that override the [@@toPrimitive]() method
// Date.prototype[@@toPrimitive]() treats the 'default' hint as if it's "string".
// Symbol.prototype[@@toPrimitive]() ignores the default hint and always returns a symbol.
//
//
//
//
// Numeric coercion
// -------------------
// 2 numeric types -> Number, BigInt.
// Sometimes specificaly a number or a BigInt is expected.eg Array.prototype.slice(), where the index must be a number.
// Example:
const myArr = [1, 4, 'Alice', 10, 'twenty'];
console.log(myArr.slice(2));

// other times it may tolerate either, and perform different operations depending on the operand's type.
// But there are strict coercion processes that do not allow implicit conversion from the other type.
//
// Numeric coercion almost the same as number coercion.
// Except BigInts returned as-is, instead of causing a TypeError.
//
// Numeric coercion is used by all arithmetic operators.. since they are overloaded for both numbers and BigInts.
// Except unary plus which always does number coercion.


// OTHER COERCIONS
// ----------------
// All data types except Null, undefined and Symbol have their respective coercion process.
// => string coercion, boolean coercion, object coercion.
//
// There are three distinct paths thro which objects may be converted to primitives:
// 	1. Primitive Coercion -> [@@toPrimitive]("default") -> valueOf() -> toString()
//
// 	2. Numeric Coercion, Number Coercion, BigInt Coercion -> [@@toPrimitive]("number") -> valueOf() -> toString()
// 	3. String Coercion -> [@@toPrimitive]("string") -> toString() -> valueOf()
//
// 	In all cases, [@@toPrimitive]() if present must be callable, and return a primitive.
// 	valueOf() or toString() will be ignored if not callable or return an object.
//
// 	At the end of the process, if successful, result is guaranteed to be a primitive.
// 	Resulting primitive is then subject to further coercions dep on the context.
//
