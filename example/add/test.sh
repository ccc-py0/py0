# clang -S -emit-llvm add.c
clang add.ir.ll main.c -o main
./main
