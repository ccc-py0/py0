# Cython Hello

## 參考

* https://docs.cython.org/en/latest/src/tutorial/cython_tutorial.html

run on linux (linode)

```
root@fqdn:~/ccc/py0/test# cd cython
root@fqdn:~/ccc/py0/test/cython# ls
build.sh  helloworld.pyx  README.md  setup.py  test.py
root@fqdn:~/ccc/py0/test/cython# chmod +x build.sh
root@fqdn:~/ccc/py0/test/cython# ./build.sh
Compiling helloworld.pyx because it changed.
[1/1] Cythonizing helloworld.pyx
/usr/local/lib/python2.7/dist-packages/Cython/Compiler/Main.py:381: FutureWarning: Cython directive 'language_level' not set, using '3str' for now (Py3). This has changed from earlier releases! File: /root/ccc/py0/test/cython/helloworld.pyx
  tree = Parsing.p_module(s, pxd, full_module_name)
running build_ext
building 'helloworld' extension
creating build
creating build/temp.linux-x86_64-2.7
x86_64-linux-gnu-gcc -pthread -fno-strict-aliasing -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-5Z483E/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC -I/usr/include/python2.7 -c helloworld.c -o build/temp.linux-x86_64-2.7/helloworld.o
creating build/lib.linux-x86_64-2.7
x86_64-linux-gnu-gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -fno-strict-aliasing -DNDEBUG -g -fwrapv -O2 -Wall -Wstrict-prototypes -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-5Z483E/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -Wl,-Bsymbolic-functions -Wl,-z,relro -Wdate-time -D_FORTIFY_SOURCE=2 -g -fdebug-prefix-map=/build/python2.7-5Z483E/python2.7-2.7.17=. -fstack-protector-strong -Wformat -Werror=format-security -fPIC build/temp.linux-x86_64-2.7/helloworld.o -o build/lib.linux-x86_64-2.7/helloworld.so
copying build/lib.linux-x86_64-2.7/helloworld.so ->
Hello World
```