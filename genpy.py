from lib0 import *
from parser0 import parse
from genx import GenX

class GenPy(GenX):
	def FUNC(self, n):
		self.emit('def ')
		self.emit(f'{n["id"]}(')
		self.gen(n['params'])
		if self.typed and n['class']:
			self.emit(f')->{n["class"]}:')
		else:
			self.emit(f'):')
		self.gen(n['block'])

	def BLOCK(self, n): # BLOCK  = begin STMTS end
		self.level += 1
		self.gen(n['stmts'])
		self.level -= 1
		self.emit('\n')

	def IF(self, n):
		self.emit('if ')
		self.gen(n['expr'])
		self.emit(':')
		self.gen(n['stmt'])
		for el in n['elifList']:
			self.emit('elif ')
			self.gen(el['expr'])
			self.emit(':')
			self.gen(el['stmt'])
		if n['elseStmt']:
			self.emit('else:')
			self.gen(n['elseStmt'])

	def WHILE(self, n):
		self.emit('while ')
		self.gen(n['expr'])
		self.emit(':')
		self.gen(n['stmt'])

	def FOR(self, n):
		self.emit('for ')
		v = n['var']
		id = v if isinstance(v, str) else v['id']
		self.emit(id)
		self.emit(' in ')
		self.gen(n['expr'])
		self.emit(': ')
		self.gen(n['stmt'])
