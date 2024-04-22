#!/usr/bin/node

const cliArgs = process.argv;
const size = Number(cliArgs[2]);

if (size === undefined || isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
