#!/usr/bin/node

// var keyword is a different way to declare variables.

// var myName;
// var myAge;

// With var you can declare a variable after you initialize it.
// Works because of hoisting.

mySchool = 'Trove';

function logSchool() {
	console.log(mySchool);
}

logSchool();

var mySchool;


// with var you can declare the same variable as many times as you would like.
var myCity = 'Meru';
var myCity = 'Nairobi';
console.log(myCity);


// with let you can not redeclare variables
let myWeight = '70kg';
// let myWeight = '60kg';
// will only work if you do it like this:
myWeight = '75kg';

console.log(myWeight);
