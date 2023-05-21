/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
  const o1Type = typeof(o1)
  const o2Type = typeof(o2)
  const o1IsArray = Array.isArray(o1)
  const o2IsArray = Array.isArray(o2)
  
  // check o1 and o2 type is equal
  if (o1Type !== o2Type || o1IsArray != o2IsArray) return false

  // if not a object or o1 is null check o1 and o2 is equal 
  if (o1Type !== 'object' || (o1 === null)) return o1 === o2

  // handle array type
  if (o1IsArray) {
    if (o1.length !== o2.length) return false
    
    for (const i in o1) {
      const isSame = areDeeplyEqual(o1[i],o2[i])
      
      if (!isSame) return false
    }
  }

  // handle object type
  const o1Keys = Object.keys(o1)
  const o2Keys = Object.keys(o2)
  if (o1Keys.length !== o2Keys.length) return false

  for (const i in o1Keys) {
    const key = o1Keys[i]
    const isSame = areDeeplyEqual(o1[key], o2[key])

    if (!isSame) return false
  }

  return true
};