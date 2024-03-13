#!/usr/bin/node

class counter {
  static i = 0;

  static increment () {
    counter.i++;
  }
}

exports.logMe = function (item) {
  console.log(counter.i + ': ' + item);
  counter.increment();
};
