#!/usr/bin/node

// Classes are a template for creating objects.
// They encapsulate data with code to work on that data
// In JS, classes are built on prototypes.
// But also have some syntax and semantics unique to classes.


// DEFINING CLASSES
// ----------------
// Classes are "special functions".
// Just as you can define function declarations and function expressions, a class can be defined in two ways: a class expression, a class declaration.
// For example: a class declaration
class Rectangle {
	length;
	width;

	constructor(length, width) {
		this.length = length;
		this.width = width;
	}
}

// a class expression: the class is anonymous, but assigned to a variable
const Rectanglee = class {
	constructor(length, width) {
		this.length = length;
		this.width = width;
	}

};

// another class expression but the class has it's own name
const Rectangle3 = class Rectangle2 {
	constructor(length, width) {
		this.length = length;
		this.width = width;
	}
};

// Like function expressions, class expressions may be anonymous, OR have a name, different from the variable that it is assigned to.
// 
// Unlike function declarations, class declarations have the same temporal dead zone restrictions as let or const thus behave as if they are not hoisted.
//
// CLASS BODY
// -----------
// Body of a class is the part that is in {}.
// It is where you define class members -> properties, methods, constructor
// Body of a class is executed in strict mode, even without the use strict directive.
// A class element can be characterized by three aspects:
// 	Kind: getter, setter, method, field
// 	Location: static or instance
// 	Visibility: private or public
// Together, they add up to 16 possible combinations.
//
//
// METHOD DEFINITIONS
// -----------------------
// This is a shorter syntax for defining a function property in an object initializer.
// Can also be used in classes.
//
// Example:
const obj = {
	foo() {
		return "bar";
	},
};

console.log(obj.foo());

// For example, given the following code,
let obj2 = {
	foo: function () {
		return "foo";
	},

	bar: function () {
		return "bar";
	},

};
// The above can be shortened to:
obj2 = {
	age: 32,
	foo() {
		return "foo";
	},

	bar() {
		return "bar";
	},

	logAge: function age() {
		return this.age;
	},
};

// Properties defined using this syntsax are own properties of the created object,
// They are configurable, writable and enumerable just like normal properties.
// Note that the method syntax is not equivalent to a normal property with a afunction as its value. There are semantic differences.
console.log(obj2.age);
console.log(obj2.logAge());

// Method definitions are not constructable
// Methods can not be constructors.
// Will trow a typeerror if you try to instantiate them.
// But a property created as a function can be used as a constructor.
//	const myObj = new obj2.foo(); -> obj2.foo() is not a constructor.
//
//Only functions defined as methods have access to the super keyword.
// super.prop looks up the property on the prototype of the object that the method was initialized on.
//

const o = {
	__proto__: {
		// prop: "foo",
		prop: "makena",
	},

	notAMethod: function () {
		// console.log(super.prop); -> super keyword unexpected here.
	},

	aMethod() {
		console.log(super.prop);
	},
};

console.log(o.__proto__);


// Examples:
const p = {
	a: "jakey",
	b() {
		return this.a;
	},
};

console.log(p.b());


// Example2: method definitions in classes
// You can use the above syntax to define public instance methods available on class instances.
// No need for comma separator btwn methods in classes.

class ClassWithPublicInstanceMethods {
	publicInstanceMethod() {
		return 'Hello World';
	}

	secondPublicMethod() {
		return "goodbye world.";
	}

}

const instance = new ClassWithPublicInstanceMethods();
console.log(instance.publicInstanceMethod());

console.log(instance.secondPublicMethod());
console.log(ClassWithPublicInstanceMethods.__proto__);
console.log(ClassWithPublicInstanceMethods.prototype);

// Public instance methods are defined on the prototype property of the class.
// Hence, ahared by all instances of the class.
// They are writable, configurable, non-enumerable.
//
// Inside instance methods, this and super work like in normal methods.
// this refers to the instance itself.
// super allows you to call methods from the superclass.
//

class SecondClass extends ClassWithPublicInstanceMethods {

	subclassMethod() {
		return super.publicInstanceMethod();
	}

}

const j = new SecondClass();
console.log(j.subclassMethod());



class BaseClass {
	msg = 'Hello people!';
	baseClassMethod() {
		return this.msg;
	}
}

class SubClass extends BaseClass {

	subclasser() {
		return super.baseClassMethod();
	}
}

const m = new SubClass();
console.log(m.subclasser());


// CONSTRUCTOR
// ---------------
// Constructor method is a special method for creating and initializing an object created with a class.
// Can only be one special method with the name constructor in a class.
// Syntax error is thrown if a class contains more than one occurence of the constructor method.
// Can use the super keyword to call the constructor of the superclass.
// You can create instance properties inside the constructor.

