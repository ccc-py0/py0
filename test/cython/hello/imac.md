
```
base) nqucsie2022@NeXT11 hello % ./build.sh
Compiling helloworld.pyx because it changed.
[1/1] Cythonizing helloworld.pyx
/usr/local/lib/python3.11/site-packages/Cython/Compiler/Main.py:381: FutureWarning: Cython directive 'language_level' not set, using '3str' for now (Py3). This has changed from earlier releases! File: /Users/nqucsie2022/Desktop/ccc/py0/test/cython/hello/helloworld.pyx
  tree = Parsing.p_module(s, pxd, full_module_name)
running build_ext
building 'helloworld' extension
creating build
creating build/temp.macosx-10.15-x86_64-cpython-311
clang -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk -I/usr/local/opt/python@3.11/Frameworks/Python.framework/Versions/3.11/include/python3.11 -c helloworld.c -o build/temp.macosx-10.15-x86_64-cpython-311/helloworld.o
creating build/lib.macosx-10.15-x86_64-cpython-311
clang -bundle -undefined dynamic_lookup -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk build/temp.macosx-10.15-x86_64-cpython-311/helloworld.o -o build/lib.macosx-10.15-x86_64-cpython-311/helloworld.cpython-311-darwin.so
copying build/lib.macosx-10.15-x86_64-cpython-311/helloworld.cpython-311-darwin.so -> 
Hello World
```
