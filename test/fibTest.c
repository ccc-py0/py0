#include <sys0.h>

int fib(int n) {
		if (n == 0 || n == 1) {
				return 1;
		}

		return fib(n - 1) + fib(n - 2);
}

int main() {
	print("fib(5)=" , fib(5));
}
