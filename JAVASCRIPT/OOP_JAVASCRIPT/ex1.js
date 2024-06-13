#!/usr/bin/node

// object literals different from objects instantiated
// from classes.

let person = {}; // empty object

console.log(person, typeof person);

// updates
person = {
  // the first two items are data items;
  // they are the objects's properties.
  name: ['Alicia', 'Makena'],
  age: 32,
  // the object's methods.
  // they are functions that allow the object to do something with the
  // data above
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old`);
  },
  introduceSelf: function () {
    console.log(`Hi, I am ${this.name[1]}!`);
  }
};

/* Access the objects properties and methods using Dot
 * Notation.
 * Object's name - namespace.
 */

console.log(person.name);
console.log(person.name[0]);
console.log(person.age);
console.log(person.bio());
console.log(person.introduceSelf());

// a simpler syntax when the object's members are functions
person = {
  name: ['Alicia', 'Makena'],
  age: 32,
  bio () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf () {
    console.log(`Hi I am ${this.name[1]}!`);
  }

};

// an object's property can itself be an object
person = {
  name: {
    first: 'Alicia',
    last: 'Makena'
  },
  age: 32,
  bio () {
    console.log(`${this.name.first} ${this.name.last} is ${this.age} years old.`);
  },
  introduceSelf () {
    console.log(`Hi I am ${this.name.last}!`);
  }
};
const myDataName = 'Height';
const myDataValue = '1.75m';
person[myDataName] = myDataValue;

// to access
console.log(person.name.first);
console.log(person.name.last);
console.log(person.bio());
console.log(person.introduceSelf());

// You can also use bracket notation to access object properties.
console.log(person.name.first);
console.log(person.name.last);
console.log(person.age);

function printProperty (propertyName) {
  console.log(person[propertyName]);
}
printProperty('age');
printProperty('name');

// update member values
person.age = 40;
person.name.last = 'Wambui';

// create new object members
person.eyes = 'Brown';
person.farewell = function () {
  console.log('Bye everyone!');
};
console.log(person.age);
console.log(person.name.last);
console.log(person.farewell());
console.log(person.eyes);
console.log(person.Height);

// create another object person2
// this is a keyword that refers to the current object the code is written inside of.

const person2 = {
  name: {
    first: 'Kurt',
    last: 'Angle'
  },
  introduceSelf () {
    console.log(`Hi I am ${this.name.last}!`);
  }
};
console.log(person.introduceSelf());
console.log(person2.introduceSelf());

// COnstructors
/*
 * OBject literals are okay when you are creating one object.
 * But are inadequate when creating more than one object.
 * You need a way to define the shape of an object.
 * That is, the set of properties and methods it can have.
 * Then use this method to create as many objects as we like.
 * And just update the values for the properties that are different.
 */

function createPerson (name) {
  // creates and returns a new object each time it is called.
  const obje = {};
  // uses the name param to set the value of the name property
  obje.name = name;
  // the value of this method remains the same for all objects created using this function.
  obje.introduceSelf = function () {
    console.log(`Hi, I am ${this.name}`);
  };
  return obje;
}

// Now you can create as many objects as you ike.
const dan = createPerson('Danson');
console.log(dan.name, dan.introduceSelf());

const peter = createPerson('Peter');
console.log(peter.name, peter.introduceSelf());

// a constructor is a function called using the new keyword.
// start with a capital letter
function Person1 (name) {
  this.name = name;
  this.goodbye = function () {
    console.log(`Goodbye! ${this.name}!`);
  };
}

const mark = new Person1('Mark');
console.log(mark.goodbye());

const tim = new Person1('Timothy');
console.log(tim.goodbye());

function Cat (name, breed, color) {
  this.name = name;
  this.breed = breed;
  this.color = color;
  this.greeting = function () {
    console.log(`Hello, said ${this.name} the ${this.breed}`);
  };
}

const pickles = new Cat('Pickles', 'Ragdoll', 'White');
const manuel = new Cat('Manny', 'Sphynx', 'Pink');
console.log(pickles.breed);
console.log(manuel.greeting());
console.log(pickles.greeting());
