#!/usr/bin/node

/*
 * Most basic statement is the block statement.
 * A block statement is used to group statements.
 * It is delimited by a pair of curly braces.
 * They are commonly used with control flow statements => if, for, while
 */
// Example:

let x = 2;

while (x < 10) {
	x++;
	console.log(x);
}

// { x++; } is the block statement.


/*
 * var-declared variables are not block-scoped.
 * but are scoped to the containing function or script.
 * The effects of setting them persist beyond the block itself.
 * Example below:
 */

var y = 1;

{
	var y = 5;
}

console.log(y);

/* The above will output 5.
 * This is because the var x statement within the block is in the same scope as the var x statement before the block.
 * This scoping can be mitigated by using const or let.
 */


let z = 10;

{
	let z = 7;
	console.log(z);
}

console.log(z);
