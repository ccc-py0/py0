from lib0 import *
from parser0 import parse
from genx import GenX

class GenC(GenX):
	def IMPORT(self, n):
		id = n['id']
		self.emit(f'#include <sys0.h>')

	def FUNC(self, n):
		self.emit(f'int {n["id"]}(')
		self.gen(n['params'])
		self.emit(')')
		self.gen(n['block'])

	def PARAMS(self, n):
		params = n['params']
		if len(params) == 0: return
		for param in params[0:-1]:
			self.emit('int ')
			self.gen(param)
			self.emit(',')
		self.emit('int ')
		self.gen(params[-1])

	def STMT(self, n):
		ty = n['stmt']['type']
		if ty != 'block': # block 也是一種 stmt，但不需要換行，因為裡面的 stmt* 每個都會換
			self.emit(f'\n{self.indent()}')
		self.gen(n['stmt'])
		if not ty in ['block', 'if', 'while', 'func', 'for', 'import']:
		    self.emit(';')		
		
	def STRING(self, n):
		self.emit(n['value'].replace("'",'"'))

	def FOR(self, n):
		self.emit('for (')
		self.gen(n['var'])
		self.emit(' of ')
		self.gen(n['expr'])
		self.emit(')')
		self.gen(n['stmt'])

	def BEXPR(self, n):
		opMap = {'and':'&&', 'or':'||'}
		for e in n['list']:
			if isinstance(e, str): # op
				self.emit(f' {opMap[e]} ')
			else:
				self.gen(e)
