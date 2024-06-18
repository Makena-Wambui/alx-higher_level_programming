#!/usr/bin/node

// Write a function that returns the number of occurrences in a list
// list here is an array
// searchelement is the number whose occurences in the list we are counting

exports.nbOccurences = function (list, searchElement) {
  // this variable keeps track of the occurence of that element.
  let occurrences = 0;

  // iterate through the list using a for loop
  // list is essentially an array so we can use the length property
  let a;
  for (a = 0; a < list.length; a++) {
    // if that element is found at that index in the array, then increment the variable occurences.
    if (searchElement === list[a]) {
      occurrences++;
    }
  }
  return occurrences;
};
