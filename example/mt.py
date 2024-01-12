import sys
sys.path.append("sys0")

import sys0
e2c:dict = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
def mt(s:str)->str:
	r:list = []
	words = sys0.split(s , ' ')
	for e in words: 
		c:str = e2c[e]
		sys0.push(r , c)

	return sys0.join(r , ' ')

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))