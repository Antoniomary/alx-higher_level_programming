#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  while (list.length) {
    const last = list.pop();
    reversedList.push(last);
  }
  return reversedList;
};
