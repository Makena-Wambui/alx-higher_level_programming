#!/usr/bin/node

// A value in memory, possibly referenced by an identifier.
// They are the only mutable values.
// Functions are also objects.
// Also callable.

// PROPERTIES
// --------------
// Objects are a collection of properties.
// Using the object literal syntax, a ltd set of properties are initialized.
// Then properties can be added or removed.
// Properties => key-value pairs.
// Keys => Strings or Symbols.
// Values => values of any type including other objects -> enables building complex data structures.

// ---------------------------------------
// TYPES OF OBJECT PROPERTIES
// ------------------------------------
// Two types of object properties:
// 	Data property
// 	Accessor property
//
// 	Each property has corresponding attributes.
// 	Each attribute is accessed internally by the JS Engine,
// 	but you can set them through Object.defineProperty(),
// 	or read them through Object.getOwnPropertyDescriptor().
//
let Person = { 'name': 'Alice', 'age': 30, 'location': 'Meru' };

const age = Object.getOwnPropertyDescriptor(Person, 'age');

console.log(age);

console.log(age.configurable);
console.log(age.value);

Object.defineProperty(Person, 'Profession', { value: 'SE', writable: false, });
console.log(Person.Profession);
console.log(Object.getOwnPropertyDescriptor(Person, 'Profession'));

// DATA PROPERTY
// Associate a key with a value.
// Can be described by the following attributes.
//
// 	value
// 	------
// 		value retrieved by a get access on the property.
// 		Can be any JS Value.
//
// 	writable
// 	--------
// 		A boolean value that indicates whether the property can be changed with an assignment.
//
// 	enumerable
// 	-----------
// 		A boolean value indicating whether the property can be enumerated by a for...in loop.
//
// 	configurable
// 	--------------
// 		A boolean value indicating whether property can be deleted, can be changed to an accessor property, or whether its attributes can be changed.
//
//
let Pet = { 'Favourite Foods': ['Chicken', 'Spaggheti', 'Cat Nip'] };
console.log(Object.getOwnPropertyDescriptor(Pet, 'Favourite Foods'));

// ACCESSOR PROPERTY
// ---------------------
// Key -> with one of two accessor functions, get and set to retrieve or store a value.
//
// Have the following properties:
// 	get
// 	----
// 		A function
// 		Called with an empty argument list.
// 		To retrieve the property value
// 		Whenever a get access on the value is performed.
// 		May be undefined.
//
// 	set
// 	-----
// 		A function.
// 		Called with an argument,
// 		Which contains the assigned value.
// 		Executed whenever specified property is attempted to be changed.
// 		May be undefined.
//
// 	enumerable
// 	-----------
// 		a boolean value
// 		indicates whether a property can be enumerated using a for .... in loop.
//
// 	configurable
// 	------------
// 		a boolean value
// 		indicates whether a property can be deleted,
// 		can be changed to a data property
// 		or its attributes changed.
//
// The prototype of an object points to another object or to null.
// It is a hidden property of the object.
// Represented as [[Prototype]]
// Properties of the object's [[Prototype]] can be accessed on the object itself.
//
// Objects are ad-hoc key-value pairs.
// Often used as Maps
// But due to ergonomics, security and performance issues, Use a Map to store arbitrary data instead.
//
const myMap = new Map();
myMap.set('a', 1);
myMap.set('b', 2);
myMap.set('c', 3);

console.log(myMap);
console.log(myMap.get('a'));

myMap.set('a', 98);
console.log(myMap.get('a'));

console.log(myMap.size);

myMap.delete('c');
console.log(myMap.size);

// Use the built in Date utility when representing dates
const myDate = new Date(2011, 10, 10);
console.log(myDate);


// Indexed Collections: Arrays and typed arrays.
// Arrays=> regular objects, there is a particular relationship between integer keyed properties and the length property.
// Inherit from Array.prototype -> provides a handful of convenient methods for array manipulation.

// indexOf() returns the first index at which a given element can be found in the array,
// or -1 if the element can not be found in the array.

const myAnimals = ['yak', 'lion', 'panther', 'giraffe', 'gorilla', 'lion'];
console.log(myAnimals.indexOf('lion'));

// starting from index 2
console.log(myAnimals.indexOf('lion', 2));

// No such element
console.log(myAnimals.indexOf('cheetah'));

// push() adds the specified elements to the end of the array ,
// and returns the new length of the array.

const newLength = myAnimals.push('gazelle');
console.log(newLength);
console.log(myAnimals);


myAnimals.push('duck', 'geese', 'chickens');
console.log(myAnimals);
// Arrays are perfect for representing ordered lists.
// Typed arrays - array like object for manipulating binary data.
//
//

// Keyed collections: Maps, Sets, WeakMaps, WeakSets
// A map is a collection of key value pairs
// Any type of value (objects, primitive values) can be used as keys or values.
// The order in which the keys are added is preserved.
// Example:

let map = new Map();
map.set('gender', 'female');
console.log(map.get('gender'));
map.set('marital_status', 'single');
console.log(map);

// Sets:
// A collection of unique values.
// No duplicates are allowed.
// Store values of any type.
// Mantain the order of elements as they are inserted.
// Example:
let set = new Set();
set.add(1);
set.add('teacher');
console.log(set);


// WeakMaps
// Similar to a map
// Only allows objects as keys
// Does not prevent garbage collection of those objects.
// If there are no other references to a key object, it can be garbage collected.
// This helps with memory mgt.
// Example:

let weakmap = new WeakMap();
let weakmap2 = new WeakMap();

const obj1 = {};
const obj2 = function () {};
weakmap.set(obj1, 'ten');
weakmap.set(obj2, 'myFunc');
weakmap.set(weakmap2, 'weakmap as a key');

console.log(weakmap.get(obj1));
console.log(weakmap.get(weakmap2));

console.log(weakmap.has(obj2));
weakmap.delete(obj2);
console.log(weakmap.has(obj2));


// WeakSets
// Like a set.
// Only allows objects as values.
// Does not prevent garbage collection of these objects.
// Do not store duplicate values.
// Do not mantain the order of elements.

let weakset = new WeakSet();
weakset.add(obj2);
console.log(weakset);

// Structured data: JSON
// JavaScript Object Notation.
// a Lightweight data interchange format derived from JavaScript.
// Used by many programming languages.
// Builds universal data structures.
// That can be transferred btwn different environments, and even across languages.
//
// JS has a standard library of built in objects,refer to it
