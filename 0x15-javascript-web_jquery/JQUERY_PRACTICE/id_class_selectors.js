#!/usr/bin/node

/*
 * Select elements based on their id attributes.
 * id is unique so only use this when you wish to select a single unique element.
 */

$(function()
{
	/* you can match all links on a page like ths.*/
	/* $("a")
	 *
	 * Or all div tags like this:
	 * $("div")
	 */
	$("#test").text("Testing");
	/*$("li.bold", "p.bold").css("font-weight", 900);*/
	$("li.bold").css("font-weight", "bolder");
	$("p.bold").css("font-weight", "bolder");
});
