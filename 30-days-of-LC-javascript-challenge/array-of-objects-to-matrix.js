/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
  const keyValuePairs = arr.map(v => getValue(v));
  const keys = [...new Set(keyValuePairs.flat().map(obj => Object.keys(obj)[0]))].sort()
  const res = [keys]

  for (const row of keyValuePairs) {
    res.push([])
    for (const k of keys) {
      const rowKeys = row.map(r => Object.keys(r)[0]);
      const existKey = rowKeys.includes(k)
      const n = res.length - 1
      
      if (existKey) {
        const v = row.find(r => Object.keys(r).includes(k));

        res[n].push(v[k])
      } else {
        res[n].push('')
      }
    }
  }
  
  return res;
};

const getValue = (obj, key = '', res = []) => {
const isNumber = typeof obj === 'number'
const isString = typeof obj === 'string'
const isBoolean = typeof obj === 'boolean'
const isNull = obj === null

if (isNumber || isString || isBoolean || isNull) {
  return {
    [key]: obj
  }
}

for (const [k, v] of Object.entries(obj)) {
  const composeKey = key ? `${key}.${k}` : `${k}`;
  res.push(getValue(v, composeKey))
}

return res.flat()
}