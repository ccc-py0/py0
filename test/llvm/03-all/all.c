int x = 3, y = 5, z=3+5;
char *s = "hello";

int add(int a, int b) {
    return a+b;
}

int fib(int n) {
    if (n == 0 || n == 1) return 1;
    return fib(n-1)+fib(n-2);
}

#include <stdio.h>
extern int fib(int n);

int main() {
    printf("fib(5)=%d\n", fib(5));
}