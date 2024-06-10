#!/usr/bin/node

/*
 * A set of commands that execute when a specified condition is true.
 *
 * if .... else
 * switch
 */

/* if ... else
 * ------------------
 *
 *  Use the if statement to execute a statement if a logical condition is true.
 *
 *  Use optional else clause to execute a statement if the condition is false.
 *
 *  if (condition) {
 *  	statement1;
 *  } else {
 *  	statement2;
 *  }
 *
 * condition => any expression that evaluates to true or false.
 *
 * if condition evaluates to true, statement1 is executed.
 * Otherwise, statement2 is executed.
 *
 * statement1 and statement2 can be any statement, including further nested if statements.
 *
 * You can also use else...if to have multiple conditions tested in sequence.
 *
 * if (condition1) {
 * 	statement1;
 * } else if (condition2) {
 * 	statement2;
 * } else if (conditionN) {
 * 	statementN;
 * } else {
 * 	statementLast;
 * }
 *
 * Where there are multiple conditions like above, only the first logical condition that evaluates to true will be executed.
 *
 * If you want to execute multiple statements, then group them within a block statement.
 *
 * Generally it is good practice to use block statements, esp when nesting if statements.
 *
 * Generally, it is not good practice to have an if .. else with an assignment like x = y as a condition:
 * 	if (x = y) {
 * 		statement1;
 * 	}
 *
 *
 *
 * -----------------------------------------------
 *  FALSY VALUES
 *  These values evaluate to false.
 *
 *  	1. false
 *  	2. null
 *  	3. undefined
 *  	4. NaN
 *  	5. 0
 *  	6. ""
 *
 * All other values, including all objects, evaluate to true when passed to a conditional statement.
 *
 */

// check for false
const value = false;

if (!value) {
	console.log('Evaluates to true: value is falsy');
} else {
	console.log('value is truthy');
}

// check for 0

const v = 0;

if (v) {
	console.log('Evaluated to false so statement 2 should run');
} else {
	console.log('Statement 2 running.');
}

if (!v) {
	console.log('Negation negates false to true so statement 2 does not run.');
} else {
	console.log('Statement 2 running');
}

// Check an empty string
const empty = "";

if (empty) {
	console.log("Statement 2 should run.");
} else {
	console.log("Statement 2 running.");
}

if (!empty) {
	console.log("Statement 1 running");
} else {
	console.log("Staement 2 running.");
}


// Check for Null
const n = null;
console.log(typeof n);

if (!n) {
	console.log("Statement 1 running");
}

// Check for undefined.
let myNum;

if (myNum) {
	console.log("Statement 1 did not run");
} else {
	console.log("Statement 2 running.");
	console.log("myNum is undefined hence a falsy.");
}


// Check for NaN
const nan = Number('Makena');
console.log(nan);

if (nan) {
	console.log("Statement 1 running");
} else {
	console.log("Statement2 running");
	console.log("nan is NaN hence evaluates to false");
}


if (!nan) {
	console.log("nan is a Falsey.");
}

// Combining multiple falsy values
const arr = [false, "Makena", 0, "", 10, NaN, null, undefined];
arr.forEach((value, index) => {
	if (!value) {
		console.log(`Value at index ${index} is a falsy.`);
	} else {
		console.log(`Value at index ${index} is a truthy.`);
	}
});

// Falsy values with the logical OR Operator.
const a = 0;
const b = 9;

const r = a || b;
console.log(r); // outputs 9 because 0 is a falsey.


// Do not confuse the primitive boolean values -> true and false, with the true and false values of the Boolean object.

const f = new Boolean(false);
console.log(f);
console.log(typeof f);
if (f) {
	console.log("Statement 1 running");
}

if (f == true) {
	console.log("Statement 1 running");
} else {
	console.log("Statement 2 running");
}

// Function checkData returns true if the number of characters in a Text Object is 3
// Else, it displays an alert and returns false
function checkData() {
	if (document.form1.threeChar.value.length === 3) {
		return true;
	} else {
		alert(`Enter exactly three characters.
			Invalid ${document.form1.threeChar.value}`);
		return false;
	}
}

