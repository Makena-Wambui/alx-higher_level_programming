/* add event handlers to our code to ensure real interactivity
 * of our website.
 *
 * We select the html element.
 * Then call its addEventListener() function.
 * Then we pass the event to listen to.
 * And the function to run in case that event occurs.
 *
 * function () is an anonymous function because it does not have a name.
 * Another way to write anonymous functions is the arrow function.
 * 	() => instead of function ()
 */

document.querySelector("html").addEventListener("click", () => {
	alert("Stop poking me!");
});
