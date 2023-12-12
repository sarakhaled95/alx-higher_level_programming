#!/usr/bin/node
const dict = require('./101-data');

const wholeList = Object.entries(dict);
const val = Object.values(dict);
const uniqeVal = [...new Set(val)];
const newDict = {};
for (const i in uniqeVal) {
  const list = [];
  for (const j in wholeList) {
    if (wholeList[j][1] === uniqeVal[i]) {
      list.unshift(wholeList[j][0]);
    }
  }
  newDict[uniqeVal[i]] = list;
}
console.log(newDict);
