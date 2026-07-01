#!/usr/bin/node
const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < n) {
    console.log('X'.repeat(n));
    i++;
  }
}
