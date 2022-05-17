#!/usr/bin/node

let fs = require('fs');
fs.readFile(arguments[1], bar)
function bar(err, data)
{
    err ? Function("error","throw error")(err) : console.log(JSON.stringify(data) );
}