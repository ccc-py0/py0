# clang -S -emit-llvm add.c
clang add.ll main.c -o main
./main
