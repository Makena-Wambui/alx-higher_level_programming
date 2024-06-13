#!/usr/bin/node

// You can create a function that does not have a name.
// In the code below, we are creating an Immediately Invoked Function Expression. => IIFE
// This is a function that is defined and executed immediately after its creation.
// The function needs to be invoked immediately after its definition.
// The anonymous function is defined within parentheses.
// Follow it immediately with another set of parentheses for invocation.
(function () {
	console.log("Hello!");
})();

// Anonymous functions are often seen when a function expects to receive another function as a parameter.
// Hence the function parameter will be an anonymous function.

// The above method/form of creating a function is called Function Expression.
// Function Expressions are not hoisted.
// For example:
// Let us say you want to run some code when the user types into a text box.
// Call the addEventListener() of the text box.
// This function expects at least two parameters.
// In this case => name of the event to listen for -> keydown
// 		=> a function to run when the event happens.
// So when the user presses a key, the browser will call the function provided.
// And will pass it a parameter, containing information about this event, including the key the user pressed.
// That is:
function logKey(event) {
	console.log(`You pressed "${event.key}"`);
}

// textBox.addEventListener('keydown', logKey);

// But instead of defining a separate logKey() function, we can pass addEventListener() an anonymous function.
// textBox.addEventListener('keydown', function (event) {
	// console.log(`You pressed '${event.key}'`);
// })


// If you pass an anonymous function like this, there is an alternative form you can use called an arrow function.
// Instead of function (event), we would use (event) =>.
// That is:
// textBox.addEventListener("keydown", (event) => {
	// console.log(`You pressed this key: ${event.key}`);
// });

// If the function only takes one parameter, you can omit the parentheses around the parameter.
// So now it will be like this:
// textBox.addEventListener("keydown", event => {
	// console.log(`You pressed this key: ${event.key}`);
// });

// If the arrow function contains only one line that is a return statement,
// You can omit the braces, and the return keyword,
// AND return the expression.
// For example in the following code, we will use the map() method of Array to double each element in the original array.


// lets include an anonymous function that doubles each element in an array.
function (value) {
 	return value * 2;
}
const originalArray = [1, 2, 3];

const newDoubledArray = originalArray.map(value => value * 2);

console.log(newDoubledArray);

// The map method above takes takes each item in the array in turn.
// And passes it into the given function.
// Then takes the value returned by the function, adding it to the new array.
// Hence value => value * 2 is the arrow function equivalent of function (value) .....
// We can use the same concise syntax to rewrite our addEventListener()
// That is:
textBox.addEventListener("keydown", event =>
	console.log(`You pressed this key: ${event.key}`),
);

// Arrow functions make your code shorter and more readable.

