#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let temp = list;
  let count = 0;
  let index;
  while (true) {
    index = temp.indexOf(searchElement);
    if (index !== -1) {
      count++;
      temp = temp.slice(index + 1);
    } else {
      break;
    }
  }
  return count;
};
