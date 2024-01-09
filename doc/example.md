# py0 -- example

## Example 1 -- mt.py0

file: mt.py0

```py
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

file: mt.sh

```bash
set -x
python py0.py convert example/mt.py0 js
deno run example/mt.js

python py0.py convert example/mt.py0 py
python example/mt.py
```

run mt.sh

```
$ ./mt.sh
++ python py0.py convert example/mt.py0 js

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
finished!
++ deno run example/mt.js
e2c= { a: "一隻", dog: "狗", chase: "追", cat: "貓" }
mt(a dog chase a cat)= 一隻 狗 追 一隻 貓
++ python py0.py convert example/mt.py0 py
import sys
sys.path.append("sys0")

import sys0
e2c = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
def mt(s):
        r = []
        words = s.split(' ')
        for e in words:
                c = e2c[e]
                sys0.push(r , c)

        return sys0.join(r , ' ')

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))
finished!
++ python example/mt.py
e2c= {'a': '一隻', 'dog': '狗', 'chase': '追', 'cat': '貓'}
mt(a dog chase a cat)= 一隻 狗 追 一隻 貓
```
