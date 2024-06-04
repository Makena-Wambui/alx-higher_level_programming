/*
 * Let us change the heading text from Mozilla is cool to Hello world!
 * We use the function querySelector() to grab a reference to our heading.
 * Then store it in a variable called myHeading.
 * Similar to doing it with CSS Selectors.
 * If you want to do smt to am element,
 * You need to select it first.
 */
const myHeading = document.querySelector("h1");
myHeading.textContent = "Hello World!";
