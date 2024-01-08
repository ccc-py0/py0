from lib0 import *
from parser0 import parse
from genx import GenX
from gen import gen

class GenJs(GenX):
	def FOR(self, n):
		emit('for (let ')
		emit(n['id'])
		emit(' in ')
		gen(n['expr'], self)
		emit(')')
		gen(n['stmt'], self)


# 測試詞彙掃描器
if __name__ == "__main__":
	from test0 import code
	ast = parse(code)
	print(ast)
	g = GenJs()
	gen(ast, g)