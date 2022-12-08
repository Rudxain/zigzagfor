const main = () => {
	const log = console.log

	const cbs = [
		() => log('0'),
		() => log('1'),
		() => log('2')
	]

	log('z')
	zfor(2, ...cbs)
	//logs: 0 1 2 1 0 1 2 1 0

	log('xz')
	xzfor(2, ...cbs)
	//logs: 0 1 2 2 1 0 0 1 2 2 1 0 (actually has an extra 0, but that's a bug)
}
main()
