#!/usr/bin/node

// CLASSES AND CONSTRUCTORS
// -------------------------
// Declare a class using the class keyword.
// eg a class declaration for our Person:

class Person {
        name = "";

        constructor(name) {
                this.name = name;
        }

        introduceSelf() {
                console.log(`Hello I am ${this.name}.`);
        }
}

// So we are declaring a class Person with:
//      name property
//      a constructor -> takes a name parameter used to initialize the new object's name property.
//      introduceSelf() method. Can refer to the object's properties using this.
//
//      name; declaration is optional.Could be omitted.
//      The line this.name = name in the constructor will create the name property then initialize it.
//      However it is good practice to list properties explicitly in the class declaration to make it easier to see the properties.
//      You can also initialize the property to a default value when you declare it ie name = "";
//
//      We define the constructor using the constructor keyword.
//      Just like a constructor outside a class definition, it will:
//              create a new object.
//              bind this to the new object so we can refer to this in our drfinition
//              run the code in the constructor.
//              return the new object.
//
//      Given the class declaration above, we can:
//              we can create and use a new Person instance:
const myPerson = new Person("Stefanie");
console.log(myPerson.name)

const myPerson2 = new Person();
console.log(myPerson2.name);
                                                             
myPerson2.introduceSelf();
// Note we call the constructor using the name of the class Person.
//
//
// We can also omit constructors.
// If we do not need to do any special initialization, constructor can be omitted.
// A default constructor will be generated for you.

class Animal {
	sleep() {
		console.log("Hey I am sleepy!");
	}
}

const levine = new Animal();
levine.sleep();

// Let us define a Professor subclass.
class Professor extends Person {
	teaches;

	constructor(name, teaches) {
		super(name);
		this.teaches = teaches;
	}
	introduceSelf() {
		console.log(`Hi I am Professor ${this.name} and i will be your ${this.teaches} teacher.`);
	}
	grade(paper) {
		const grade = Math.floor(Math.random() * (5 - 1) + 1);
		console.log(grade);
	}
}

// Use the extends keyword to show inheritance ie class Professor inherits from class Person.
// Then we declare a new property teaches.
//
// We want to set the teaches property when a new Professor is created.
// So we define a constructor.
// Takes name and teaches as arguments.
// The first thing it does,is call the superclass constructor using super().
// We pass super the name parameter.
// Superclass constructor sets the name property.
// Then after the Professor constructor sets the teaches property
//
// If a subclass has any of its own initializations to do, 
// it must first call the superclass constructor using super().
// And we must pass any parameters the superclass constructor expects.
//
// Also overeriden introduceSelf() method from superclass Person.
// Also added a new method grade() -> assigns random grades to papers,
// Let us now create and use Professors.

const walsh = new Professor("Walsh", "Statistics");
console.log(walsh.name)
console.log(walsh.teaches);
walsh.introduceSelf();
walsh.grade("Probability");


// Encapsulation
// --------------
// We can make the year property of the Student class private.
class Student extends Person {
	#year;

	constructor(name, year) {
		super(name);
		this.#year = year;
	}

	introduceSelf() {
		console.log(`Hello I am ${this.name} and I am in year ${this.#year}`);
	}

	canStudyArchery() {
		return this.#year > 2;
	}
}
// #year -> a private data property
// Student objects can use year internally, but if code outside the object tries to access #year, error is thrown.
const student = new Student("Timothy", 3);
console.log(student.name);
console.log(student.year);
// console.log(student.#year);
console.log(student.canStudyArchery());
student.introduceSelf();
// private data properties must be declared in the class declaration.
// They must start with #.


// PRIVATE METHODS
// ----------------
// Private methods + private data properties.
// Their names start with #.
// They can only be called by the object's own methods.
// For ex:

class Example {
	somePublicMethod() {
		this.#somePrivateMethod();

	}


	#somePrivateMethod() {
		console.log("You called me?");
	}
}

const a = new Example();
a.somePublicMethod();
// console.log(a.#somePrivateMethod());
//
//
class Shape {

  name;
  sides;
  sideLength;

  constructor(name, sides, sideLength) {
    this.name = name;
    this.sides = sides;
    this.sideLength = sideLength;
  }
  calcPerimeter() {
     const perimeter = this.sides * this.sideLength;
     return perimeter;
  }
}
const square = new Shape("square", 4, 5);
console.log(square.calcPerimeter());


const triangle = new Shape("triangle", 3, 3); 
console.log(triangle.calcPerimeter());   

class Square extends Shape {
	calcArea() {
		const area = this.sideLength * this.sideLength;
		return area;
	}

	constructor(sideLength) {
		super("square", 4, sideLength);
		
	}
}

const square2 = new Square(10);
console.log(square2.calcArea());
console.log(square2.name);
console.log(square2.sides);


const square3 = new Square(6);
console.log(square3.calcArea());
console.log(square3.calcPerimeter());
console.log(square3.name);
console.log(square3.sides);
