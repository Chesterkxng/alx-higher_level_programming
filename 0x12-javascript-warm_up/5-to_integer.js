#!/usr/bin/node
if (parseInt(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2], 0));
} else {
  console.log('Not a number');
}
