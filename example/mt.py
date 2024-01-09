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