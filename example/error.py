e2c = {'a':'一隻', 'dog':'狗', 'chase':'追', 'cat':'貓'}
print('e2c=', e2c)

def mt(s):
	r = []
	words = s.split(' ')
	for e in words:
		c = e2c[e]
		r.append(c)
		++*
	return ' '.join(r)

print('mt(a dog chase a cat)=', mt('a dog chase a cat'))
