#!/usr/bin/node

/*
 * Comment this code out to create an anonymous function instead that
 * is immediately passed th the ready method as a reference..
 * function DocumentReady()
                        {
                                $("#container").text("Hello World!");
                        }

                        /*
                                Then use the ready method..
                                to assign our function to the ready event.
                                This tells jquery that as soon as our document is ready,
                                to call our function.
                       */
$(document).ready(function()
	{
		$('#container').text("Hello and Welcome!");
	});
