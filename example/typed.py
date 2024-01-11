import sys
sys.path.append("sys0")

import sys0
a:int = 1
b:int = 2
c:int = a + b
print('c=' , c)
def sum(n:int)->int:
	s:int = 0
	for i in range(1 , n + 1): 
		s = s + i

	return s

print('sum(10)=' , sum(10))
e2c:dict = {'a':'一隻','dog':'狗','chase':'追','cat':'貓'}
print('e2c=' , e2c)
def mt(s:str)->str:
	r:list = []
	words:list = s.split(' ')
	for e in words: 
		c = e2c[e]
		sys0.push(r , c)

	return sys0.join(r , ' ')

print('mt(a dog chase a cat)=' , mt('a dog chase a cat'))