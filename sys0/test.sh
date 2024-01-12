# g++ -std=c++11 sys0.cpp test.cpp
set -x
g++ -std=c++17 -finput-charset=utf-8 -fexec-charset=big5 sys0.cpp test.cpp -o test
./test

