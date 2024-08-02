#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number === 0) return '0';
    
    function toBase(num) {
      return num === 0 ? '' : toBase(Math.floor(num / base)) + '0123456789abcdef'[num % base];
    }
    
    return toBase(number);
  };
};

