#!/usr/bin/node
function fact (n) {
  if (n === 0) {
    return 1;
  } else {
    return fact(n - 1) * n;
  }
}
if (isNaN(parseInt(process.argv[2]))) {
  console.log(1);
} else {
  console.log(fact(parseInt(process.argv[2])));
}
