#!/usr/bin/node
if (parseInt(process.argv[2], 0)) {
  for (let i = 0; i < parseInt(process.argv[2], 0); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
