#!/usr/bin/node
exports.converter = function (base) {
  function conv (a) {
    return a.toString(base);
  }
  return conv;
};
