#!/usr/bin/node
const argvLen = process.argv.length - 2;
if (argvLen === 0) console.log('No argument');
if (argvLen === 1) console.log('Argument found');
if (argvLen >= 2) console.log('Arguments found');
