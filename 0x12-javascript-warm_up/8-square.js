#!/usr/bin/node
if (parseInt(process.argv[2], 0)) {
  for (let i = 0; i < parseInt(process.argv[2], 0); i++) {
    let lsquare = '';
    for (let j = 0; j < parseInt(process.argv[2], 0); j++) {
      lsquare += 'X';
    }
    console.log(lsquare);
  }
} else {
  console.log('Missing size');
}
