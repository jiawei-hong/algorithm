/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
  this._count = init

  const increment = () => this._count+=1
  const reset = () => this._count = init
  const decrement =() => this._count-=1

  return {
      increment,
      reset,
      decrement,
  }
};

/**
* const counter = createCounter(5)
* counter.increment(); // 6
* counter.reset(); // 5
* counter.decrement(); // 4
*/