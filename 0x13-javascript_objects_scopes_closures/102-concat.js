#!/usr/bin/node

// Import the required modules
const fs = require('fs');
const path = require('path');

function concatenateFiles(sourceFilePath1, sourceFilePath2, destinationFilePath) {
  try {
    // Read the contents of the first source file
    const content1 = fs.readFileSync(sourceFilePath1, 'utf8');

    // Read the contents of the second source file
    const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

    // Concatenate the contents
    const concatenatedContent = content1 + content2;

    // Write the concatenated content to the destination file
    fs.writeFileSync(destinationFilePath, concatenatedContent);

  } catch (error) {
    console.error('Error concatenating files:', error.message);
  }
}


// Get the file paths from command-line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Call the function to concatenate the files
concatenateFiles(sourceFile1, sourceFile2, destinationFile);
