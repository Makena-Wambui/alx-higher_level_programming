#!/usr/bin/node

/*
 * A version of the Jquery constructor was created which takes a ready function as a parameter.
 * Makes the code even shorter.
 * Our anonymous function is passed directly to the jQuery constructor,
 * which assigns it to the ready event.
 *
 */

$(function()
{
	$('#container').text("Welcome to my website!").removeClass("blue").addClass("bold").css("color", "yellow");
});

/*
 * In the above command chain,
 * We instantiate a new jquery object, and select the container element with the $ character.
 * $ -> a shortcut for the jquery class.
 * So we get a jQuery object,
 * that allows us to manipulate the selected element.
 * We use this object to call the text method.
 * The text method sets the text of the selected elements.
 * Text() returns the jquery object again.
 * Hence we can use another method call directly on the return value. eg css method
 */
