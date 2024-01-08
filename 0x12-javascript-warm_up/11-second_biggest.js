#!/usr/bin/node
let biggest = -Infinity;
let secondBiggest = -Infinity;

for (let i = 2; i < process.argv.length; i++) {
  const num = Number(process.argv[i]);

  if (num > biggest) {
    secondBiggest = biggest;
    biggest = num;
  } else if (num > secondBiggest && num !== biggest) {
    secondBiggest = num;
  }
}
if (secondBiggest === -Infinity) {
  console.log(0);
} else {
  console.log(secondBiggest);
}
