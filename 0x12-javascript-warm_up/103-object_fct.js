#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
 * Most typically, this is used in object methods, where this refers to the
 * object that the method is attached to, thus allowing the same method to
 * be reused on different objects.
 * When a regular function is invoked as a method of an object (obj.method()), this points to that object.
*/
myObject.incr = function () {
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
