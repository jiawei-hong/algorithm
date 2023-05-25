/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
  const n = arr.length;
  let res = [];

  for(let i = 0;i < n;i += size) {
      res.push(arr.slice(i, i + size))
  }

  return res;
};