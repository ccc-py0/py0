from lib0 import *
from parser0 import parse
from genx import GenX
from gen import gen

class GenPy(GenX):
	def FUNC(self, n):
		emit(f'def {n["id"]}(')
		gen(n['params'], self)
		emit('):')
		gen(n['block'], self)

	def BLOCK(self, n): # BLOCK  = begin STMTS end
		self.level += 1
		gen(n['stmts'], self)
		self.level -= 1
		emit('\n')
	def IF(self, n):
		emit('if ')
		gen(n['expr'], self)
		emit(':')
		gen(n['stmt'], self)
		for el in n['elifList']:
			emit('elif ')
			gen(el['expr'], self)
			emit(':')
			gen(el['stmt'], self)
		if n['elseStmt']:
			emit('else:')
			gen(n['elseStmt'], self)

	def WHILE(self, n):
		emit('while ')
		gen(n['expr'], self)
		emit(':')
		gen(n['stmt'], self)

	def FOR(self, n):
		emit('for ')
		emit(n['id'])
		emit(' in ')
		gen(n['expr'], self)
		emit(' : ')
		gen(n['stmt'], self)

# 測試詞彙掃描器
if __name__ == "__main__":
	from test0 import code
	ast = parse(code)
	print(ast)
	g = GenPy()
	gen(ast, g)
