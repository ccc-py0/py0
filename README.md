# py0

Py0 is a subset of Python that can be convert into 

1. JavaScript
2. C++/C

and py0 will support the following language in the future

3. Dart
4. C#

## Example 1 : Convert to JavaScript and run

input file: example/mt.py0

```
import sys0

e2c = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)

def mt(s):
	r = []
	words = s.split(' ')
	for e in words: 
		c = e2c[e]
		sys0.push(r, c)

	return sys0.join(r, ' ')

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))
```

generate JavaScript and run

```
$ python py0.py run example/mt.py0 js
-------------- example/mt.js -----------

import * as sys0 from "sys0/sys0.js"
var e2c = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
function mt(s) {
        var r = []
        var words = s.split(' ')
        for (var e of words) {
                var c = e2c[e]
                sys0.push(r , c)
        }

        return sys0.join(r , ' ')
}

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))
---------- run ---------------
e2c= { a: "一隻", dog: "狗", chase: "追", cat: "貓" }
mt(a dog chase a cat)= 一隻 狗 追 一隻 貓
```

## Example 2 : Convert to C 

input file:fib.py0

```
def fib(n:int):
	if n == 0 or n == 1:
		return 1

	return fib(n - 1) + fib(n - 2)

```

run

```
$ python py0.py convert example/fib.py0 c
-------------- example/fib.c -----------

int fib(int n) {
        if (n == 0 || n == 1) {
                return 1;
        }

        return fib(n - 1) + fib(n - 2);
}
```
