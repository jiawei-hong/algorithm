/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
  const isNull = object == null
  const isObject = typeof object === 'object'
  const isArray = Array.isArray(object)
  const isString = typeof object === 'string'

  if (isNull) return 'null';

  if (isArray) {
    const elements = object.map(ele => jsonStringify(ele));
    return `[${elements.join(',')}]`;
  }

  if (isObject) {
    const keys = Object.keys(object)
    const values = keys.map(key => `"${key}":${jsonStringify(object[key])}`)
    return `{${values.join(',')}}`
  }

  if (isString) {
    return `"${object}"`
  }

  return object.toString()
};