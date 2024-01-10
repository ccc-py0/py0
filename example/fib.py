import sys
sys.path.append("sys0")

import sys0
def fib(n)->int:
	if n == 0 or n == 1:
		return 1

	return fib(n - 1) + fib(n - 2)

def main():
	print('fib(5)=' , fib(5))

main()