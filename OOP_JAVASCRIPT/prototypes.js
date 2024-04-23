#!/usr/bin/node
// prototypes are the mechanism by which JS Objects inherit features from one another.
// Every object in JS has a built in property - its property.
// prototype itself is an object, so the prototype has its own prototype.
// CReates a prototype chain, which ends when we reach a prototype that has null for its own prototype.
// object literal
// Standard way to access an object's prototype is: object.getPrototypeOf().// All browsers use proto.
const myObject = {
  city: 'Madrid',
  greeting () {
    console.log(`Hello from ${this.city}`);
  }
};
console.log(myObject.greeting());

// the prototype of myObject
console.log(Object.getPrototypeOf(myObject));

// create a Date object
// then walks up the prototype chain
// logging the prototypes.

const myDate = new Date();
let obj = myDate;
do {
  obj = Object.getPrototypeOf(obj);
  console.log(obj);
} while (obj);


// Shadowing properties
// define a property in an object, when you have a property in that object's prototype that has the same name.

const date = new Date(24, 02, 18);
console.log(date.getYear());

date.getYear = function () {
	console.log('Testing...');
};

console.log(date.getYear());

//setting a prototype
// Object.create()
// it creates a new object allows you to specify what object will be that objects's prototype.
const myObject2 = {
	farewell () {
		console.log('Goodbye.');
	}
};
console.log(myObject2.farewell());

const k = Object.create(myObject2);
console.log(k.farewell());

// setting prototypes using constructors
/*
 * All functions have a property called prototype.
 * When you call a function as a constructor,
 * the newly created objects will have this property as their 
 * prototype.
 */

const dog = {
	bark () {
          console.log(`${this.breed} can bark`);
		}
};
// cOnstructor function
function BreedName(name) {
	this.breed = name;
};

Object.assign(BreedName.prototype, dog);
const chi = new BreedName('Chihuahua');
console.log(chi.bark());
console.log(Object.getPrototypeOf(chi));

// own properties
// properties that are defined directly in the objects are called own properties.
// check using the static method: Object.hasOwn()
const t = new BreedName('Terrier');
console.log(Object.hasOwnProperty(t, 'breed'));
console.log(Object.hasOwnProperty(t, 'bark'));
