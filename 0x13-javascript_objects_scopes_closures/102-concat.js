#!/usr/bin/node

// Write a script that concats 2 files.
// The first argument is the file path of the first source file
// The second argument is the file path of the second source file
// The third argument is the file path of the destination

const fs = require('fs');
const path = require('path');

function concatenateFiles (sourceFilePath1, sourceFilePath2, destinationFilePath) {
  try {
    // Read the contents of the first source file
    const content1 = fs.readFileSync(sourceFilePath1, 'utf8');

    // Read the contents of the second source file
    const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

    // Concatenate the contents
    const concatenatedContent = content1 + content2;

    // Write the concatenated content to the destination file
    fs.writeFileSync(destinationFilePath, concatenatedContent);

    console.log(destinationFilePath);
  } catch (error) {
    console.error('Error concatenating files:', error.message);
  }
}

// The __dirname variable represents the current directory where your script resides.
const sourceFile1 = path.resolve(__dirname, 'fileA');
const sourceFile2 = path.resolve(__dirname, 'fileB');
const destinationFile = path.resolve(__dirname, 'fileC');
concatenateFiles(sourceFile1, sourceFile2, destinationFile);
