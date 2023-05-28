/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
  let group = {}

  for (const element of this) {
    const data = fn(element)

    if (data in group) {
      group[data].push(element)
    } else {
      group[data] = [element]
    }
  }

  return group
};

/**
* [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
*/