from lib0 import *
from parser0 import parse
from genx import GenX

class GenPy(GenX):
	def VAR(self, n, isNew):
		self.emit(n["id"])

	def FUNC(self, n):
		self.emit(f'def {n["id"]}(')
		self.gen(n['params'])
		self.emit('):')
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
		self.gen(n['var'])
		self.emit(' in ')
		self.gen(n['expr'])
		self.emit(': ')
		self.gen(n['stmt'])
