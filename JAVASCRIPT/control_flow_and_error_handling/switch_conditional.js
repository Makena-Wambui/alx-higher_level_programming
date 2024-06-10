#!/usr/bin/node

/*
 * Allows a program to evaluate an expression,
 * then attempt to match the expression's value to a case label.
 * If a match is found,
 * the program executes the associated statement.
 */

/* example:
 * ---------
 *  switch (expression) {
 *  	case label1:
 *  		statements1;
 *  		break;
 *  	case label2:
 *  		statements2;
 *  		break;
 *
 *  	.
 *  	.
 *  	.
 *  	.
 *  	default:
 *  		statementsDefault;
 *  }
 *
 *  How the above switch statement is evaluated:
 *  ---------------------------------------------
 *  The program first looks for a case clause with a label matching the value of expression.
 *  It then transfers control to that clause, executing the associated statements.
 *
 *  If no match is found:
 *  	Program looks for the optional default clause.
 *  		If a default clause is found, 
 *  		The program transfers control to that clause.
 *  		Associated statements are executed.
 *
 *  		If no default clause is found:
 *  		Program resumes execution at the statement following the end of switch.
 *
 *  		By convention, the default clause is written as the last clause, but it does not need to be so.
 *
 *
 * Break Statements
 * -----------------
 *  Optional
 *  And associated with each case clause.
 *  Ensures that the program breaks out of switch once the matched statement is executed.
 *  And continues execution at the statement following switch.
 *
 *  If omitted,
 *  the program continues execution inside the switch statement.
 */

// Example
let fruitType = "Bananas";
fruitType = "WaterMelon";
fruitType = "Pawpaw";

switch (fruitType) {
	case "Mangoes":
		console.log("Mangoes are 100 shillings per kg.");
		break;

	case "Grapefruit":
		console.log("Grapefruit is 200 shillings per kg.");
		break;

	case "Bananas":
		console.log("Bananas are 30 shillings per kg");
		break;
	case "WaterMelon":
		console.log("Watermelons are 250 shillings per kg.");
		break;
	default:
		console.log(`We are out of ${fruitType}`);
}

console.log("Is there anything else you would like?");
