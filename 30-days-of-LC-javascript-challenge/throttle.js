/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var throttle = function(fn, t) {
  let timer = null;
  let tempArgs = null;

  return function(...args) {
    if (timer) {
      tempArgs = args
    } else {
      fn(...args)
      timer = setInterval(() => {
        if (tempArgs) {
          fn(...tempArgs)
          tempArgs = null
        } else {
          clearInterval(timer)
          timer = null
        }
      },t)
    }
  }
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */