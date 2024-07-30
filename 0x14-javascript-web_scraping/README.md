Notes on JSON
-------------
JSON is purely a string with a specified data format.
	Contains only properties, no methods

Double quotes must be used around strings and property names.
	Single quotes invalid except when surrounding the entire JSON string.

A single misplaced comma or colon can cause JSON not to work.
Validate any data you are attempting to use.
You can validate JSON using an application like JSONLint

JSON can actually take the form of any data type that is valid for inclusion inside JSON,
not just arrays or objects. So for example, a single string or number would be valid JSON.

Unlike in JavaScript code in which object properties may be unquoted, in JSON only quoted strings may be used as properties.

parse(): Accepts a JSON string as a parameter, and returns the corresponding JavaScript object.
stringify(): Accepts an object as a parameter, and returns the equivalent JSON string.


Working with fs and request:
==============================
