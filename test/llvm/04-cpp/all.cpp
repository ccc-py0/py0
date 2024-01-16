#include <iostream>

int x = 3, y = 5, z=3+5;
std::string str = "hello";

int add(int a, int b) {
    return a+b;
}

int fib(int n) {
    if (n == 0 || n == 1) return 1;
    return fib(n-1)+fib(n-2);
}


int main() {
    std::cout << "fib(5)=" << fib(5) << std::endl;
}
