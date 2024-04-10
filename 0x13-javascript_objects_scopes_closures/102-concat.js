#!/usr/bin/node
//Write a script that concats 2 files.

const file = require('file');
const A = file.readFileSync(process.argv[2], 'utf8');
const B = file.readFileSync(process.argv[3], 'utf8');
file.writeFileSync(process.argv[4], A + B);
