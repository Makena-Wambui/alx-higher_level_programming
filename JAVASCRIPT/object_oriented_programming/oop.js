#!/usr/bin/node

// A programming paradigm fundamental to many programming languages such as Java and C++.
// Basic concepts -> 1. classes and instances 2. encapsulation. 3. inheritance.
//
// The features described here are of a particular style of OOP -> Class based or classical OOP.
//
// OOP is about modelling a system as a collection of objects.
// With each object representing an aspect of the system.
// Objects contain both methods and data.
// An object provides a public interface to other code that wants to use it.
// But mantains its own internal private state.
// Other parts of the system dont have to care about what is going on inside the object.
//
// CLASSES AND INSTANCES.
// ---------------------------
// When modelling a problem in terms of objects in OOP, we create abstract definitions that represent the types of objects we want to have in our system
//
// For example:
// If modelling a school, we might have objects representing professors.
//
// Each professor has some properties in common: all have a name, and a subject they teach.
// They also can do certain things -> all grade a paper, introduce themselves to the students at the start of each year.
// Hence Professor could be a class in our system.
// The definition of the class will contain the data and the methods every professor has.
//
// in pseudocode, this looks like this:
class Professor
	properties
		name
		teaches
	methods
		grade(paper)
		introduceSelf()

// We have defined a Professor class with:
// two data properties-> name, teaches
// two methods -> grade() to grade a paper, introduceSelf() for introducing themselves.
//
// A class is a kind of template for creating concrete objects of that type.
// Each concrete Professor we create is called an instance of the Professor class.
// The process of creating an instance is done by a special function called a constructor.
// Values are passed to the constructor for any internal state we want to initiliaze in the new instance.
// The constructor is written as part of the class definition.
// Usually has the same name as the class itself.

class Professor
	properties
		name
		teaches
	constructor
		Professor(name, teaches)
	methods
		grade(paper)
		introduceSelf()

// The constructor here takes two parameters -> name and teaches.
// So we can initialize the name and teaches properies when we create a new Professor.
//
// We use the keyword new to signal a constructor is being called.
walsh = new Professor("Walsh", "Statistics");
cecilia = new Professor("Cecilia", "Mathematics");

walsh.name // Walsh
walsh.teaches // Statistics
walsh.introduceSelf() // "My name is Professor Walsh and I will be teaching you Statistics."
cecilia.introduceSelf() // "My name is Professor Cecilia and I will be teaching you Mathematics."
// So we have created two objects.
// Both are instances of the Professor class..
//


// INHERITANCE
// -------------
// We might want to represent students in our School.
// However students do not grade papers, do not teach any particular subject, but they do belong to a particular year.
// They also do have a name, may also introduce themselves: a student class definition may look like this ->

class Student
	properties
		name
		year
	constructor
		Student(name, year)
	methods
		introduceSelf()

// Students and professors do share some properties.
// Or you could say on some level, they are the same kind of thing.
// Inheritance allows us to do this.
//

// Students and professors are both people.
// People have names and want to introduce themselves.
// We model this by defining a class Person -> here we define all the common properties of people.
// Professor and Student can then derive from Person, adding their extra properties.

class Person
	properties
		name
	constructor
		Person(name)
	methods
		introduceSelf()

class Professor : extends Person
	properties
		teaches
	constructor
		Professor(name, teaches)
	methods
		grade(paper)
		introduceSelf()

class Student : extends Person
	properties
		year
	constructor
		Student(name, year)
	methods
		introduceSelf()

// Person is the superclass or parent class of both Professor and Student.
// Professor and Student are subclasses or child classes of Person.
// Notice that introduceSelf() is defined in all three classes.
// While all people introduce themselves, they do it in a different manner.
walsh = new Professor("Walsh", "Statistics");
walsh.introduceSelf(); // Hi, I am professor Walsh, and I will be your Statistics teacher this year.

tilly = new Student("Tillie", "year 4");
tilly.introduceSelf(); // Hi I am Tillie and I am in year 4

// We also could have a default implementation of introduceSelf() for people who are not students or professors.
lydia = new Person("Lydia");
lydia.introduceSelf(); // Hi I am Lydia.

// So when a method has the same name as seen above but a different implementation in different classes is called POLYMORPHISM.
// When a method in a subclass replaces the superclass's implementation -> the subclass overrides the version in the superclass.


