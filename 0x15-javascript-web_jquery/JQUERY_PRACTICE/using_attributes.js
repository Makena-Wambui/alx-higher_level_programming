#!/usr/bin/node

// We acn find elements on a page using their class or id.
// With jquery, you can find elements based on any attribute.
//
// Find all elements with a specific attribute:
// In this example, we do not require the attribute to have a specific value.
// Infact, the attribute does not have to have a value.
// use a set of [] wih the name of the desired attribute inside it. eg [name] or [href]

$(function()
{
	$("[title]").css("text-decoration", "underline");
});

// To find elements with a specific value for a specific attribute:

/*
 * The selector simply tells jQuery to find all links (the a elements)
 * which has a target attribute that equals the string value "_blank"
 * and then append the text "[new window]" to them.
 */
$(function()
{
	$("a[target=_blank]").append(" [new window]");
});