class Rectangle5 {
	constructor(width, height) {
		this.width = width;
		this.height = height;
	}
}

// If your instance properties' values do not depend on the constructor's arguments, you can define them as class fields.
//
//
// static initialization blocks
// -----------------------------:
// These are blocks of code used to initialize static properties of a class.
// They allow flexible initialization of static properties.
// Meaning unlike static field initializers, S.I.B allow for more complex initialization logic including multiple statements and expressions.
// You can write any JavaScript code inside a SIB.
// ie you can perform calculations, make conditional assignments, loop thro data etc during initialization of static properties.
// Access to the private scope: Inside a SIB, you still have access to private properties and methods of the class.
// So you can use or modify these private members while setting up your static properties.
// You can have more than one SIB in your class.
// Static blocks can be mixed with static fields and methods. You can declare a static field, then a static block, then another static field, etc.
// All static fields, methods and blocks are evaluated in the order in which they are declared in the class. ie the sequence in which they appear in the class definition determines their order of execution.
// For example:

class MyClass {
	// the first static field: property1 initialized to 10
	static property1 = 10;

	// the first static block
	static {
		console.log("The first static block.");
		// initializes static field property2 with property1
		this.property2 = this.property1 * 2;
	}

	static property3 = 30;

	static {
		console.log("The second static block.");
		this.property4 = this.property2 + this.property3;
	}

	static {
		console.log("The third static block.");
		this.property5 = this.property4 * 3;
	}

	static getSummary() {
		return `property1: ${this.property1}, property2: ${this.property2}, property3: ${this.property3}, property4: ${this.property4}, property5: ${this.property5}`
	}

}
console.log(MyClass.getSummary());

const a = new MyClass();
console.log(a.property1);
console.log(MyClass.property1);

// METHODS
// -----------
// Methods are defined on the protototype of each class instance,
// Shared by all instances.
// They can be plain functions, async functions, generator functions or async generator functions.
// For example:

class Rectangle10 {
	constructor(width, height) {
		this.width = width;
		this.height = height;
	}

	// this is a getter
	get area() {
		return this.calcArea();
	}
	// Method
	calcArea() {
		return this.width * this.height;
	}

	*getSides() {
		yield this.height;
		yield this.width;
		yield this.height;
		yield this.width;
	}
}

const mySquare = new Rectangle10(10, 10);
console.log(mySquare.area);
console.log(mySquare.calcArea());
const iterObject = mySquare.getSides();
console.log(iterObject.next().value);
console.log(iterObject.next().value);
console.log(iterObject.next().value);
console.log(iterObject.next().value);
// Method definitions allow computed property names
const bar = {
	foo0: function () {
		return 0;
	},

	foo1() {
		return 1;
	},
	["foo" + 2]() {
		return 2;
	},

};

console.log(bar.foo0());
console.log(bar.foo1());
console.log(bar.foo2());

// Generator Methods
// ------------------:
// A generator function is a function that can pause its execution, and resume later.
// The function* syntax is used to declare a generator function.
// The asterisk before g indicates that g is a generator function.
// The yield keyword is used to pause function execution and return a value.
// So in the example below, when yield is encountered, the function's execution is paused, and the value of index is returned.
// index++ increments the value of index after yielding its current value.
//
// The (*) in the generator method syntax must come before the generator property name.
// 	* g() {} and not g*() {}
// For example, using a named property:
const n = {
	g: function* () {
		let index = 0;
		while (true) {
			yield index++;
		}
	},
};

// The same object but using shorthand syntax
const n2 = {
	*g() {
		let index = 0;
		while (true) {
			yield index++;
		}
	},
};
// creating an iterator object from the generator function g.
// Then we call the next() method on the iterator object to resume the execution of the generator function from where it was last paused and get the next value.
// index is initialized to 0.
// yield pauses the execution of the generator function and the current value of index is returned which is 0.
// index++ increments index to 1 after 0 is returned.
// the first i.next().value yields 0. the second call to next() yield 1 and so forth.
//
//
const i = n.g();
console.log(i.next().value);

// Static methods and fields
// static keyword is used to define static methods and fields for a class.
// Static properties: static fields and methods are defined on the class itself, not on each instance.
// Static methods-> create utility functions for an application.
// static fields -> useful for caches, fixed configurations, or any other data that does not need to be replicated across instances
// For ex:

class Point {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}

	static displayName = "Point";

	static distance(a, b) {
		const dx = a.x - b.x;
		const dy = a.y - b.y;
		return Math.hypot(dx, dy);
	}
}

const p1 = new Point(5, 5);
const p2 = new Point(10, 10);

console.log(p1.displayName);
console.log(p2.displayName);
console.log(p1.distance);
console.log(Point.displayName);
console.log(Point.distance(p1, p2));

