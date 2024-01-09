
import * as sys0 from "sys0/sys0.js"
function fib(n) {
	if (n == 0 || n == 1) {
		return 1
	}

	return fib(n - 1) + fib(n - 2)
}

function main() {
	print('fib(5)=' , fib(5))
}

main()