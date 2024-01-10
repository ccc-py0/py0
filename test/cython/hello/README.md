# Cython Hello

## 參考

* https://docs.cython.org/en/latest/src/tutorial/cython_tutorial.html

## 編譯後執行

run on linux (linode)

```

root@fqdn:~/ccc/py0/test/cython/hello# chmod +x build.sh
root@fqdn:~/ccc/py0/test/cython/hello# ./build.sh
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

## 用 pyximport 直接編譯執行

```
pyximport: Cython Compilation for Developers
If your module doesn’t require any extra C libraries or a special build setup, then you can use the pyximport module, originally developed by Paul Prescod, to load .pyx files directly on import, without having to run your setup.py file each time you change your code. It is shipped and installed with Cython and can be used like this:
```
