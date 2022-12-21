from typing import Final

NEG_ITER_MSG: Final = 'cannot time travel'
'''error message for negative iteration count'''


def zfor(iterations: int = 0, *callbacks):
	'''
	Iterate back and forth on an array of callbacks,
	calling each callback in a "triangular waveform" order.

	This is a regular loop followed by a reverse loop, calling the ends once per "bounce".

	`iterations` Times to iterate. Reverse iters are part of regular iters, so they aren't counted
	'''
	if iterations < 0:
		raise ValueError(NEG_ITER_MSG)

	# if a big int is passed, this would reduce memory use
	# `for _ in range(iterations)` dupes memory
	while iterations > 0:
		iterations -= 1
		i = 0
		while i < len(callbacks):
			callbacks[i]()
			i += 1

		i -= 2
		while i > 0:
			callbacks[i]()
			i -= 1

		if iterations < 1:
			callbacks[0]()  # bad patch


def xzfor(iterations: int = 0, *callbacks):
	'''
	Iterate back and forth on an array of callbacks,
	calling each callback in a "hexagonal waveform" order.

	This is a regular loop followed by a reverse loop, calling the ends twice per "bounce".

	`iterations` Times to iterate. Reverse iters are part of regular iters, so they aren't counted
	'''
	if iterations < 0:
		raise ValueError(NEG_ITER_MSG)

	# if a big int is passed, this would reduce memory use
	# `for _ in range(iterations)` dupes memory
	while iterations > 0:
		iterations -= 1
		i = 0
		while i < len(callbacks):
			callbacks[i]()
			i += 1

		i -= 1
		while i >= 0:
			callbacks[i]()
			i -= 1