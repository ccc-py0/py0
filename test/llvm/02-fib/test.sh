# clang -S -emit-llvm add.c
clang fib.ll main.c -o main
./main
