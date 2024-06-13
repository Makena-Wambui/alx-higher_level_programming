#!/usr/bin/node

// What is an object?
// A collection of related data and/or functionality => Usually consist of several variables and functions => properties, methods 

let Person;
console.log(Person);

Person = {};

console.log(Person); // empty object.

Person = {
	name: ["Bob", "Smith"],
	age: 32,
	bio: function () {
		console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
	},
	introduceSelf: function () {
		console.log(`Hi, I am ${this.name[0]}`);
	},
};

console.log(Person.name);
console.log(Person.name[0]);
console.log(Person.age);
console.log(Person.bio());
console.log(Person.introduceSelf());

// An object is made up of multiple members.
// Each member has a name => name, age.
// and a value eg 32.
// Each name-value pair must be separated by a comma.
// Name and value must be separated by a colon.
// Syntax is as follows:
// 	const objectName = {
// 		member1Name: member1Value,
// 		member2Name: member2Value,
// 		.
// 		.
// 		.
// 		memberNname: memberNvalue,
// 		
// 	};
// Value of an object member can be anything -> number, array, function, etc.
// The first two items => name, age are data items => object properties.
// The last two items, => bio and introduceSelf ae functions.
// They allow the object to do something with that data =>object's methods.
//
//
// Simpler syntax to use when the object's members are functions:
// Instead of bio: function () we say bio() 

const person = {
	name: ["Bob", "Smith"],
	age: 32,
	bio() {
		console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
	},
	introduceSelf() {
		console.log(`Hi I am ${this.name[0]}.`);
	},
};

console.log(person.name);
console.log(person.introduceSelf());

// this kind of object is called an object literal.
// Because we have literally written out the object contents.
// They are different from objects instantiated from classes.
//
// Common to create an object using an object literal when you want to transfer a series of structured related data items in some manner, for ex sending a request to the server to be put into the db.
// Sending a single object more efficient than sending several items individually.
// Also easier to work with than an array -> when you want to identify individual items by name.
//


// DOT NOTATION:
// -------------------
// You can access the object properties and methods using dot notation as shown above.
//
// The object name eg person acts as the namespace.
// Must be entered first to access anything inside the object.
// Next write a dot.
// Then the item you want to access => name of a simple property, an item of an array property, or a call to one of the object's methods.

// Objects as object properties.
// --------------------------------
// For example..
Person = {
	name: {
		firstName: "Mary",
		secondName: "Magdalene",
	},
	age: 40,
	bio() {
		console.log(`${this.name.firstName} ${this.name.secondName} is ${this.age} years old.`);
	},
};
console.log(Person.name.firstName);
console.log(person.bio());
console.log(Person.bio());

// BRACKET NOTATION.
// -------------------
// Provides an alternative way of accessing object properties.
// Instead of Person.age, we say Person["age"].

console.log(Person["age"]);
console.log(Person["name"]["secondName"]);

// Objects are sometimes called associative arrays, in that they map strings to values in the way that arrays map numbers to values.
// However, dot notation preferrd because it is easier to read and more succinct.
//
// There are some cases you have to use bracket notation.
// For ex if an object property name is held in a variable, you can not use dot notation to access the value, but you can use bracket notation.

const student = {
	name: ['Alicia', 'Makena'],
	grade: 17,
};

function logPropertyName(propertyName) {
	console.log(student[propertyName]);
}

logPropertyName("grade");
logPropertyName("name");


// SETTING OBJECT MEMBERS:
// --------------------------
// You can set/update the value of object members by declaring the member you want to set using dot notation or bracket notation. 
student.name[0] = "Brenda";
console.log(student.name[0]);
student["grade"] = 15;
console.log(student["grade"]);
Person["name"]["firstName"] = "Monique";
console.log(Person["name"]["firstName"]);

// You can also create completely new object members.
// for example:
Person["Weight"] = "70 kilograms";
console.log(Person["Weight"]);
Person.Height = "1.80cm";
console.log(Person.Height);
Person.farewell = function () {
	console.log("Bye Everyone");
};
console.log(Person.farewell());
console.log(Person);

// We can also do this:
// --------------------------
// But only with bracket notation.
const myDataItem = "Eyes_Color";
const myDataValue = "Brown";

Person[myDataItem] = myDataValue;
console.log(Person.Eyes_Color);

// Adding a property to an object like this is not possible with dot notation=> it can only accept a literal member name, not a variable.


// What is "this"?
// ----------------
//
// For ex in our introduceSelf() {
// 	console.log(`Hi my name is ${this.name[0]}`);
// }
//
// "this" keyword => the current object the code is written inside eg Person.
// // Why not write Person instead?
// ----------------------------------
// When you only have to create a single object literal, 'this' is not very useful.
// But if you're creating more than one, 'this' allows you to use the same method definition for every object created.


const person1 = {
	name: ["Jake", "Ragira"],
	introduceSelf() {
		console.log(`Hello my name is ${this.name[0]}`);
	},
};

const person2 = {
	name: ["Chris", "Odhiambo"],
	introduceSelf() {
		console.log(`Hello my name is ${this.name[0]}`);
	},
};

console.log(person1.introduceSelf());
console.log(person2.introduceSelf());


// Constructors:
// -------------
// Using object literals is ok when you want to create one object.
// But they are inadequate when you need to create more than one object.
// We have to write out the same code for every object we create.
// And if we want to change some properties of the object, like adding a new height property, we have to update every object.
//
// We can have a way of defining the shape of our object => the set of properties and methods our object will have.
// Then use this to create as many objects as we like.
// And just update the values for the properties that are different.
//
//
// First way to do this is to use a function:
// ------------------------------------------

function createPerson(name) {
	const obj = {};
	obj.name = name;
	obj.introduceSelf = function () {
		console.log(`Hello I am ${this.name}`);
	};
	return obj;
}

// The function above creates a new object and returns that object every time we call it.
// The object has two members => property name, and method introduceSelf().
// createPerson() will take a parameter name, which will be used to set the value of the name property.
// The value of introduceSelf() method is however the same for every object created using this function: a common pattern for creating objects.
//
const person3 = createPerson('Makena');
console.log(person3);
console.log(person3.name);
console.log(person3.introduceSelf());

const person4 = createPerson("Frank");
console.log(person4.name);
console.log(person4.introduceSelf());

// The function works fine but it is a bit long winded -> we have to create an empty object, initialize it, and return it.
// A better way is to use a constructor.
//
// A constructor is a function called using the new keyword.
// When you call a constructor, it will:
// 	1. Create a new object.
// 	2. Bind 'this' to the new object so we can refer to this in our constructor code.
// 	3. Run the constructor code.
// 	4. Return the new object.
//
// Constructors must start with a capital letter
// Named after the type of object it creates.
// We would therefore recreate the above function like this:
//
function MyPerson(name) {
	this.name = name;
	this.introduceSelf = function () {
		console.log(`Hi my name is ${this.name}`);
	};
}

// Now to call Person as a constructor we use the new keyword:
const woman1 = new MyPerson("Monica");
console.log(woman1.name);
console.log(woman1.introduceSelf());
