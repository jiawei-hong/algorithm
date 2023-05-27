/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, depth) {
  let res = [];

  const flatten = (arr, _depth) => {
      for (const data of arr) {
          if (Array.isArray(data) && _depth > 0) {
              flatten(data, _depth - 1)
          } else {
              res.push(data)
          }
      }
  }

  flatten(arr, depth)

  return res
};