

It is a small, fast, feature rich Javascript library.

It makes thimgs like event handling, animation, Ajax and HTML document traversal and manipulation much easier.

Has an easy to use API that works across a multitude of browsers.

Highly extensible and versatile.

Method chaining
----------------
Most of jQuery methods return a jquery object, which you can use to call another method.
This allows you to do command chaining.
	where you can perform multiple methods on the same set of elements
	Saves you and the browser from having to find the same elements more than once.
	for ex: $('#container').text("Welcome to my website!").css("color", "red");
	
Some methods do not return the jquery object
Others return it depending on the parameters you pass to them

For ex text().
	if no parameters are passed to it,
	the current text of the selected elements is returned.
	If a single parameter is passed to it,
	jquery will set the specified text,
	and return a jquery object.

	

DOM MANIPULATION
----------------
One of the most important aspects of JavaScript and thereby jQuery, is manipulation of the DOM

DOM stands for Document Object Model:
a mechanism for representing and interacting with your HTML, XHTML or XML documents.

It allows you to navigate and manipulate your documents through a programming language, which in the browser will almost always be JavaScript.
DOM navigation and manipulation using standard JavaScript can be pretty cumbersome.
However, jQuery comes with a bunch of DOM related methods, making it all much easier.

How to differentiate between text, value and html for various elements.
------------------------------------------------------------------------
Text:
	the textual(no HTML) representation of the inner content of all regular HTML elements such as <div>, <p>, <span>
	contains no HTML tags or attributes.

	ex:
	<div id="exampleText">Hello <b>World</b>!</div>
	Text => Hello World!
Values: for form elements.
	value of form elements like <input>, <textarea>, <select>
	<input type="text" id="exampleValue" value="UserInput">

HTML:
	The inner content along with any HTML tags and attributes inside an element.
	The full markup inside an element
	<div id="exampleHtml">Hello <b>World</b>!</div>
	HTML is Hello <b>World</b>!

