python3 setup.py build_ext --inplace

gcc -fPIC $(python3-config --cflags --ldflags) hello.c

