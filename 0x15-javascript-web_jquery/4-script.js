#!/usr/bin/node

// a JavaScript script that toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header:
// If the current class is red, when the user clicks on DIV#toggle_header,
// the class must be updated to green ; and the reverse.

$(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
