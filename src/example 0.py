from typing import Final
from lib import zfor, xzfor

def main():
	cbs: Final = (
		lambda: print('0'),
		lambda: print('1'),
		lambda: print('2')
	)

	print('z')
	zfor(2, *cbs)
	# logs: 0 1 2 1 0 1 2 1 0

	print('xz')
	xzfor(2, *cbs)
	# logs: 0 1 2 2 1 0 0 1 2 2 1 0 (actually has an extra 0, but that's a bug)

if __name__ == '__main__':
	main()