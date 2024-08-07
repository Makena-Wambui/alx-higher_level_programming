#!/usr/bin/node

/*
 * Write a JavaScript script that updates the text color of the <header> element to red ( #FF0000 )
 * use document.querySelector to select the HTML tag
 * do not use the JQuery API
 */

const myHeader = document.querySelector('header');

/*
 * use the setAttribute method to set the style attribute with the desired color.
 */

myHeader.setAttribute('style', 'color: red');
