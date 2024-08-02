#!/usr/bin/node
const fs = require('fs');

// Get the file paths from command-line arguments
const [sourceFile1, sourceFile2, destFile] = process.argv.slice(2);

// Function to read a file and return its content as a promise
const readFile = (filePath) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) return reject(err);
      resolve(data);
    });
  });
};

// Read both source files and write their contents to the destination file
Promise.all([readFile(sourceFile1), readFile(sourceFile2)])
  .then(([data1, data2]) => {
    fs.writeFile(destFile, data1 + data2, (err) => {
      if (err) throw err;
      console.log('Files have been concatenated and written to', destFile);
    });
  })
  .catch((err) => {
    console.error('Error:', err);
  });

