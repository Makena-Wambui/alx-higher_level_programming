#!/usr/bin/node

/*
 * Use throw to throw an exception.
 * Use a throw statement to specify the value to be thrown.
 */

// throw expression;

/*
 * You can throw any expression.
 * The expression does not need to be of any specific type.
 * Here, we are throwing several exceptions of varying types.
 */

// throw "Error!"; // string type.
// throw 89; // Number type
// throw true; // Boolean type.

//throw {
	// Exception being thrown here is an object.
	
	// the toString() method of the object can be useful for producing a meaningful error message.
	//
	// toString() {
		// return "Throwing an object!";
	// },
// };

try {
  throw {
    toString() {
      return "I'm an object!";
    },
  };
} catch (error) {
  console.log(error.toString());  // Outputs: "I'm an object!"
}

// without toString()
// If we had not defined the toString() method, the default toString() method inherited from Object,
// would be used, which does not provide a meaningful error message.
try {
	throw {};
} catch (error) {
	console.log(error.toString()); // [object Object]
}
