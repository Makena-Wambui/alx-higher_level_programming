#!/usr/bin/node

// a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item.
// The new element must be: <li>Item</li>
// The new element must be added to UL.my_list

$(function () {
  $('DIV#add_item').click(function () {
    const myItem = $('<li></li>').text('Item');

    $('UL.my_list').append(myItem);
  });
});
