//@ts-check

/**
Iterate back and forth on an array of callbacks,
calling each callback in a "triangular waveform" order.

This is a regular loop followed by a reverse loop, calling the ends once per "bounce".
@param {number|bigint} iterations Times to iterate. Reverse iters are part of regular iters, so they aren't counted
@param {...() => void} callbacks
*/
export const zfor = (iterations = 0, ...callbacks) => {
	while (iterations-- > 0) {
		let i = 0
		for (; i < callbacks.length; i++)
			callbacks[i]()

		i -= 2
		for (; i > 0; i--)
			callbacks[i]()

		if (iterations < 1)
			callbacks[0]() //bad patch
	}
}

/**
Iterate back and forth on an array of callbacks,
calling each callback in a "hexagonal waveform" order.

This is a regular loop followed by a reverse loop, calling the ends twice per "bounce".
@param {number|bigint} iterations Times to iterate. Reverse iters are part of regular iters, so they aren't counted
@param {...() => void} callbacks
*/
export const xzfor = (iterations = 0, ...callbacks) => {
	while (iterations-- > 0) {
		let i = 0
		for (; i < callbacks.length; i++)
			callbacks[i]()

		i -= 1
		for (; i >= 0; i--)
			callbacks[i]()

		if (iterations < 1)
			callbacks[0]() //bad patch
	}
}