// ENCAPSULATION
// ---------------
// Objects provide an interface to other code that wants to use them,
// But mantain their own private internal state.
// Meaning thatinternal state can only be accessed by the object's own methods.
// and not from other objects.
//
// Keeping an objects internal state private, and making a clear division between the object's public interface and its own private internal state -> encapsulation.
// This is useful -> allows the programmer to change the internal implementation of the object, without having to find and update all the code that uses it.
// Creates a kind of firewall btwn this object and the rest of the system


// For ex:
// Suppose students are allowed to study archery if they are in year two or above.
// One way to implement this is by exposing the student's year property and other code could examine that to determine whether the student can take the archery class.


student = new Student("Tom", "year 4");
if (student.year > 1) {
	// allow student to take archery class
}

// The problem with this is that if we decide to change the criteria for allowing students to study archery, for ex the student needs to have parent's permission, we will then have to update every place in our system that performs this test.
// Would be better instead to have a canStudyArchery() method on Student objects, that implements the logic in one place.

class Student : extends Person
	properties
		year
	constructor
		Student(name, year)
	methods
		introduceSelf()
		canStudyArchery() {
			return this.year > 1;
		}

if (student.canStudyArchery()) {
	// allow into archery class
}
// So if we want to change rules about studying archery, we only need to update the Student class, and all code using it will still work.
//
// We can prevent other code from accessing an object's internal state by marking some properties as private.
// This generates an error if code outside the object tries to access these properties

class Student : extends Person
	properties
		private year
	constructor
		Student(name, year)
	methods
		introduceSelf()
		canStudyArchery() {
			return this.year > 1;
		}
student2 = Student("Jackson", "year 3");
student2.year // error: year is a private property of Student


// OOP AND JAVASCRIPT
// ------------------
// Core JS features such as constructors and prototypes, have some relation to some of the basic OOP Concepts discussed above.
//
// Constructors -> provide us with something like a class definition.
// They enable us to define the shape of an object, including any methods it contains in one place.
// But prototypes can be used here too. eg if a method is defined on a constructor's prototype property,
// all objects created using that constructor will have that method via their prototype, and we do not need to define it in the constructor.
//
//
// The prototype chain -> seems like a natural way to implement inheritance. eg a Student object whose prototype is Person, then it can inherit name, and override introduceSelf().
//
//
// But there are also differences btwn these features and and the class based OOP Concepts
//
// 	In class based OOP, classes and objects are 2 separate constructs.
// 	Objects are created as instances of classes.
//
// 	There is also a distinction btwn the feature used to define a class ie the class syntax and the feature used to instantiate an object ie the constructor.
//
// 	In JS, you can create objects without a separate class definition using a function or an object literal.
// 	This makes working with objects more lightweight than it is with class based OOP.
//
// 	And although a prototype chain looks like an inheritance hierarchy and may behave like it, it is different in some ways.
// 	When a subclass is instantiated, a single object is created.
// 	It combines properties defined in the subclass with properties defined further up the hierarchy.
// 	With prototyping, each level of the hierarchy is represented by a separate object, and are linked togetehr via the _proto_ property
// The prototype chain's behavior is less like inheritance and more like delegation.
// What is delegation? -> a programming pattern where an object when asked to perform a task, can perform the task itself,
// or ask another object(it's delegate), to perform the task on its behalf.
// Delegation is a more flexible way of combining objects than inheritance -> for ex it is possible to change or completely replace the delegate at run time.
//



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
// 	name property
// 	a constructor -> takes a name parameter used to initialize the new object's name property.
// 	introduceSelf() method. Can refer to the object's properties using this.
//
// 	name; declaration is optional.Could be omitted.
// 	The line this.name = name in the constructor will create the name property then initialize it.
// 	However it is good practice to list properties explicitly in the class declaration to make it easier to see the properties.
// 	You can also initialize the property to a default value when you declare it ie name = "";
//
// 	We define the constructor using the constructor keyword.
// 	Just like a constructor outside a class definition, it will:
// 		create a new object.
// 		bind this to the new object so we can refer to this in our drfinition
// 		run the code in the constructor.
// 		return the new object.
//
// 	Given the class declaration above, we can:
// 		we can create and use a new Person instance:
const myPerson = new Person("Stefanie");
console.log(myPerson.name)

const myPerson2 = new Person();
console.log(myPerson2.name);
